# Database

Source: https://docs.cofounder.co/cli/guide/database
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Query the company's Supabase database, ship schema changes and functions from the company repo, try changes on a branch, and move files in and out of storage.

The company's app runs on a Supabase database that Cofounder manages. These
commands work through your Cofounder login, so you never handle database
passwords or keys yourself.

Every command targets the company's default database. Pass `--resource` with a
database's name or id to pick another one, and `--branch` to work on a branch
instead of production. `cofounder database refs list` shows the databases the
company can use.

| MCP | CLI | API |
| --- | --- | --- |
| `database_refs_list` | `cofounder database refs list` | `GET /cofounder-cli/v1/company/database/refs` |
