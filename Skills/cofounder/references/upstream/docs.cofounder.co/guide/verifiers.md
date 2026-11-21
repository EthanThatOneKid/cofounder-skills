# Verifiers

Source: https://docs.cofounder.co/guide/verifiers
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Create or improve social carousels, videos, copy, website designs and market strategy from context and optional content.

Verifiers are not available to every company yet. Access is enabled selectively
during rollout.

Choose a verifier and provide the goals and references it should work from.
The working agent creates or improves the deliverables and returns the finished
output after rubric checks pass. Content uses independent JEV checks alongside agent inspection; the other
verifiers use agent evaluation. Website runs also include an
implementation handoff for the agent with access to the customer repository and
services.

| Verifier | Output |
| --- | --- |
| `content` | Finished social carousels, videos and accompanying copy saved to the company Library, with slide order, preview and download links |
| `copy` | Finished text, including image-ad copy |
| `website` | Library ZIP containing improved frames, implementation files and an implementation handoff selected from your brief |
| `market` | Market strategy covering the ICP, audience and approach to building the business |

Website runs use public URLs or screenshots. They do not require source code,
a repository or a custom domain, and the output is a design handoff rather than
a working customer application. Content runs create assets; they do not publish posts or launch campaigns.

Use `copy` for image-ad wording. Supply the image to review its headline,
on-image wording and accompanying copy together; the result is finished text.
Use `content` for finished social carousels and videos, whether paid ads or
organic posts. It is optional delegation: an agent using `slideshows.generate`
or media tools directly does not need to call a verifier afterward.

Content runs default to one finished piece. Open briefs compare a few text
concepts before producing only the selected direction. Carousels use the
slideshow tools by default; video uses creative research, reference inspection
and media production. Supply finished slides or videos in `content` to improve
them. Include their order and any existing generation recipe in context. The
agent inspects them first, preserves useful work and can return an already
suitable piece unchanged. Rendered slides are flattened images; text-layer
editing or exact reconstruction from a prompt-only request is not promised.
