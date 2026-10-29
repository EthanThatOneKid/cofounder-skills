# Verify work

Source: https://docs.cofounder.co/guide/verify-work
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Review deployed products, copy, ads and research through one API operation.

Choose a verifier and submit a deployed URL or company Library references.
Reviews run as company jobs and incur model usage charges. A previous verifier
pass is not a prerequisite. You do not supply routes, roles or viewports.

| Name | Submission | Required context |
| --- | --- | --- |
| `copy` | URL or `copy` Library reference | Voice is optional for general copy quality |
| `brand-identity` | URL | Identity and voice |
| `product-dev` | URL | Product requirements and voice |
| `ads` | `manifest` Library reference | Brief, identity, voice, assets and matching copy |
| `market-research` | Library documents | ICP, pain, product, value and mission/vision |

Identity, voice and research references default to the company's saved Library
documents. An explicit `references` entry overrides its default using `key`,
`title` and `library_path`. Documents must be UTF-8 text. Ads manifests refer to
PNG, JPEG, WebP or MP4 assets through Library paths. Missing required evidence is
reported before starting paid judges.

The `market-research` judge compares the five frozen documents for material
contradictions, citing both conflicting statements and their document locations.
It does not verify sources, factual accuracy, research depth or market viability.
A pass means no material contradiction was found. Existing jobs retain their
frozen criteria; submit with a new idempotency key to use updated criteria.
