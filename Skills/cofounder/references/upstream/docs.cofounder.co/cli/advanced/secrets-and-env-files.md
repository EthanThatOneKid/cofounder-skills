# Secrets and Environment Files

Source: https://docs.cofounder.co/cli/advanced/secrets-and-env-files
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Where secrets live: managed app secrets that ship to deploy targets, database secrets, and local environment files.

There are two kinds of secrets in play, and they live in different places.
App secrets are values your deployed app reads at runtime. Local secrets are
what your environment needs to talk to Cofounder — `COFOUNDER_API_TOKEN`
and friends.
