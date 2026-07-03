---
name: cofounder
description: Master Cofounder workflow skill with subcommands for start, plan, build, brand, launch, and scale. Use when the user wants the full venture-building flow or a specific phase in one place.
compatibility: Created for any AI agent. No external services required.
metadata:
  author: EthanThatOneKid
  version: "1.0"
---

# Cofounder

Use this skill as the single entry point for the Cofounder workflow.

Subcommand shape:

- `cofounder start` — validate the idea, wedge market, name, and domain
- `cofounder plan` — turn the idea into a tight MVP spec
- `cofounder build` — scaffold the product and production path
- `cofounder brand` — define story, values, and visual identity
- `cofounder launch` — build the website, get first users, and run outreach
- `cofounder scale` — add analytics, support, unit economics, and expansion planning

## Routing rule

When the user gives a broad Cofounder request, route it to the right subcommand instead of splitting the workflow across separate skills.

When the user gives a multi-phase request, keep the phases in order:
`start` → `plan` → `build` → `brand` → `launch` → `scale`.

## Shared principles

- Start narrow and keep the wedge specific.
- Cut scope aggressively before building.
- Prefer web-first builds unless there is a strong reason not to.
- Keep brand, launch, and scale tied to real user feedback.
- Preserve upstream references, but treat them as raw source material rather than auto-generated instruction.

## `cofounder start`

Use this when the user wants to start a company, validate an idea, narrow a wedge, or choose a name and domain.

Focus on:

- Whether the founder has direct pain, access, or unique insight
- Market size, pain, and founder-market fit
- Picking a narrow wedge the user can actually reach
- Choosing a name that is spellable, flexible, and available

Output:

- Problem statement
- Evaluation of the idea
- Narrowed wedge market
- Company name
- Domain plan
- Handoff to `cofounder plan`

## `cofounder plan`

Use this when the user has a validated idea and needs a focused MVP spec.

Focus on:

- One tight problem statement
- The target user
- The platform choice, usually web
- The minimum feature set, usually three to five core features
- Out-of-scope items
- Success criteria

Output:

- MVP spec
- Explicit cuts
- Handoff to `cofounder build`

## `cofounder build`

Use this when the user is ready to turn the spec into a production-ready product.

Focus on:

- Repository setup and branch safety
- Deployment before heavy coding
- Backend, auth, and data model decisions
- Frontend implementation
- Tests, linting, and debugging

Output:

- Running codebase
- Deployment path
- Test and quality checklist

## `cofounder brand`

Use this when the user needs positioning, identity, or visual direction.

Focus on:

- The story of why the company exists
- Values that actually show up in the product
- A usable visual identity
- Documenting the result in a design guide

Output:

- Brand story
- Values
- Visual identity notes
- `DESIGN.md`

## `cofounder launch`

Use this when the user has a live product and needs users, a website, ICP, or a sales motion.

Focus on:

- A homepage that explains the product fast
- The first user conversations
- A specific ICP
- The right sales motion
- Outreach and marketing that match the market

Output:

- Website copy and structure
- ICP definition
- Sales motion
- Outreach plan

## `cofounder scale`

Use this when the product has real users and needs growth systems.

Focus on:

- Product analytics
- Founder-led then AI-assisted support
- Unit economics
- Expansion planning

Output:

- Analytics plan
- Support plan
- Unit economics summary
- Expansion recommendations

## Upstream references

Use the raw upstream notes under `references/upstream/` as source material for the relevant subcommand.

- `references/upstream/cofounder.co/how-to/start.md`
- `references/upstream/cofounder.co/how-to/build.md`
- `references/upstream/cofounder.co/how-to/sell.md`
- `references/upstream/cofounder.co/how-to/scale.md`
- `references/upstream/docs.cofounder.co/workspace/roadmap.md`
- `references/upstream/docs.cofounder.co/workspace/marketing-department.md`
- `references/upstream/docs.cofounder.co/agents/design-agent.md`
- `references/upstream/docs.cofounder.co/agents/marketing-agent.md`
- `references/upstream/docs.cofounder.co/agents/sales-agent.md`
- `references/upstream/docs.cofounder.co/workspace/tasks.md`
