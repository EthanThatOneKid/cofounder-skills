# Install Cofounder for your agent

Source: https://cofounder.co/install.md
Fetched from: https://cofounder.co/install.md

---
name: cofounder-install
description: Connect your agent to the hosted Cofounder MCP server, sign the user in, and verify the connection with user_get. Use when asked to install, set up, or connect Cofounder. After sign-in it hands off to the onboarding_get tool, which owns everything after.
compatibility: needs an agent client that supports remote MCP over HTTP with OAuth
---

# Set up Cofounder

Cofounder supplies company context, resources, and capabilities to your own agent. This guide connects your client to Cofounder (https://app.cofounder.co) and signs the user in.

## Rules

- Follow the steps yourself. Ask the user only for sign-in and consent.
- Reuse an existing Cofounder connection if one exists.
- Never report success before step 4 passes.
- Never paste or print tokens.
- Do not switch accounts to work around errors.
- Installing Cofounder does not authorize anything else.

## Step 1: Identify your client

Decide from the runtime you are running in, not from the model name. If unclear, ask the user. Windows users use the plugin or MCP; the CLI needs WSL.

## Step 2: Connect

If Cofounder tools are already listed, skip to step 4. Otherwise use the block for your client.

**Claude (claude.ai web, Claude Desktop chat, mobile).** Give the user this link:
https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Cofounder&connectorUrl=https%3A%2F%2Fapi.cofounder.co%2Fmcp
The user confirms the prefilled dialog, then clicks Connect to sign in. By hand: Customize, Connectors, +, Add custom connector. Then enable it in a chat from "+", Connectors.
- Free plans allow one custom connector.
- On Team and Enterprise only Owners can add connectors, using https://claude.ai/admin-settings/connectors?modal=add-custom-connector&connectorName=Cofounder&connectorUrl=https%3A%2F%2Fapi.cofounder.co%2Fmcp. Members then connect individually.
- Open the link in a browser signed in to claude.ai; the connector then appears in Desktop and mobile too.

**Claude Code.** Plugin:
`claude plugin marketplace add General-Intelligence-Company/cofounder-plugin` then `claude plugin install cofounder@cofounder --scope user`
(on Claude Code 2.1.292+, `claude plugin install cofounder --marketplace General-Intelligence-Company/cofounder-plugin` also works).
Without the plugin: `claude mcp add --transport http cofounder https://api.cofounder.co/mcp --scope user`.
Sign in with `/mcp`, cofounder, authenticate, or run `claude mcp login cofounder`. `claude -p` cannot do OAuth.

**Codex (app, CLI, and IDE share one config).**
- App: Plugins, Add, Add a marketplace, General-Intelligence-Company/cofounder-plugin, Install, Authenticate.
- CLI: `codex plugin marketplace add General-Intelligence-Company/cofounder-plugin` then `codex plugin add cofounder@cofounder`.
- Manual: `codex mcp add cofounder --url https://api.cofounder.co/mcp` then `codex mcp login cofounder` (use the name shown by `codex mcp list`). The user runs login in their own terminal (PowerShell on Windows); you cannot complete it.
- The Windows sandbox cannot write `~/.codex`, so use the Plugins UI or the user's own PowerShell.

**ChatGPT.**
- Desktop app, Work chat: add the server yourself through the host's MCP installation support (URL `https://api.cofounder.co/mcp`, authentication OAuth), then continue in a new Work chat. In a Chat-mode chat, ask the user to switch to Work or use the website steps.
- Website: send the user to https://app.cofounder.co/os/setup/chatgpt, an illustrated guide. By hand: https://chatgpt.com/plugins, Add, Add custom MCP server, name Cofounder, Server URL `https://api.cofounder.co/mcp`, authentication OAuth, Create as a plugin. Work mode needs Plus or Pro; Free and Go plans use Chat mode, where code changes are not supported. Availability also depends on workspace policy.
- Mobile: not supported; set up on the desktop app or website first.

**Cursor.** Open `cursor://anysphere.cursor-deeplink/mcp/install?name=cofounder&config=eyJ1cmwiOiJodHRwczovL2FwaS5jb2ZvdW5kZXIuY28vbWNwIn0=`, or put `{"mcpServers":{"cofounder":{"url":"https://api.cofounder.co/mcp"}}}` in `~/.cursor/mcp.json`.

**VS Code.** Open `vscode:mcp/install?%7B%22name%22%3A%22cofounder%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapi.cofounder.co%2Fmcp%22%7D`, or add the server to `.vscode/mcp.json` under the top-level `servers` key as `{"type":"http","url":"https://api.cofounder.co/mcp"}`.

**Goose.** Open `goose://extension?url=https%3A%2F%2Fapi.cofounder.co%2Fmcp&type=streamable_http&id=cofounder&name=Cofounder`.

**Other clients.** Add a remote Streamable HTTP server with OAuth at https://api.cofounder.co/mcp. Protected-resource metadata is at https://api.cofounder.co/.well-known/oauth-protected-resource/mcp.

**Config writes.** If you must write config, merge into the existing file (keep other servers) and read it back.

## Step 3: Sign in

New users create their account on the same sign-in page. After sign-in, if the tools do not appear, start a NEW chat (Claude: enable the connector in that chat; Claude Code: `/mcp` or `/reload-plugins`; Codex: new local chat, not cloud; ChatGPT: rescan tools). Retry once, then tell the user exactly what to click instead of editing configs repeatedly.

## Step 4: Verify

Call `user_get`. This step passes only when it returns the user's id and email.

## Step 5: Hand off

Call `onboarding_get` and follow its next step. It works for new users, existing companies, and companies created in the web app.

## Optional: CLI for terminal-only agents

`npm install --global @generalintelligence/cofounder@latest`, then `cofounder auth login`, then `cofounder onboarding` (Node 22 or 24; macOS, Linux, or WSL).
