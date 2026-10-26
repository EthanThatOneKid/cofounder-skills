# Pay Cofounder with MPP

Source: https://docs.cofounder.co/cli/advanced/mpp-payments
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Buy company credits from a Machine Payments Protocol wallet, then spend them on Cofounder services like company research.

Your agent can buy prepaid company credits with a
[Machine Payments Protocol (MPP)](https://docs.stripe.com/payments/machine/mpp)
wallet, then spend the company's balance on Cofounder services such as
company research, which returns a saved report with sources.

top-up → wallet pays `payment_url` → credits land → `research start` draws on the balance

Buying credits only adds credits. Research is a separate call that needs
company access.
