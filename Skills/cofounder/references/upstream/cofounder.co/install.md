# Install Cofounder for your agent

Source: https://cofounder.co/install.md
Fetched from: https://cofounder.co/install.md

---
name: cofounder-install
description: Install the Cofounder MCP, sign in, and begin onboarding in a supported desktop app. Use when asked to install, connect, or get started with Cofounder; use the connected tools directly for ongoing company work.
---

# Install Cofounder and get started

## First: Confirm the user's setup

Identify the user's app and mode from runtime context when available. Use the table for listed configurations; for an unlisted agent, check its capabilities as described below. For local Codex, start the native plugin connection flow without asking plan or company questions first; the native client checks installation eligibility. For other configurations, ask only for missing details that block the next setup action, one question at a time.

- **Agent can install directly:** The agent can add the MCP connection for the user.
- **Manual setup:** User must add a custom MCP connection manually.
- **Supported setup:** Rows marked true are supported; unlisted agents can also work if they meet the capabilities below.

| Provider | App | Mode | Plan | MCP setup | Code changes | Supported setup |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI | Codex desktop | — | Free, Go, Plus, Pro | Agent can install directly | Use the push token. | true |
| OpenAI | ChatGPT desktop | Codex | All plans | Agent can install directly | Use the push token. | true |
| OpenAI | ChatGPT desktop | Work | All plans | Agent can install directly | Use the push token. | true |
| OpenAI | ChatGPT desktop | Chat | All plans | Manual setup | Code changes not supported. | false |
| OpenAI | ChatGPT website | Chat | Pro | Manual setup | Use the push token. | false |
| OpenAI | ChatGPT website | Chat | Free, Go, Plus | Manual setup | Code changes not supported. | false |
| OpenAI | ChatGPT website | Work | Pro | Manual setup | Use the push token. | false |
| OpenAI | ChatGPT website | Work | Plus | Manual setup | Code changes not supported. | false |
| OpenAI | ChatGPT website | Codex | Pro | Manual setup | Code changes not supported. | false |
| OpenAI | ChatGPT website | Codex | Plus | Manual setup | Code changes not supported. | false |
| OpenAI | ChatGPT mobile | — | All plans | Not supported | Code changes not supported. | false |
| Anthropic | Claude website | Chat | Free | Manual setup | Use the push token. | false |
| Anthropic | Claude website | Chat | Max | Manual setup | Code changes not supported. | false |
| Anthropic | Claude desktop | Code | All plans | Agent can install directly | Use the push token. | true |
| Anthropic | Claude desktop | Chat | All plans | Manual setup | Code changes not supported. | false |
| Anthropic | Claude mobile | Chat | Free | Manual setup | Use the push token. | false |
| Cursor | Cursor desktop | — | All plans | Agent can install directly | Use the push token. | true |
| xAI | Grok Bot desktop | — | All plans | Agent can install directly | Use the push token. | true |

**ChatGPT desktop:** Use **Codex mode or ChatGPT Work mode, never Chat mode**. After sign-in or a restart, continue in a new chat in one of those supported desktop modes.

**Grok Bot desktop:** The Bot runs on a shared cloud computer, not on the founder's laptop. Do not claim access to laptop files or offer local-folder upload from Grok Bot; use a connected GitHub repository or a new repository for company code.

## Other and unsupported setups

For an unlisted agent, reuse its existing Cofounder connection or use its own connection flow to add the remote HTTP MCP server at https://api.cofounder.co/mcp. Continue when it can authenticate and call Cofounder tools. Repository work also requires a shell and filesystem the agent can use; do not claim access the host does not provide. Ask for the specific missing capability only when it blocks the requested work.

