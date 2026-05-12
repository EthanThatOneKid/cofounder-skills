---
name: cofounder-plan
description: Turn a validated startup idea into a focused MVP spec — core problem, essential features, and platform decision. Use when defining what to build.
compatibility: Created for any AI agent. No external services required.
metadata:
  author: EthanThatOneKid
  version: "1.0"
---

# Cofounder Plan Skill

This skill turns a validated startup idea into a focused **Minimum Viable Product (MVP) spec** — the smallest version of your product that delivers real value to a real user.

## When to Use

- User has a validated idea and is ready to define the MVP
- User says "what should I build first?"
- User has a product concept but scope is unclear
- User wants to cut features before building

---

## The Goal: Define the MVP

An MVP is not:
- A landing page
- A demo
- A PowerPoint

An MVP is: **a working piece of software that solves a specific problem well enough that someone would actually use it.**

---

## Step 1: Define the Core Problem

Be ruthlessly specific.

**Bad:** "Helping people manage their finances"
**Good:** "Freelancers lose track of quarterly tax estimates because existing tools assume W-2 employment"

**Your task:** Help the user compress their idea into one tight problem statement. The tighter the problem definition, the easier every subsequent decision becomes.

Ask: *What is the one problem your first user has that you are going to solve?*

---

## Step 2: Define the Minimum Feature Set

List every feature the user thinks they need, then cut half.

If the MVP has more than 3–5 core features, it's too big. You're not building the final product — you're building the first thing real users will test.

**The cutting exercise:**

For each proposed feature, ask:
1. Does this feature solve the core problem?
2. Can a user get value without this?
3. What is the simplest version of this feature that still works?

Cut features that don't directly solve the core problem.

---

## Step 3: Choose a Platform

**For most startups: start with web.**

Reasons:
- Fastest to build
- Easiest to deploy
- Simplest to iterate on
- No app store review required
- Users can access immediately

You can always go native later once you've validated the product.

If the user is building mobile or desktop specifically, help them scope for that — but encourage web-first unless there's a clear reason not to.

---

## Step 4: Write the Spec

Structure the spec as follows:

```markdown
# [Company] MVP Spec

## Core Problem
[One tight problem statement]

## Target User
[Specific user type with the problem]

## Platform
[Web / Mobile / Desktop]

## MVP Features (max 5)
1. [Feature name] — [what it does, why it matters]
2. [Feature name] — [what it does, why it matters]
...

## Out of Scope (for now)
- [Feature]
- [Feature]

## Success Criteria
[How we know the MVP worked — e.g. "10 users pay for it" or "users complete X task without support"]
```

---

## Step 5: Identify What's Next

Once the spec is written, the next step is **Build** — use the `cofounder-build` skill.

The build phase covers:
- Create a repository
- Set up deployment (Vercel)
- Scaffold the app (Supabase backend)
- Build the frontend
- Deploy to production
- Testing and quality

---

## Cofounder Platform Reference

The Cofounder platform uses **Plan Mode** to help with this — an agent helps the user think through feature sets, identify what's essential, and produce a structured spec.

When running this skill independently, you are executing the plan-mode function manually.

---

## Key Constraints to Reinforce

1. **Ruthless specificity on the problem** — vague problem = vague solution
2. **Cut features aggressively** — if the list is long, it will take too long
3. **Web first** — unless there's a clear reason for mobile/desktop
4. **Spec before code** — write the spec first, then move to build

---

## Outputs

At the end of this skill, you should have:
- [ ] Core problem statement (one sentence)
- [ ] Target user description (specific)
- [ ] Platform decision (web default)
- [ ] MVP features list (≤5)
- [ ] Out-of-scope list
- [ ] Success criteria
