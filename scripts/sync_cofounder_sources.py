#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

DEFAULT_DOCS_FULL_URL = "https://docs.cofounder.co/llms-full.txt"
DEFAULT_SITE_MAP_URL = "https://cofounder.co/llms.txt"
DEFAULT_OUTPUT_DIR = Path("references/upstream")
DEFAULT_MANIFEST = DEFAULT_OUTPUT_DIR / "manifest.json"


@dataclass(frozen=True)
class Document:
    title: str
    source_url: str
    content: str
    fetched_from: str


def fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; cofounder-skills-sync/1.0)",
            "Accept": "text/markdown, text/plain, */*;q=0.8",
        },
    )
    with urlopen(request, timeout=120) as response:
        return response.read().decode("utf-8")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "index"


def source_to_relative_path(source_url: str, title: str) -> Path:
    parsed = urlparse(source_url)
    host = parsed.netloc or "unknown-source"
    raw_path = unquote(parsed.path).strip("/")

    if not raw_path:
        raw_path = "index"

    if raw_path.endswith(".html.md"):
        raw_path = raw_path.removesuffix(".html.md")
    elif raw_path.endswith(".md"):
        raw_path = raw_path.removesuffix(".md")
    elif raw_path.endswith("/"):
        raw_path = raw_path.rstrip("/")

    if not raw_path:
        raw_path = slugify(title)

    return Path(host) / f"{raw_path}.md"


def parse_docs_full(text: str, fetched_from: str) -> list[Document]:
    lines = text.splitlines()
    sections: list[list[str]] = []
    current: list[str] = []

    for line in lines:
        if line.startswith("## ") and not line.startswith("## Documentation"):
            if current:
                sections.append(current)
            current = [line]
            continue
        if current:
            current.append(line)

    if current:
        sections.append(current)

    documents: list[Document] = []
    for section in sections:
        title = section[0][3:].strip()
        source_url = ""
        body_start = 1

        for index, line in enumerate(section[1:], start=1):
            if line.startswith("**URL:** "):
                source_url = line.removeprefix("**URL:** ").strip()
                body_start = index + 1
                break

        if not source_url:
            continue

        body = "\n".join(section[body_start:]).strip()
        if not body:
            continue

        content = f"# {title}\n\nSource: {source_url}\nFetched from: {fetched_from}\n\n{body}\n"
        documents.append(
            Document(
                title=title,
                source_url=source_url,
                content=content,
                fetched_from=fetched_from,
            )
        )

    return documents


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    links: list[tuple[str, str]] = []
    for title, url in re.findall(r"- \[([^\]]+)\]\((https?://[^)]+)\)", text):
        links.append((title.strip(), url.strip()))
    return links


def markdown_candidates(url: str) -> list[str]:
    parsed = urlparse(url)
    path = parsed.path

    candidates: list[str] = []
    if path.endswith(".md") or path.endswith(".html.md"):
        candidates.append(url)
    elif parsed.netloc == "cofounder.co":
        candidates.append(f"{url}.md")
        candidates.append(f"{url}.html.md")
        candidates.append(url)
    else:
        candidates.append(url)

    deduped: list[str] = []
    for candidate in candidates:
        if candidate not in deduped:
            deduped.append(candidate)
    return deduped


def fetch_first_markdown(url: str) -> tuple[str, str]:
    errors: list[str] = []
    for candidate in markdown_candidates(url):
        try:
            text = fetch_text(candidate)
        except Exception as error:  # noqa: BLE001 - preserve URL-specific scrape failures
            errors.append(f"{candidate}: {error}")
            continue

        stripped = text.lstrip()
        if stripped.startswith("<!DOCTYPE html") or stripped.startswith("<html"):
            errors.append(f"{candidate}: returned HTML, not markdown")
            continue
        return candidate, text

    raise RuntimeError(f"No markdown source found for {url}: {'; '.join(errors)}")


