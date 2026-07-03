# Cofounder Skills

[![skills.sh](https://skills.sh/b/wazootech/wiki)](https://skills.sh/wazootech/wiki)

A skill library that brings [Cofounder](https://cofounder.co) — the autonomous venture-building engine — to any AI agent, for free, with your model of choice.

This library is a free, open re-implementation of the Cofounder methodology, organized around one master Agent Skill with subcommands:

1. **`cofounder start`** — Idea validation, wedge market, naming, domain
2. **`cofounder plan`** — Spec, problem statement, platform choice, MVP cuts
3. **`cofounder build`** — Repository, CI/CD, backend, frontend, deployment
4. **`cofounder brand`** — Brand story, values, visual identity
5. **`cofounder launch`** — Website, first users, ICP, sales motion, outreach
6. **`cofounder scale`** — Analytics, support, unit economics, expansion

> **Note:** These skills are informational — they guide you through Cofounder-style workflows but do not replace Cofounder's managed execution (Vercel infra, Supabase auth, Stripe billing, PostHog analytics, Fin support, etc.). Where a step says "let Cofounder handle X", that refers to the managed Cofounder platform which requires a paid subscription.


## Onboarding

### Getting Started

Install the library with:

```bash
npx skills add https://github.com/EthanThatOneKid/cofounder-skills
```

Then follow this flow:

1. Start with `cofounder start` to validate the idea, wedge market, name, and domain.
2. Move into `cofounder plan` to turn the idea into a tight MVP spec.
3. Continue through `cofounder build`, `cofounder brand`, `cofounder launch`, and `cofounder scale` as needed.

You can use the master skill one phase at a time or as a full end-to-end sequence.


## Skill Index

| Skill | Scope | Description |
|---|---|---|
| [`cofounder`](/cofounder-skills/cofounder/) | Start → Scale | Master skill with `start`, `plan`, `build`, `brand`, `launch`, and `scale` subcommands |


## What is Cofounder?

[Cofounder](https://cofounder.co) is an autonomous venture-building platform that manages the full lifecycle of a software startup — from a neuro-symbolic "Small Web" idea to a mature, scalable entity. It replaces traditional project management with active execution.

The Cofounder Tech Tree enforces a strict dependency graph: "one right way" to build, where critical path items are hard-locked until prerequisites are met.

This skill library captures the same methodology in plain Agent Skills format — so you can run Cofounder-style workflows with any AI agent, any model, any infrastructure.


## Framework: AI-Driven Startup Execution Engine

### Core Primitives

- **Tech Tree**: A strict dependency roadmap for company progression. Tasks are locked until prerequisites are met.
- **Execution Primitives**:
  - *Agent can do this* — the AI executes technical work (prepare repository, brand identity, build app)
  - *Needs your input* — creative anchors (initial idea, company name)
  - *Approval gate* — user approval before AI proceeds to next node

### Tech Tree Stages

| Stage | Focus | Cofounder Status |
|---|---|---|
| Idea | Concept validation | 100% Complete |
| Initial | Legal & Technical Foundations | 66% (Pending LLC) |
| Identity | Branding & Positioning | In-Progress |
| Build | Product & Web Engineering | Available |
| GTM | Outreach & Growth | Locked |
| Launch | Market Entry | Locked |
| Scale | Optimization & Sales | Locked |
| Mature | Compliance & Longevity | Locked |


## Tech Tree Node Map

```
Idea
 └─ Initial Legal & Technical Foundations
     ├─ Create repository (agent)
     ├─ Set up DNS / domain (agent)
     └─ Incorporate LLC (human)
 └─ Identity — Branding & Positioning
     ├─ Define story and values (human + agent)
     ├─ Design visual identity (agent)
     └─ Set up brand assets (agent)
 └─ Build — Product & Web Engineering
     ├─ Come up with spec (cofounder plan)
     ├─ Scaffold backend (agent)
     ├─ Scaffold frontend (agent)
     ├─ Set up CI/CD (agent)
     └─ Deploy to production (agent)
 └─ Sell — Outreach & Growth
     ├─ Define ICP (human + agent)
     ├─ Build website (agent)
     ├─ First user research (human)
     └─ Run sales motion (human + agent)
 └─ Scale — Optimization & Sales
     ├─ Add product analytics (agent)
     ├─ Add customer support (agent)
     └─ Understand unit economics (human + agent)
 └─ Launch — Market Entry
     └─ (human approval gate)
 └─ Mature — Compliance & Longevity
     └─ (human approval gate)
```


## Case Study: Wazoo Technologies

Framework applied end-to-end via the Tech Tree. See [`references/case-study-wazoo.md`](references/case-study-wazoo.md) for the full Wazoo execution log.

## Upstream Cofounder references

This repository keeps raw upstream Cofounder markdown under `references/upstream/`.

Nightly GitHub Actions scrapes:

- `https://docs.cofounder.co/llms-full.txt`
- `https://cofounder.co/llms.txt`
- Available markdown pages linked from the Cofounder site map

The scrape opens a pull request only when tracked generated content changes. Skill files are not rewritten automatically; upstream changes should be reviewed and synthesized into `Skills/*/SKILL.md` deliberately.


## Skills Reference

Each skill lives in its own directory under `Skills/`:

```
cofounder-skills/
├── README.md
├── Skills/
│   └── cofounder/
│       └── SKILL.md
└── references/
    └── case-study-wazoo.md
```


## Source

- Cofounder product: https://cofounder.co
- How-to guide: https://cofounder.co/how-to