If the current host cannot connect to Cofounder or perform a needed coding step, explain the blocker and offer a supported alternative. Install [ChatGPT](https://chatgpt.com/download/), [Claude](https://claude.com/download), [Cursor](https://cursor.com/download), or [Grok Bot](https://cursor.com/download/bot), then use Codex or Work mode in ChatGPT, Code mode in Claude, Cursor, or Grok Bot desktop.

If they switch, have them paste "Please follow https://app.cofounder.co/install.md to connect Cofounder and help me get started" in the selected desktop app, then wait for them to continue.


## Connect

Reuse an existing Cofounder connection or plugin for https://api.cofounder.co/mcp. If `user_get` succeeds, skip installation. If the existing connection needs sign-in, authenticate it instead of adding another connection.

In Claude chat (web or Desktop) or Cowork, use an existing Cofounder connector. If Claude offers a **Connect** card, ask the founder to select it and complete sign-in. Check the user's connectors, including custom connectors, even when Cofounder tools have not loaded.

When a connection is needed, welcome the founder in one short sentence and give them only the next action: select **Connect** and sign in, then return here. The same sign-in page creates an account for new users; mention this only when relevant. Sign-in may open a browser. Wait for the founder, then call `user_get` to verify the account and resume with `onboarding_get`. If the tools remain unavailable after sign-in, ask them to enable Cofounder or start a new chat. Do not assume a missing tool means a particular connection state or ask for a new chat before checking.

If no card appears, check whether the user's connectors already include Cofounder at https://api.cofounder.co/mcp. If the Cofounder plugin is installed, ask the founder to open **Customize → Plugins → Cofounder → Connectors** and select **Connect**. For an existing custom connector, use **Customize → Connectors** instead. They may need to continue in their browser and approve access before returning to Claude. If the connector is already connected, enable it in the chat and retry loading its tools. Start a new chat if the tools remain unavailable.

If no existing connection is registered, offer [Add Cofounder to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Cofounder&connectorUrl=https%3A%2F%2Fapi.cofounder.co%2Fmcp). This opens a prefilled custom connector form on Claude web. The user confirms it, chooses **Sign in now**, and completes the connection. If the link opens without the form, have them sign in to Claude and open it again. Alternatively, add a custom connector with https://api.cofounder.co/mcp. If workspace policy prevents adding it, ask an owner to add it. Mobile users can complete connector setup on the web or Desktop with the same Claude account. Keep consent in Claude's connection flow; do not create a duplicate connection or send these users to a terminal.

If there is no existing connection:

For Codex running locally on the user's computer, install the official Cofounder plugin from the public Git marketplace. This also applies to Codex mode in the desktop app; it does not apply to a remote shell or ChatGPT Work mode.

Keep the first setup turn focused on opening the native plugin page. Explain only the next user action, not the installation machinery. Use available Cofounder tools to recognize an existing connection. If you need the CLI's plugin status, scope it to `codex plugin list --marketplace cofounder --available --json`; stale unrelated marketplaces must not block this setup. Do not inspect the native UI to verify installation.

Import the marketplace using the local Codex CLI:

```sh
codex plugin marketplace add General-Intelligence-Company/cofounder-plugin --json
```

If the command reports that `cofounder` is already added from a different source, inspect the scoped plugin list above. If its `marketplaceSource` is the official Cofounder Git repository, retry marketplace add with that exact source to get its `installedRoot`; otherwise explain the conflict instead of replacing it. If the response says `alreadyAdded: true`, refresh only Cofounder's catalog with `codex plugin marketplace upgrade cofounder --json`. Use the marketplace-add response's `installedRoot` to locate `.agents/plugins/marketplace.json`. Build a link on this computer: `codex://plugins/cofounder?marketplacePath=<URL-encoded absolute marketplace.json path>`. Open it through the local OS URL handler; if opening is unavailable, give the user the clickable link. The native page owns **Install**, authentication, and **Set up for Cofounder**. Do not install the plugin through the CLI first. Keep the plugin's existing `cofounder:get-started` action as the setup entry. Once the page is open, say: “Install Cofounder, connect your account, then choose Set up for Cofounder on this page.” Stop that bootstrap turn there; the native setup action continues onboarding. Ask company and repository questions after connection succeeds.

If the local CLI is unavailable or cannot write its settings, use Codex's **Plugins → Add → Add a marketplace**, enter `General-Intelligence-Company/cofounder-plugin`, and install Cofounder. Do not guess a cache path or run the commands on a different computer. Do not add a second raw MCP connection alongside the plugin.

For Claude Code running locally on the user's computer, reuse a working Cofounder plugin or MCP connection for https://api.cofounder.co/mcp. Check `claude mcp list` and `claude plugin list --json` when needed. A plugin pointing at a different endpoint may be an older install; do not treat its presence as a working connection. If the existing plugin fails, explain its status and help the founder update or disable it before adding another connection. Otherwise add the public marketplace and install the plugin:

```sh
claude plugin marketplace add General-Intelligence-Company/cofounder-plugin
claude plugin install cofounder@cofounder --scope user
```

The plugin provides its own MCP server; do not add a duplicate. Open `/mcp`, select the Cofounder server, and ask the founder to sign in in the browser. If the installed plugin or its server does not appear, reload plugins or start a new Claude Code session. Before the browser handoff, tell the founder: “After signing in, return to this conversation and send Continue.” For Claude Code cloud sessions, use the host's existing connector flow instead of changing the local computer.

For the other supported desktop configurations, install the https://api.cofounder.co/mcp MCP through the host's connection flow.

Preserve other MCP servers. If Cofounder tools are missing, check whether the connection needs to be added or enabled before requesting sign-in. When sign-in is required, have the user complete the client's OAuth sign-in and consent. New users create their account on the same sign-in page.

After sign-in, refresh or re-enable the connection. If tools are still missing, start a new chat in the supported app and mode. Retry once; if still blocked, tell the user exactly what to do next and stop.

Call `user_get` and verify it returns the user's ID and email. If an expected email was provided, confirm it matches. Continue to onboarding only after this succeeds.

## Onboard

Call `onboarding_get` and follow the [onboarding skill](https://app.cofounder.co/mcp-onboarding/skill.md).

If the connection or guide is unavailable, report the blocker.
