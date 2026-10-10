# MCP Beyond Tools

Source: https://docs.cofounder.co/cli/advanced/mcp-apps-prompts-resources
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** What the hosted MCP server serves besides tools: resources for billing, the Library, outputs, and skills; prompts as slash commands; and the CRM board and domain purchaser.

With the Codex or Claude plugins, your agent cannot buy credits, manage
auto-recharge, retry payments, purchase or renew domains, or create Link spend
requests and retrieve card details. Use the CLI dashboard for these actions;
missing domain, retry, and Link flows will be available soon. The CLI and
general `/mcp` retain these tools.

Tools are most of the MCP surface, but not all of it. Your agent can also
read resources on demand, pick up prompts as slash commands, and open the
CRM board and the domain purchaser.

The default `/mcp` endpoint serves the full tool catalog, including media
generation. `/mcp/claude` serves that catalog without `media_generate` or the
`generate-image`/`generate-video` prompts; `media_get` remains available to
read existing jobs. `/mcp/openai` is a curated catalog for coding agents:
the company-operations core covering identity and membership, company setup,
code and repositories, database, hosting, domains the company already owns,
playbooks, events, support, research, and billing. Bulk-operations surfaces
such as CRM, company mail, ads, social, payments admin, registrar domain
operations, and design stay on `/mcp` and `/mcp/claude`; media generation is
`/mcp` only, as are domain purchase and renewal. Library reads, search,
text writes, uploads, and URL ingestion stay in `/mcp/openai` because the
text operations' guidance and the brand kit's recovery steps call them;
file publishing and deletion are `/mcp` and `/mcp/claude` only.
All three endpoints use the same Cofounder account, with their own OAuth resource
identities. Plugin eligibility is explicit per tool; future tools on general MCP
are not automatically included in plugin catalogs. When the OAuth proxy is enabled,
plugin authorization routes live under `/mcp/openai/oauth` and `/mcp/claude/oauth`;
the upstream Supabase client must allow both additional redirects:
`<backend-url>/mcp/openai/oauth/callback` and
`<backend-url>/mcp/claude/oauth/callback`. Connection listing and revocation cover
all profiles. This adds endpoint support; plugin directory availability is separate.
