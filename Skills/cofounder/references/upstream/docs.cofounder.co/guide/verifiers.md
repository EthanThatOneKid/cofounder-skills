# Verifiers

Source: https://docs.cofounder.co/guide/verifiers
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Create or improve video ads, copy, website designs and market strategy from context and optional content.

Verifiers are not available to every company yet. Access is enabled selectively
during rollout.

Choose a verifier and provide the goals and references it should work from.
The working agent creates or improves the deliverables and returns the finished
output after rubric checks pass. Ads use independent JEV evaluation; the other
verifiers use agent evaluation. Website runs also include an
implementation handoff for the agent with access to the customer repository and
services.

| Verifier | Output |
| --- | --- |
| `ads` | Finished videos and accompanying ad text saved to the company Library, with preview and download links |
| `copy` | Finished text, including image-ad copy |
| `website` | Library ZIP containing improved frames, implementation files and an implementation handoff selected from your brief |
| `market` | Market strategy covering the ICP, audience and approach to building the business |

Website runs use public URLs or screenshots. They do not require source code,
a repository or a custom domain, and the output is a design handoff rather than
a working customer application. Ads runs create assets; they do not launch campaigns.

Use `copy` for image-ad wording. Supply the image to review its headline,
on-image wording and accompanying copy together; the result is finished text.
Use `ads` for finished video ads. Artwork and keyframes remain part of video
production, rather than standalone image-ad deliverables.
