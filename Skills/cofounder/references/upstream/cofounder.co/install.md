# Install Cofounder for your agent

Source: https://cofounder.co/install.md
Fetched from: https://cofounder.co/install.md

---
name: cofounder-install
description: Install the Cofounder MCP, sign in, and begin onboarding in a supported desktop app. Use when asked to install, connect, or get started with Cofounder; use the connected tools directly for ongoing company work.
---

# Install Cofounder and get started

## First: Confirm the user's setup

Identify the user's app and mode from runtime context when available. Verify that the configuration is supported in the table. For local Codex, start the native plugin connection flow without asking plan or company questions first; the native client checks installation eligibility. For other configurations, ask only for missing details that block the next setup action, one question at a time.

- **Agent can install directly:** The agent can add the MCP connection for the user.
- **Manual setup:** User must add a custom MCP connection manually.
- **Supported setup:** Use a row marked true.

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

## Unsupported setup

For an unsupported or unlisted setup, guide the user to one of the supported desktop configurations above. Install [ChatGPT](https://chatgpt.com/download/), [Claude](https://claude.com/download), [Cursor](https://cursor.com/download), or [Grok Bot](https://cursor.com/download/bot), then use Codex or Work mode in ChatGPT, Code mode in Claude, Cursor, or Grok Bot desktop.

Have them paste "Please follow https://app.cofounder.co/install.md to install the Cofounder MCP and onboard me" in the selected desktop app, then wait for them to continue.


## Connect

Reuse an existing Cofounder connection or plugin for https://api.cofounder.co/mcp. If `user_get` succeeds, skip installation. If the existing connection needs sign-in, authenticate it instead of adding another connection.

In Claude chat (web or Desktop) or Cowork, prefer the host's native inline **Connect** card or sign-in prompt. Use the host's available connector-management tools to find the existing Cofounder connector and offer its connect card, even if its MCP tools have not loaded. Check the user's connectors, not only the public directory: a custom connector can have an inline card without a directory listing. If `user_get` is available, call it once to check identity and request authentication.

When a connection is needed, welcome the founder briefly if you haven't already and give them one next action. When the card is shown, ask them to select **Connect** and sign in, and invite them to return to this chat when finished; the same sign-in page creates an account for new users. Keep connection details and tool names in the background. Wait for the founder; then call `user_get` to verify the account and resume with `onboarding_get`. If the tools remain unavailable after sign-in, ask them to enable Cofounder or start a new chat. Do not assume a missing tool means a particular connection state or ask for a new chat before checking.

If no native prompt is available, check whether the user's connectors already include Cofounder at https://api.cofounder.co/mcp. An installed plugin can have a bundled connector that is **Not added**; missing tools alone do not prove it is signed out. If you cannot check, ask the founder to look for Cofounder in their connectors before adding it. If the connection is already added, enable it in the chat and retry loading its tools; use its existing sign-in or reconnect action only if the inline prompt does not appear. Start a new chat if the tools remain unavailable.

If no existing connection is registered, offer [Add Cofounder to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Cofounder&connectorUrl=https%3A%2F%2Fapi.cofounder.co%2Fmcp). This opens a prefilled custom connector form on Claude web. The user confirms it, chooses **Sign in when needed**, then returns to chat for the native connect card. If the link opens without the form, have them sign in to Claude and open it again. Alternatively, find Cofounder under **Plugins** (or **Customize**) and connect its bundled connector, or add a custom connector with https://api.cofounder.co/mcp. If workspace policy prevents adding it, ask an owner to add it. Mobile users can complete connector setup on the web or Desktop with the same Claude account. Keep consent in Claude's connection flow; do not create a duplicate connection or send these users to a terminal.

If there is no existing connection:

For Codex running locally on the user's computer, install the official Cofounder plugin from the public Git marketplace. This also applies to Codex mode in the desktop app; it does not apply to a remote shell or ChatGPT Work mode.

Keep the first setup turn focused on opening the native plugin page. Use available Cofounder tools to recognize an existing connection. If you need the CLI's plugin status, scope it to `codex plugin list --marketplace cofounder --available --json`; stale unrelated marketplaces must not block this setup. Do not inspect the native UI to verify installation.

Import the marketplace using the local Codex CLI:

```sh
codex plugin marketplace add General-Intelligence-Company/cofounder-plugin --json
```

If the response says `alreadyAdded: true`, refresh only Cofounder's catalog with `codex plugin marketplace upgrade cofounder --json`. Use the marketplace-add response's `installedRoot` to locate `.agents/plugins/marketplace.json`. Build a link on this computer: `codex://plugins/cofounder?marketplacePath=<URL-encoded absolute marketplace.json path>`. Open it through the local OS URL handler; if opening is unavailable, give the user the clickable link. The native page owns **Install**, authentication, and **Set up for Cofounder**. Do not install the plugin through the CLI first. Keep the plugin's existing `cofounder:get-started` action as the setup entry. Ask company and repository questions after connection succeeds.

If the local CLI is unavailable or cannot write its settings, use Codex's **Plugins → Add → Add a marketplace**, enter `General-Intelligence-Company/cofounder-plugin`, and install Cofounder. Do not guess a cache path or run the commands on a different computer. Do not add a second raw MCP connection alongside the plugin.

For the other supported desktop configurations, install the https://api.cofounder.co/mcp MCP through the host's connection flow.

Preserve other MCP servers. If Cofounder tools are missing, check whether the connection needs to be added or enabled before requesting sign-in. When sign-in is required, have the user complete the client's OAuth sign-in and consent. New users create their account on the same sign-in page.

After sign-in, refresh or re-enable the connection. If tools are still missing, start a new chat in the supported app and mode. Retry once; if still blocked, tell the user exactly what to do next and stop.

Call `user_get` and verify it returns the user's ID and email. If an expected email was provided, confirm it matches. Continue to onboarding only after this succeeds.

## Onboard

Call `onboarding_get` and follow the [onboarding skill](https://app.cofounder.co/mcp-onboarding/skill.md).

Before new-company setup, ask whether the user wants an existing GitHub repository, a local-folder upload, or a new repository. Ask one question at a time and wait for each answer. For an existing company, resume its repository and completed setup.

If the connection or guide is unavailable, report the blocker.
