# Pay Cofounder with MPP

Source: https://docs.cofounder.co/cli/advanced/mpp-payments
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Buy company credits through Machine Payments Protocol, then use them for Cofounder services such as company research.

Cofounder accepts [Machine Payments Protocol (MPP)](https://docs.stripe.com/payments/machine/mpp)
payments for prepaid company credits. An agent buys credits, then spends the
company's balance on Cofounder services. Company research is one example: the
agent starts a research job and receives a saved report with sources.

The payment endpoint delivers a credit purchase receipt. Research is a separate,
authenticated operation; paying for credits does not start a research job.
