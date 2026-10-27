# Wallet

Source: https://docs.cofounder.co/guide/wallet
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Connect a company wallet, send payments, and collect money.

Connect a payment wallet so your agent can pay vendors and collect money for your company.
Wallet tools are not available to every company yet. Wallet funds are separate from Cofounder usage credits.

| MCP | CLI | API |
| --- | --- | --- |
| `wallet_connect` | `cofounder wallet connect` | `POST /cofounder-cli/v1/company/wallet/connect` |
| `wallet_apps_setup` | `cofounder wallet apps setup` | `POST /cofounder-cli/v1/company/wallet/apps/setup` |
| `wallet_get` | `cofounder wallet get` | `GET /cofounder-cli/v1/company/wallet` |
| `wallet_payments_create` | `cofounder wallet payments create` | `POST /cofounder-cli/v1/company/wallet/payments` |
| `wallet_payment_requests_create` | `cofounder wallet payment-requests create` | `POST /cofounder-cli/v1/company/wallet/payment-requests` |
| `wallet_operations_get` | `cofounder wallet operations get` | `GET /cofounder-cli/v1/company/wallet/operations/{operation_id}` |
| `wallet_transactions_list` | `cofounder wallet transactions list` | `GET /cofounder-cli/v1/company/wallet/transactions` |
