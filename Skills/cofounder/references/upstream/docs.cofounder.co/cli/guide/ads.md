# Ads

Source: https://docs.cofounder.co/cli/guide/ads
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Run paid ads: connect or set up an ad account, research keywords, draft and fund campaigns, launch them, and track spend and results.

There are two ways to advertise. Connect an ad account the company already
has (Google, Meta, LinkedIn, TikTok, and others), or use the managed Meta ad
account that company setup creates, which you fund from the company balance.
Setup, drafting, and anything that spends money need a company admin; any
member can read accounts, campaigns, and results.

**What spends money or needs the founder:**

- Spends money: `ads billing fund`, `ads campaigns launch`,
  `ads campaigns resume`, and `ads billing payment retry`.
- Needs the founder: signing in to connect an account, and answering
  business verification requests.

When the company has more than one ad account, choose one with `--resource`
(its name or id), or with `--key` or `--resource-id` on commands that take
those. `cofounder ads accounts list` shows each account's key and id.
