# Mobile Apps

Source: https://docs.cofounder.co/cli/guide/mobile
Fetched from: https://docs.cofounder.co/llms-full.txt

**Description:** Develop, test, build, and ship Expo mobile apps with EAS: previews, Maestro tests, store submissions, and over-the-air updates.

`cofounder mobile` runs an Expo (React Native) app's lifecycle on Expo
Application Services (EAS): installable previews, Android and iOS builds,
Maestro tests on emulators and simulators, TestFlight and Google Play
submissions, and over-the-air (OTA) updates. The commands run the pinned `eas`
CLI in a local app checkout, so EAS builds exactly the source you have. Every
command takes `--dir <app directory>` (default: the current directory) and
`--json` for structured results.

| MCP | CLI | API |
| --- | --- | --- |
| — | `cofounder mobile init` | `POST /cofounder-cli/v1/company/mobile/projects`, `POST /cofounder-cli/v1/company/mobile/projects/provision` |
| — | `cofounder mobile status` | `GET /cofounder-cli/v1/company/mobile/jobs`, `GET /cofounder-cli/v1/company/mobile/jobs/{job_id}` |
| — | — | `GET /cofounder-cli/v1/company/mobile/project`, `POST /cofounder-cli/v1/company/mobile/credentials`, `POST /cofounder-cli/v1/company/mobile/jobs`, `POST /cofounder-cli/v1/company/mobile/jobs/{job_id}/provider`, `POST /cofounder-cli/v1/company/mobile/jobs/{job_id}/outcome` |

The job and credential routes support the commands: each build, submission,
update, rollback, and test is recorded as a Cofounder job keyed by its intent,
so rerunning an interrupted command reuses the operation it already started.
