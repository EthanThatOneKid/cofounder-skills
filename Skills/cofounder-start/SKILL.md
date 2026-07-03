---
name: cofounder-start
description: Evaluate startup ideas, pick wedge markets, choose company names and domains. Use when the user wants to start a company, validate an idea, pick a niche, or name a startup.
compatibility: Created for any AI agent. No external services required.
metadata:
  author: EthanThatOneKid
  version: "1.0"
---

# Cofounder Start Skill

This skill guides you through the **Idea** and **Initial** phases of the Cofounder Tech Tree — from raw idea to a validated concept with a name, domain, and MVP scope.

## When to Use

- User says they want to start a company
- User has a startup idea and wants to evaluate it
- User needs help narrowing to a wedge market
- User wants to pick a company name or buy a domain
- User is unsure if they should start a company

---

## Step 1: Should You Start?

Evaluate whether this is the right time. A good starting point is if:

- You have seen a painful problem up close
- You understand a customer or industry better than most people
- You have access to a market other founders cannot easily reach
- A new technology makes something newly possible
- You keep returning to the same problem even after ignoring it

**Your task:** Ask the user which of these applies. If none do, help them find a problem space before proceeding.

---

## Step 2: Come Up With Startup Ideas

Startup ideas come from three main sources:

1. **Problems you understand** — from previous work or personal life. The best ideas come with context: you know the customer, their language, what they've tried, and what parts are annoying vs. expensive.
2. **New technology** — AI, cloud infrastructure, new platforms. Map the technology to a real customer pain. "We use AI" is not a startup idea. "We help paralegals review discovery documents in half the time" is.
3. **Specific opportunities (alpha)** — markets you understand unusually well due to your job, family, location, relationships, or reputation.

**Useful question to ask:** *What became newly possible that customers already wanted?*

---

## Step 3: Evaluate the Idea

Evaluate the idea across four lenses:

### Market Size
The market should be big already or small but likely to grow. You need: a reachable customer + a painful problem + a budget. If the market is too small, revenue growth will hit a ceiling.

### Founder/Market Fit
Can you actually understand and serve this market? With software in 2026, probably yes — unless you're trying to start a business in a domain you have no access to.

### Pain
Does the customer already care? Are they using spreadsheets, hiring people, duct-taping tools, paying consultants, or tolerating bad incumbents? Workarounds are evidence of demand.

**Test:** *What does the customer do today because your product does not exist, and would they pay you to fix it?*

### Unique Insight
Do you believe something most market participants haven't realized yet? Without this, you're entering the market the same way everyone else sees it.

---

## Step 4: Pick a Wedge Market

A startup idea is the wedge. The market is the world around it.

A good early market:
- The customer is easy to describe
- The pain is frequent or expensive
- The buyer has budget
- You can reach customers without a giant sales team
- Current alternatives are bad, expensive, slow, or outdated
- The market is changing in a way that creates an opening

**Start narrow.** "Independent dental practices with 3–10 locations that struggle with insurance claim denials" is better than "small businesses."

**Rule:** Pick a market small enough to reach, inside a market big enough to matter.

### Narrowing Exercise

Help the user go from broad to specific:

```
broad market         →  reachable segment       →  first wedge
small businesses     →  independent dental       →  3–10 location practices
                                                 →  fighting claim denials
```

---

## Step 5: Pick a Name and Domain

Rules for a good name:
- Avoid names people cannot spell after hearing once
- Avoid names that lock you into a tiny feature
- Avoid names too similar to existing companies
- Avoid cleverness that only makes sense after an explanation
- Check basic trademark risk before getting attached
- Make sure you can get a reasonable domain and social handles

**Domain:** `.com` is ideal but not required. Alternatives: `.co`, `.app`, `.io`, `.ai`, `.dev`. Do not use other TLDs.

**Note:** Do not spend months negotiating for the perfect domain before talking to customers. Pick a name and move.

**Your task:** Help the user brainstorm names, check domain availability, and verify social handle availability.

---

## Step 6: Come Up With a Spec

Once the idea is validated and named, turn it into a focused MVP spec. Use the `cofounder-plan` skill for this step.

---

## Common Mistakes to Flag

- **Avoiding ideas that seem too hard.** Hard ideas can be good because fewer people attempt them and it's easy to get people and capital to rally around them.
- **Avoiding boring industries.** Many of the best opportunities live in logistics, insurance, construction, compliance, accounting, healthcare administration, legal workflows, manufacturing. Boring problems often make excellent businesses.
- **Being too afraid of competitors.** Competition usually means the problem exists. The question is not "are there competitors?" The question is "why will customers choose us now?"
- **Waiting for the perfect idea.** You will learn more from a month of serious customer conversations and prototyping than from a year of abstract brainstorming.

---

## Cofounder Platform Reference

The Cofounder platform handles this phase by:
- Defining your ICP when you get started
- Buying and configuring your domain (DNS, SSL)
- Providing a step-by-step roadmap from zero to first deployed product

When running this skill independently (without Cofounder), you are the agent executing these steps manually.

## Upstream References

Use the raw upstream notes under `references/upstream/` when updating this skill:
- `references/upstream/cofounder.co/how-to/start.md`
- `references/upstream/docs.cofounder.co/workspace/roadmap.md`
- `references/upstream/docs.cofounder.co/settings/domains.md`

---

## Outputs

At the end of this skill, you should have:
- [ ] Clear problem statement
- [ ] Evaluation across market size, founder/market fit, pain, unique insight
- [ ] Narrowed wedge market
- [ ] Company name
- [ ] Domain acquired or reserved
- [ ] MVP spec started (use `cofounder-plan` skill to complete)