def normalize_linked_document(title: str, source_url: str, markdown_url: str, text: str) -> Document:
    body = text.strip()
    if not body:
        raise ValueError(f"Empty markdown document: {markdown_url}")

    if body.startswith("# "):
        content = f"{body}\n"
    else:
        content = f"# {title}\n\n{body}\n"

    if "Source: " not in content[:500] and "Canonical: " not in content[:500]:
        content = f"# {title}\n\nSource: {source_url}\nFetched from: {markdown_url}\n\n{body}\n"

    return Document(
        title=title,
        source_url=source_url,
        content=content,
        fetched_from=markdown_url,
    )


def collect_documents(docs_full_url: str, site_map_url: str) -> tuple[list[Document], list[dict[str, str]]]:
    documents: list[Document] = []
    failures: list[dict[str, str]] = []

    docs_full = fetch_text(docs_full_url)
    documents.extend(parse_docs_full(docs_full, docs_full_url))

    site_map = fetch_text(site_map_url)
    for title, source_url in extract_markdown_links(site_map):
        if urlparse(source_url).netloc != "cofounder.co":
            continue
        try:
            markdown_url, text = fetch_first_markdown(source_url)
        except Exception as error:  # noqa: BLE001 - keep scrape resilient to upstream link drift
            failures.append({"title": title, "source_url": source_url, "error": str(error)})
            continue
        documents.append(normalize_linked_document(title, source_url, markdown_url, text))

    seen: set[str] = set()
    deduped: list[Document] = []
    for document in documents:
        if document.source_url in seen:
            continue
        seen.add(document.source_url)
        deduped.append(document)

    return deduped, failures


def write_document(output_dir: Path, document: Document) -> Path:
    relative_path = source_to_relative_path(document.source_url, document.title)
    output_path = output_dir / relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document.content, encoding="utf-8")
    return relative_path


def prune_stale_files(output_dir: Path, active_paths: set[Path], manifest_path: Path) -> list[Path]:
    removed: list[Path] = []
    if not output_dir.exists():
        return removed

    manifest_resolved = manifest_path.resolve()
    for path in sorted(output_dir.rglob("*.md")):
        if path.relative_to(output_dir) not in active_paths and path.resolve() != manifest_resolved:
            path.unlink()
            removed.append(path)

    for directory in sorted((path for path in output_dir.rglob("*") if path.is_dir()), reverse=True):
        if not any(directory.iterdir()):
            directory.rmdir()

    return removed


def build_manifest(
    documents: Iterable[Document],
    output_dir: Path,
    docs_full_url: str,
    site_map_url: str,
    failures: list[dict[str, str]],
) -> dict:
    items = []
    for document in documents:
        relative_path = source_to_relative_path(document.source_url, document.title)
        items.append(
            {
                "title": document.title,
                "source_url": document.source_url,
                "fetched_from": document.fetched_from,
                "path": str(relative_path).replace("\\", "/"),
                "sha256": hashlib.sha256(document.content.encode("utf-8")).hexdigest(),
            }
        )

    return {
        "sources": {
            "docs_full_url": docs_full_url,
            "site_map_url": site_map_url,
        },
        "output_dir": str(output_dir),
        "count": len(items),
        "failure_count": len(failures),
        "failures": failures,
        "items": items,
    }


def sync(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    manifest_path = Path(args.manifest)
    documents, failures = collect_documents(args.docs_full_url, args.site_map_url)

    if not documents:
        print("No documents collected.", file=sys.stderr)
        return 1

    manifest = build_manifest(documents, output_dir, args.docs_full_url, args.site_map_url, failures)

    if args.dry_run:
        print(json.dumps(manifest, indent=2))
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)

    written_paths: set[Path] = set()
    for document in documents:
        written_paths.add(write_document(output_dir, document))

    removed = prune_stale_files(output_dir, written_paths, manifest_path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {len(written_paths)} markdown files to {output_dir}")
    if removed:
        print(f"Removed {len(removed)} stale markdown files")
    if failures:
        print(f"Skipped {len(failures)} unavailable markdown sources", file=sys.stderr)
    print(f"Manifest: {manifest_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Cofounder public markdown sources.")
    parser.add_argument("--docs-full-url", default=DEFAULT_DOCS_FULL_URL)
    parser.add_argument("--site-map-url", default=DEFAULT_SITE_MAP_URL)
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    return sync(args)


if __name__ == "__main__":
    raise SystemExit(main())
