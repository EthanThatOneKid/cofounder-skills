---
name: cofounder-build
description: Scaffold a production-ready web app — repository, CI/CD, backend with Supabase, frontend with Next.js, deployment on Vercel, testing, and debugging.
compatibility: Requires git, Node.js, Vercel account, Supabase account. For payments: Stripe account. For email: Postmark account.
metadata:
  author: EthanThatOneKid
  version: "1.0"
---

# Cofounder Build Skill

This skill guides you through the **Build** phase of the Cofounder Tech Tree — from spec to a live, production-ready web application.

## When to Use

- User has an MVP spec and is ready to build
- User says "build my product"
- User needs to set up a repository, CI/CD, backend, or frontend
- User is deploying to production
- User is debugging or managing infrastructure

---

## Phase 1: Set Up the Foundation

### 1. Create a Repository

```bash
# Initialize a new GitHub repo
gh repo create [company-name] --private --clone
cd [company-name]
```

Set up a sensible folder structure for the tech stack:
```
company-name/
├── src/              # source code
├── public/           # static assets
├── tests/            # test files
├── .gitignore
├── README.md
└── package.json
```

**Branch protection:** Protect `main` so nobody can push directly to production.

**Add a `.gitignore`:** Never commit `.env` files, `node_modules`, secrets, or build artifacts.

### 2. Set Up Deployment First

**Before writing code**, set up deployment. This ensures every change is immediately visible in a real environment.

**Recommended: Vercel**
- Built for Next.js (and modern web frameworks)
- Handles scaling automatically
- Free tier available; paid plans ~$20/month per seat

Set up three environments:
1. **Preview** — per-PR deployments (automatic on Vercel)
2. **Staging** — mirrors production, connected to `main` branch
3. **Production** — live environment users see

### 3. Secret Management

Your app will need API keys, database connection strings, and auth secrets.

**Rules:**
- Never hardcode secrets in codebase — not even in private repos
- Use environment variables injected at runtime
- Different secrets per environment (staging ≠ production)
- Add `.env` files to `.gitignore`
- Rotate secrets periodically

---

## Phase 2: Scaffold the Backend

### Recommended Stack: Supabase

Supabase provides: PostgreSQL database, Auth, Storage, Real-time, and a dashboard.

### Database Schema

Design the schema around your MVP spec. Key principles:
- Only send users the data they need (least privilege)
- Never trust browser data — validate on the server
- Use **row-level security (RLS)** so users can only see their own data
- Write **migrations** for schema changes (never edit the schema directly in production)

### API Layer

Your API routes handle:
- Loading data for pages
- Saving form submissions
- Business logic
- Third-party service calls (Stripe, Postmark)

Keep routes clean and well-organized. Validate incoming data. Return helpful error messages.

### Third-Party Integrations

**Payments — Stripe:**
- Handles credit cards, subscriptions, invoicing, tax compliance
- 2.9% + 30¢ per transaction
- Set up webhooks to notify your app of payment events

**Transactional Email — Postmark:**
- Fast, reliable, focused on transactional email (not marketing)
- Free development tier; paid plans from $15/month for 10,000 emails
- Trigger emails on product state changes (signup, reset, receipt)

### Security Checklist

- [ ] Row-level security enabled on all tables
- [ ] Input validation on all API routes
- [ ] HTTPS everywhere (Vercel handles this automatically)
- [ ] No secrets in codebase
- [ ] Auth checks on every protected route

---

## Phase 3: Build the Frontend

### Recommended Stack: Next.js + TypeScript + React

Frontend development in 2026 is primarily TypeScript with component-based frameworks like React/Next.js.

**AI agents excel at translating designs and user flows into working UI code.** The agent is only as good as your direction.

**You need to deeply understand:**
- Core user flows
- Business logic
- What happens at each step

### UX Principles

1. **Define the first valuable moment** — identify the moment the product first delivers real value, then minimize steps to get there
2. **Every extra step is a drop-off risk**
3. **Write copy in the customer's language** — not the code language

### Design Guidance

If the user has a brand guide (from `cofounder-brand` skill):
- Follow the color palette, typography, and visual style
- Maintain consistency with the brand identity

