# Cards

Source: https://docs.cofounder.co/guide/cards
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Issue single-use or recurring virtual cards, configure auto-approval budgets, and reveal checkout details.

Issue virtual cards so your agent can pay external merchants at checkout or subscribe to online tools with a spend limit and expiration.

| MCP | CLI | API |
| --- | --- | --- |
| `cards_status_get` | `cofounder cards status get` | `GET /cofounder-cli/v1/company/cards/status` |
| `cards_balance_setup_create` | `cofounder cards balance-setup create` | `POST /cofounder-cli/v1/company/cards/balance-setup` |
| `cards_create` | `cofounder cards create` | `POST /cofounder-cli/v1/company/cards` |
| `cards_list` | `cofounder cards list` | `GET /cofounder-cli/v1/company/cards` |
| `cards_get` | `cofounder cards get` | `GET /cofounder-cli/v1/company/cards/{card_id}` |
| `cards_details_get` | `cofounder cards details get` | `GET /cofounder-cli/v1/company/cards/{card_id}/details` |
| `cards_cancel` | `cofounder cards cancel` | `POST /cofounder-cli/v1/company/cards/{card_id}/cancel` |
| `cards_provider_set` | `cofounder cards provider set` | `POST /cofounder-cli/v1/company/cards/provider` |
