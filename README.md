# Cofounder Skills

A skill library that brings [Cofounder](https://cofounder.co) — the autonomous venture-building engine — to any AI agent, for free, with your model of choice.

This library is a free, open re-implementation of the Cofounder methodology, broken into itemized Agent Skills that map to the four phases of building a company:

1. **[Start](/cofounder-skills/start/)** — Idea validation, wedge market, naming, domain
2. **[Build](/cofounder-skills/build/)** — Spec, repository, CI/CD, backend, frontend, deployment
3. **[Sell](/cofounder-skills/sell/)** — Brand, website, first user, ICP, sales motion, outreach, marketing
4. **[Scale](/cofounder-skills/scale/)** — Analytics, support, unit economics, expansion

> **Note:** These skills are informational — they guide you through Cofounder-style workflows but do not replace Cofounder's managed execution (Vercel infra, Supabase auth, Stripe billing, PostHog analytics, Fin support, etc.). Where a step says "let Cofounder handle X", that refers to the managed Cofounder platform which requires a paid subscription.

---

## Onboarding

### Getting Started

Install the library with:

```bash
npx skills add https://github.com/EthanThatOneKid/cofounder-skills
```

Then follow this flow:

1. Start with [`cofounder-start`](/cofounder-skills/start/) to validate the idea, wedge market, name, and domain.
2. Move into [`cofounder-plan`](/cofounder-skills/plan/) to turn the idea into a tight MVP spec.
3. Continue through [`cofounder-build`](/cofounder-skills/build/), [`cofounder-brand`](/cofounder-skills/brand/), [`cofounder-launch`](/cofounder-skills/launch/), and [`cofounder-scale`](/cofounder-skills/scale/) as needed.

You can use these skills one at a time or as a full end-to-end sequence.

---

## Skill Index

| Skill | Phase | Description |
|---|---|---|
| [`cofounder-start`](/cofounder-skills/start/) | Start | Evaluate ideas, narrow wedge markets, pick names and domains |
| [`cofounder-plan`](/cofounder-skills/plan/) | Start | Turn an idea into a focused MVP spec |
| [`cofounder-build`](/cofounder-skills/build/) | Build | Scaffold codebase, CI/CD, backend, frontend, deployment pipeline |
| [`cofounder-brand`](/cofounder-skills/brand/) | Sell | Craft brand story, values, and visual identity |
| [`cofounder-launch`](/cofounder-skills/launch/) | Sell | Build website, get first users, run early sales motions |
| [`cofounder-scale`](/cofounder-skills/scale/) | Scale | Add analytics, support, unit economics, and expansion planning |

---

## What is Cofounder?

[Cofounder](https://cofounder.co) is an autonomous venture-building platform that manages the full lifecycle of a software startup — from a neuro-symbolic "Small Web" idea to a mature, scalable entity. It replaces traditional project management with active execution.

The Cofounder Tech Tree enforces a strict dependency graph: "one right way" to build, where critical path items are hard-locked until prerequisites are met.

This skill library captures the same methodology in plain Agent Skills format — so you can run Cofounder-style workflows with any AI agent, any model, any infrastructure.

---

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

---

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
     ├─ Come up with spec (cofounder-plan skill)
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

---

## Case Study: Wazoo Technologies

Framework applied end-to-end via the Tech Tree. See [`references/case-study-wazoo.md`](references/case-study-wazoo.md) for the full Wazoo execution log.

---

## Skills Reference

Each skill lives in its own directory under `Skills/`:

```
cofounder-skills/
├── README.md
├── Skills/
│   ├── cofounder-start/
│   │   └── SKILL.md
│   ├── cofounder-plan/
│   │   └── SKILL.md
│   ├── cofounder-build/
│   │   └── SKILL.md
│   ├── cofounder-brand/
│   │   └── SKILL.md
│   ├── cofounder-launch/
│   │   └── SKILL.md
│   └── cofounder-scale/
│       └── SKILL.md
└── references/
    └── case-study-wazoo.md
```

---

## Source

- Cofounder product: https://cofounder.co
- How-to guide: https://cofounder.co/how-to