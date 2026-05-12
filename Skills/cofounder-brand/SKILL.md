---
name: cofounder-brand
description: Craft a company brand — story, values, and visual identity. Use when building a brand from scratch or refining an existing one.
compatibility: Created for any AI agent. No external services required.
metadata:
  author: EthanThatOneKid
  version: "1.0"
---

# Cofounder Brand Skill

This skill guides you through the **Identity** stage of the Cofounder Tech Tree — crafting a brand that tells customers why you exist, what you believe, and whether they should trust you.

## When to Use

- User is building a brand for a new company
- User has a product but no clear brand story
- User wants to refine or document an existing brand
- User says "help me with branding"

---

## What a Brand Is

A brand is not just a logo. It is the story people attach to your company.

A brand has three parts:
1. **The story of the company** — why does the company exist?
2. **A set of values** — what do you believe that should show up in the product?
3. **A visual identity** — what does the company look and feel like?

---

## Step 1: Find the Story

Start with *why*. The story is the emotional anchor.

**Good stories come from:**
- Problems you've seen up close
- Pain points you've personally experienced
- Industries you've worked inside
- Observations about what customers do because the product doesn't exist

**Examples:**
- Uber: Someone waited 20 minutes for a cab and realized the system was broken
- Airbnb: Travel should help people feel like they belong anywhere
- Stripe: The internet should make it easier for more businesses to participate

**Exercise for the user:**
*What is the seed of your brand? What problem did you see, and why did you decide to solve it?*

The story doesn't need to be dramatic. It needs to be a story — one that people can repeat.

---

## Step 2: Define Brand Values

Brand values should be clear and actionable. They should shape product and marketing decisions.

**Good values:**
- Nike: Sport should move the world forward and be accessible to everyone
- Stripe: The internet should make it easier for more businesses to participate in the global economy
- Shopify: Anyone, anywhere should be able to start and grow a business

**Bad values (too vague):**
- "We innovate"
- "We put customers first"
- "We're passionate"

Values should sound like something a real person believes — not a corporate poster.

---

## Step 3: Design the Visual Identity

The visual identity is how the brand shows up. It needs to feel **intentional and consistent** — not perfect, but deliberate.

### Elements of a Visual Identity

1. **Logo** — the primary mark
2. **Color palette** — primary, secondary, accent colors with hex codes
3. **Typography** — fonts for headings and body
4. **Button and layout styles** — standard components
5. **Image/illustration style** — how visuals look (photos, illustrations, screenshots)
6. **Rules for how everything works together**

### Color Palette Exercise

Pick:
- A **primary color** — the main brand color (e.g., dominant in logo, headers)
- A **secondary color** — supporting tones
- An **accent color** — used sparingly for CTAs and highlights
- A **dark and light background** — for light/dark mode or card backgrounds

Document as:
```
Primary:     #XXXXXX
Secondary:   #XXXXXX
Accent:      #XXXXXX
Background:  #XXXXXX (light) / #XXXXXX (dark)
Text:        #XXXXXX (light bg) / #XXXXXX (dark bg)
```

### Typography Exercise

Pick:
- A **heading font** — distinctive, works at large sizes
- A **body font** — readable, works at small sizes

### Logo Guidance

- Keep it simple
- Works at small sizes (favicon) and large (website header)
- Works in one color (monochrome) and in full color
- Avoid trends — timeless beats trendy

### Image Style

Decide how the product and marketing will look in imagery:
- Real photography vs. illustrations vs. screenshots
- People vs. no people
- Lifestyle vs. abstract
- Color treatment (vibrant vs. muted, warm vs. cool)

---

## Step 4: Document the Brand Guide

Compile everything into a `DESIGN.md` file in the company's repository:

```markdown
# Brand Guide — [Company Name]

## Story
[One to three paragraphs on why the company exists]

## Values
1. [Value name]: [what it means in practice]
2. [Value name]: [what it means in practice]
...

## Visual Identity

### Logo
[Description of logo usage, variations, clearance space]

### Color Palette
- Primary: #XXXXXX
- Secondary: #XXXXXX
- Accent: #XXXXXX
- Background Light: #XXXXXX
- Background Dark: #XXXXXX
- Text Light: #XXXXXX
- Text Dark: #XXXXXX

### Typography
- Headings: [Font name, weights]
- Body: [Font name, weights]

### Button Styles
[Description or examples of standard button treatments]

### Image Style
[Description of how photography/illustration should look]

## Voice and Tone
[Tone adjectives — e.g., direct, confident, warm]
[Example copy in brand voice]
```

---

## Common Mistakes

- **Trying to be everything to everyone** — a brand that speaks to everyone speaks to no one
- **Inconsistency** — using different colors, fonts, or tones across different channels
- **Copying competitors** — your brand should be distinct, not a slightly different version of someone else's
- **Overdesigning early** — start with clean and intentional, not complex and elaborate

---

## Cofounder Platform Reference

The Cofounder platform can work with you to create a brand guideline — story, values, and visual identity — so the brand feels consistent from day one.

When running this skill independently, you are executing this brand-building function manually.

---

## Outputs

At the end of this skill, you should have:
- [ ] Company story (why the company exists)
- [ ] Brand values (1–5 clear, actionable values)
- [ ] Color palette documented with hex codes
- [ ] Typography choices documented
- [ ] Logo usage guidelines
- [ ] Image/illustration style direction
- [ ] `DESIGN.md` file created in the repository
