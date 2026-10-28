# Install Cofounder for your agent

Source: https://cofounder.co/install.md
Fetched from: https://cofounder.co/install.md

---
name: cofounder-install
description: Install the Cofounder MCP, sign in, and begin onboarding in a supported desktop app or Grokbot. Use when asked to install, connect, or get started with Cofounder; use the connected tools directly for ongoing company work.
---

# Install Cofounder and get started

## First: Confirm the user's setup

Verify that the user's app, mode, and plan match a supported configuration in the table. If not, guide them to one. Ask for missing details one question at a time.

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
| Anthropic | Claude desktop | Chat | All plans | Manual setup | Code changes not supported. | true |
| Anthropic | Claude mobile | Chat | Free | Manual setup | Use the push token. | false |
| xAI | Grokbot | — | All plans | Agent can install directly | Use the push token. | true |

**ChatGPT desktop:** Use **Codex mode or ChatGPT Work mode, never Chat mode**. After sign-in or a restart, continue in a new chat in one of those supported desktop modes.

## Unsupported setup

For an unsupported or unlisted setup, guide the user through downloading and installing the appropriate desktop app: [ChatGPT desktop](https://chatgpt.com/download/) or [Claude desktop](https://claude.com/product/claude-code). Use Code mode in Claude.

Have them paste "Please follow https://app.cofounder.co/install.md to install the Cofounder MCP and onboard me" there, then wait for them to continue.


## Connect

Reuse an existing Cofounder connection. Otherwise:

Install the https://api.cofounder.co/mcp MCP.

Preserve other MCP servers. Call `onboarding_get`. If sign-in is required or Cofounder tools are missing, have the user complete the client's OAuth sign-in and consent. New users create their account on the same sign-in page.

After sign-in, refresh or re-enable the connection. If tools are still missing, start a new chat in the supported app and mode. Retry once; if still blocked, tell the user exactly what to do next and stop.

Call `user_get` and verify it returns the user's ID and email. If an expected email was provided, confirm it matches. Continue to onboarding only after this succeeds.

## Onboard

Call `onboarding_get` and follow the [onboarding skill](https://app.cofounder.co/mcp-onboarding/skill.md).

Before new-company setup, ask whether the user wants an existing GitHub repository, a local-folder upload, or a new repository. Ask one question at a time and wait for each answer. For an existing company, resume its repository and completed setup.

If the connection or guide is unavailable, report the blocker.
