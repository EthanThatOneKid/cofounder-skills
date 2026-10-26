# How Your Agent Works

Source: https://docs.cofounder.co/cli/get-started/how-your-agent-works
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** What your agent does with CofounderOS through MCP or the CLI: which company it picks, which guides it reads, what it asks you before acting, and how it reports progress.

Besides tools, Cofounder gives your agent guides to read, company context to
check, and rules about what needs your approval. You don't need to memorize
any of it. Your agent reads the same guidance through MCP or the CLI, and
knowing what it does tells you what to expect and what to ask for.

| Step | MCP | CLI |
| --- | --- | --- |
| Get started | `onboarding_get` | `cofounder onboarding` |
| Check who is signed in | `user_get` | `cofounder auth whoami` |
| List your companies | `company_memberships_list` | `cofounder company memberships list` |
| Read the company overview | `company_get` | `cofounder company show` |
| Read the roadmap | `roadmap_get` | `cofounder roadmap get` |
| Find and read guides | `list_resources`, `read_resource` | `cofounder skills list`, `cofounder skills show <name>` |
| Read recent events | `events_list` | `cofounder events list` |
| Post progress | `events_post` | `cofounder events post` |

The sections below name the MCP tool. A CLI agent runs the matching command.
