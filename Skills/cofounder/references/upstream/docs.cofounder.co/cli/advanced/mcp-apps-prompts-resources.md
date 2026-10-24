# MCP Beyond Tools

Source: https://docs.cofounder.co/cli/advanced/mcp-apps-prompts-resources
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** What the hosted MCP server serves besides tools: resources for billing, the Library, outputs, and skills; prompts as slash commands; and the company app's CRM, roadmap, and domains views.

The hosted MCP server at `/mcp` serves the same full catalog to every host,
including Codex, Claude, ChatGPT, and Cursor. Your agent can call tools, read
resources on demand, pick up prompts as slash commands, and open the company
app's CRM, roadmap, and domains views.

Media generation and the `generate-image`/`generate-video` prompts are available
through `/mcp`. All hosts use the same Cofounder account and OAuth resource
identity. When the OAuth proxy is enabled, the upstream Supabase client must
allow `<backend-url>/mcp/oauth/callback`. Connection listing and revocation
cover all account connections.
