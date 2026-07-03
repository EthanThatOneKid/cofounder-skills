---
name: cofounder-scale
description: Add product analytics (PostHog), AI support (Fin), understand unit economics, and plan expansion. Use when a product has real users and needs to grow sustainably.
compatibility: Requires PostHog account for analytics. Requires Fin/Intercom for support automation.
metadata:
  author: EthanThatOneKid
  version: "1.0"
---

# Cofounder Scale Skill

This skill guides you through the **Scale** phase of the Cofounder Tech Tree — turning a working product into a sustainable business using data, support systems, and unit economics.

## When to Use

- User has paying customers and wants to understand business health
- User needs product analytics set up
- User wants to add customer support systems
- User is asking about unit economics (LTV, CAC, churn)
- User is planning to expand the product or market

---

## Phase 1: The Scaling Loop

A startup is not a static product. It is a loop:

```
Build → Sell → Observe → Support → Learn → Iterate → (repeat)
```

Early on, you can run this loop manually — talk to every user, fix bugs in real time. Eventually, you need systems.

**Your task:** Help the user identify which parts of the loop are still manual and which need systems.

---

## Phase 2: Add Product Analytics

You cannot iterate well if you do not know what is broken.

### Recommended: PostHog

PostHog provides: funnels, custom events, session replay, and retention analysis.

### Set Up PostHog

1. Create a PostHog project
2. Add the library to your app
3. Include the project key and host in environment variables
4. Identify users after they log in

### What to Measure

Track outcomes, not just page views. Start with these key events:

```javascript
signed_up
onboarding_completed
core_action_completed
trial_started
checkout_completed
subscription_upgraded
teammate_invited
support_ticket_opened
```

**Rules:**
- Use clear event names
- Keep staging and production data separate
- Do NOT track: passwords, payment details, private documents, API keys

### The Four Analytics Views

1. **Funnels** — Where do users drop off? If 1,000 sign up and only 150 create a first project, the problem is activation, not traffic.

2. **Custom events** — Meaningful actions you decide to track. Track outcomes: project created, report generated, invoice sent.

3. **Session replay** — Recordings of how users move through the app. Analytics tells you *where* something broke. Replay often shows you *why*.

4. **Retention** — Do users keep coming back? The question is not "do users come back every day?" It's "do users come back at the natural frequency of the problem we solve?"

### The Analytics Loop

```
Find a drop-off or unusual pattern
  → Watch replays for that segment
    → Talk to a few affected users
      → Form a hypothesis
        → Ship a small change
          → Measure whether the metric improves
```

---

## Phase 3: Add Customer Support

The users you fought to win have given you something valuable: trust. That trust has a limit.

### Early Support: Founder-Led

Watch your first customers use the product. Ask what they expected. Fix bugs in real time. Listen to the words they use to describe problems. This teaches you what the product feels like from the customer's side.

### Scale Support: AI Agent

Recommended: **Fin by Intercom** — an AI support agent that answers inbound questions using your documentation, product context, and support procedures, then escalates issues it cannot resolve.

**What Fin handles well:**
- Password resets
- Billing updates
- Teammate invites
- Import failures
- Plan changes
- Basic troubleshooting

**What should escalate to humans:**
- Refund disputes
- Security concerns
- Data loss
- Angry enterprise customers
- Bugs affecting many users

### Build a Knowledge Base

A knowledge base is the set of help articles, troubleshooting steps, and policies your support system uses.

**Start with:**
- Getting started
- Core workflows
- Billing and plans
- Troubleshooting
- Account management
- Known limitations

**Rule:** Write docs in the language customers use — not the language your codebase uses.

### Use Decision Trees

A support decision tree is a structured path for handling a category of issue.

**Start with the most common and painful categories:**
- Login problems
- Billing questions
- Import failures
- Permission issues
- Core workflow errors
- Cancellations
- Bugs that block users from getting value

---

## Phase 4: Understand Unit Economics

Revenue tells you how much money is coming in. Profit tells you how much you keep. Both matter.

To understand whether the business can scale, you need to look at the economics of a **single customer.**

### Core Metrics

**Churn** — The rate at which customers leave.
```
Revenue churn rate = lost recurring revenue during period / 
                     recurring revenue at start of period
```

**Average Customer Lifetime**
```
Average customer lifetime = 1 / churn rate
```
(If monthly churn is 20%, average lifetime is ~5 months)

**ARPU** — Average revenue per user/customer.
```
ARPU = total revenue / number of customers
```

**LTV** — Lifetime value.
```
LTV = ARPU × average customer lifetime
Gross margin LTV = ARPU × gross margin × average customer lifetime
```

**CAC** — Customer acquisition cost.
```
CAC = sales and marketing cost during period / 
      new customers acquired during period
```

**LTV/CAC** — Health ratio.
```
LTV/CAC = lifetime value / customer acquisition cost
```
If LTV < CAC, something is broken. Increase retention, raise pricing, improve margins, lower CAC, or revisit your ICP.

**Payback Period** — How long to earn back acquisition cost.
```
Payback = CAC / (ARPU × gross margin)
```

### What to Watch

- Is churn going up or down?
- Are customers staying longer?
- Are customers paying more over time?
- Is acquisition getting cheaper or more expensive?

**Do not obsess over precision early.** With small datasets, numbers are noisy. The point is direction.

---

## Phase 5: Expand the Business

Once the core product works, support is manageable, and your economics are improving — the next question is how to expand the ceiling.

### Two Expansion Paths

**Vertical expansion** — Serve existing customers more deeply. Add products, services, workflows, or infrastructure that make your product more central. Works best when customers already trust you, the adjacent pain is obvious, and the new product increases retention or ARPU.

**Horizontal expansion** — Serve a broader set of customers. Take what you built and adapt it to adjacent segments, use cases, or markets. Works best when the core technology applies to multiple customer types.

### Questions to Ask Before Expanding

1. **Where is demand already showing up?** — Inbound requests, support tickets, sales conversations that point to the same adjacent thing.

2. **Does this improve retention, ARPU, CAC, or payback?** — Expansion should improve unit economics, not just grow revenue.

3. **Will it strengthen the core product or distract from it?** — The best expansions make the core product better. The worst ones split engineering focus.

4. **Can we test demand before building?** — Sell the expansion before you build it. Get a verbal commit or letter of intent.

5. **Does it meaningfully increase TAM?** — The total addressable market opportunity.

### Cofounder Platform Reference

The Cofounder platform can analyze expansion opportunities by combining product usage, customer feedback, support themes, and revenue data — identifying which segments are retaining, which features drive expansion, and which roadmap bets are most likely to increase the ceiling.

When running this skill independently, you are executing the analysis and expansion planning manually.

## Upstream References

Use the raw upstream notes under `references/upstream/` when updating this skill:
- `references/upstream/cofounder.co/how-to/scale.md`
- `references/upstream/docs.cofounder.co/settings/company-context.md`
- `references/upstream/docs.cofounder.co/settings/env-files-and-secrets.md`
- `references/upstream/docs.cofounder.co/workspace/tasks.md`

---

## Outputs

At the end of this skill, you should have:
- [ ] PostHog (or equivalent) installed and tracking key events
- [ ] Funnels set up for core flows
- [ ] Session replay enabled for debugging
- [ ] Support knowledge base written
- [ ] Decision trees for common support categories
- [ ] Fin (or equivalent) configured for automated support
- [ ] Unit economics dashboard (churn, LTV, CAC, LTV/CAC, payback)
- [ ] Expansion opportunity identified (vertical or horizontal)
- [ ] Expansion hypothesis tested (verbal commit or letter of intent)
