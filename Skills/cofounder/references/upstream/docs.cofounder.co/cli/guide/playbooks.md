# Playbooks

Source: https://docs.cofounder.co/cli/guide/playbooks
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Cofounder-defined goals an agent pursues for your company, one routine run at a time, using the cofounder CLI on the company's behalf.

A playbook is a goal Cofounder defines, such as keeping the company's state
current or finding a starting price. Cofounder writes and maintains each
playbook's instructions, so improvements reach every company on its next
routine run.

A **playbook run** is your company pursuing one playbook. It is one agent in a
sandbox that has the `cofounder` CLI, signed in as the person who started the
run. The agent works in **routine runs**: each one is a turn of that same
agent, so it keeps its context and sandbox from one routine run to the next.
Routine runs happen on the run's schedule, or right away when you continue the
run. The agent keeps its progress in two places: Library files people read,
and progress notes it posts to the company's event log, tagged with the run's
id, which `cofounder events list --attribute run_id=<id>` returns. When the
goal is met, the agent marks the run complete and its routine runs stop. A
company can have several playbook runs, of the same playbook too.
