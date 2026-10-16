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

The default `/mcp` endpoint serves the full tool catalog. Both plugin endpoints,
`/mcp/openai` and `/mcp/claude`, include CRM, company mail, ads, social, payments
administration, domain management, design, and Library tools. Billing commerce,
domain purchase and renewal, and other explicitly excluded tools remain
available only through general MCP.

Media generation and the `generate-image`/`generate-video` prompts are available
through `/mcp` and `/mcp/openai`. `/mcp/claude` excludes those tools and prompts;
`media_get` remains available on all three endpoints to read existing jobs.
All three endpoints use the same Cofounder account, with their own OAuth resource
identities. Plugin eligibility is explicit per tool; future tools on general MCP
are not automatically included in plugin catalogs. When the OAuth proxy is enabled,
plugin authorization routes live under `/mcp/openai/oauth` and `/mcp/claude/oauth`;
the upstream Supabase client must allow both additional redirects:
`<backend-url>/mcp/openai/oauth/callback` and
`<backend-url>/mcp/claude/oauth/callback`. Connection listing and revocation cover
all profiles. This adds endpoint support; plugin directory availability is separate.
