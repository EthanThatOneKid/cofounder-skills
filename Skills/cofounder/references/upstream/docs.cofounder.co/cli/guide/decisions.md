# Decisions

Source: https://docs.cofounder.co/cli/guide/decisions
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Ask a company member to decide what your agent should not decide alone, with the context they need, and read their answer.

Some calls belong to a person: shipping a pricing change, picking a launch
date, approving copy. A decision asks a company member, with the context they
need to answer quickly, and records their answer for your agent.

| MCP | CLI | API |
| --- | --- | --- |
| `decisions_create` | `cofounder decisions create --title <text> --response-type confirm` | `POST /cofounder-cli/v1/decisions` |
| `decisions_list` | `cofounder decisions list --status pending` | `GET /cofounder-cli/v1/decisions` |
| `decisions_get` | `cofounder decisions get --decision-id <id>` | `GET /cofounder-cli/v1/decisions/{decision_id}` |
| `decisions_submit` | `cofounder decisions submit --decision-id <id> --response-type confirm --approved` | `POST /cofounder-cli/v1/decisions/{decision_id}/answer` |
| `decisions_cancel` | `cofounder decisions cancel --decision-id <id>` | `POST /cofounder-cli/v1/decisions/{decision_id}/cancel` |
