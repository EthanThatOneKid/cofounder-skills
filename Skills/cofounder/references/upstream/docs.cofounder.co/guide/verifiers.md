# Verifiers

Source: https://docs.cofounder.co/guide/verifiers
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Create or improve ads, copy, website designs and market strategy from context and optional content.

Verifiers are not available to every company yet. Access is enabled by environment
during rollout.

Choose a verifier and provide the goals and references it should work from.
The working agent creates or improves the deliverables and returns the finished
output after rubric checks pass. Ads use independent JEV evaluation; the other
verifiers use agent evaluation. Website runs also include an
implementation handoff for the agent that will build the design.

| Verifier | Output |
| --- | --- |
| `ads` | Finished images, videos and any ad text saved to the company Library, with preview and download links |
| `copy` | The finished copy |
| `website` | Library ZIP containing improved frames, implementation files and an implementation handoff selected from your brief |
| `market` | Market strategy covering the ICP, audience and approach to building the business |

Website runs use public URLs or screenshots. They do not require source code,
a repository or a custom domain, and the output is a design handoff rather than
a working customer application. Ads runs create assets; they do not launch campaigns.