If no brand guide exists:
- Use clean, professional defaults
- Prioritize clarity over decoration
- Make sure the product is usable on mobile

---

## Phase 4: Deploy to Production

### Deployment Pipeline

```
PR opened → preview environment (temp live URL) → human review → 
staging (prod mirror) → release gate → production (real users)
```

**Preview environments are key when working with AI agents:**
- Every PR gets a live URL
- No need to pull branches locally to see changes
- Review several changes in parallel
- You become the person who steers — not the person who writes every line

### Pre-Deployment Checklist

- [ ] All API routes have input validation
- [ ] Row-level security is enabled
- [ ] Auth checks on protected routes
- [ ] Environment variables set in Vercel (not in code)
- [ ] Staging tested and working
- [ ] Branch protection on `main`

---

## Phase 5: Testing and Quality

### Quality Control Checklist

Before any code ships, it should pass:

1. **Behavior tests** — does the core flow work?
2. **Code hygiene** — is it consistent and low-risk?
3. **Human review** — does it feel right in the app?

### Write Tests

- **Unit tests** — individual functions in isolation
- **Integration tests** — multiple parts working together
- **End-to-end (E2E) tests** — simulate real user interactions

Start with tests for core flows — the critical paths that, if broken, would make the app unusable.

**Warning:** When using AI agents to write tests, verify the tests actually test meaningful outcomes. Common failure: agents write tests that check "does this code do what this code does?" instead of "does this code do what the user needs?"

### Set Up Linting and Formatting

- **ESLint** — catches potential bugs
- **Prettier** — keeps formatting consistent

Run these automatically on save and on commit.

### Configure Agent Rules

If using AI agents to write code, set up rules files (`AGENTS.md`, `.cursorrules`) that specify:
- Tech stack and versions
- Coding conventions (naming, file structure, import patterns)
- Libraries to use (and not use)
- Examples of well-written code in the project
- Common pitfalls specific to the codebase

---

## Phase 6: Debugging in Production

### Where to Look

- **Vercel logs** — API routes and serverless function errors
- **Supabase logs** — database query performance, auth events
- **Browser dev tools (F12)** — Console (JavaScript errors) and Network (failed requests)

### For Serious Monitoring

Consider **Sentry** for error tracking — it automatically captures errors, shows exactly where they happened, and groups similar errors.

### Debugging Mental Model

Most bugs aren't mysterious. They're usually:
- A typo
- A missing environment variable
- An API that changed its response format
- A database query that doesn't account for a new edge case

The hard part isn't fixing the bug — it's finding it.

---

## Phase 7: Infrastructure Management

### Scaling the Database

Watch for:
- **Slow lookups** — add indexes (Supabase dashboard shows slow queries)
- **Storage growth** — set up data retention policies for old data
- **Connection limits** — upgrade plan if seeing connection errors

### Scaling Compute (Vercel)

Vercel handles scaling automatically, but costs can spike with traffic.

Cost management strategies:
- Cache aggressively
- Rate limit APIs
- Set up billing alerts
- Optimize function execution times

## Upstream References

Use the raw upstream notes under `references/upstream/` when updating this skill:
- `references/upstream/cofounder.co/how-to/build.md`
- `references/upstream/docs.cofounder.co/managed-services/overview.md`
- `references/upstream/docs.cofounder.co/managed-services/github.md`
- `references/upstream/docs.cofounder.co/managed-services/supabase.md`
- `references/upstream/docs.cofounder.co/managed-services/vercel.md`
- `references/upstream/docs.cofounder.co/managed-services/migrations.md`
- `references/upstream/docs.cofounder.co/integrations/payments-and-stripe.md`
- `references/upstream/docs.cofounder.co/managed-services/postmark.md`

---

## Outputs

At the end of this skill, you should have:
- [ ] Repository created with branch protection
- [ ] Vercel deployment configured (preview + staging + production)
- [ ] Supabase backend (database with RLS, auth)
- [ ] API routes for core flows
- [ ] Frontend scaffolded with Next.js + TypeScript
- [ ] Payment (Stripe) and email (Postmark) integrations
- [ ] Tests written for core flows
- [ ] Linting and formatting configured
- [ ] Agent rules (`AGENTS.md`) in the repo
- [ ] Live production URL
