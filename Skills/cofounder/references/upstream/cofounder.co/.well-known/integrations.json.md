# Integration discovery manifest

Source: https://cofounder.co/.well-known/integrations.json
Fetched from: https://cofounder.co/.well-known/integrations.json

{
  "version": 3,
  "summary": "Cofounder is an agent-first platform for running a company. Agents create and set up a company, then operate its deploys, database, domains, email, phone, ads, payments, CRM, and research through a hosted MCP server, the cofounder CLI, or the REST API — three transports over the same operation surface.",
  "credentials": {
    "cofounder-account": {
      "type": "oauth2",
      "label": "Cofounder account",
      "generateUrl": "https://app.cofounder.co/login",
      "setup": "Create or sign in to a Cofounder account at https://app.cofounder.co/login (email/password, Google, or GitHub). MCP clients discover the authorization server through the protected-resource metadata at https://api.superoptimizers.cofounder.co/.well-known/oauth-protected-resource and complete the hosted Supabase OAuth 2.1 flow in the browser — no manual credential is needed. The cofounder CLI runs the same flow with `cofounder auth login`."
    },
    "cofounder-session-token": {
      "type": "bearer",
      "label": "Cofounder session token",
      "setup": "After `cofounder auth login`, run `cofounder auth token` (or `cofounder auth token --json`) to print a Supabase access token for the signed-in user. Send it as `Authorization: Bearer <token>` to the REST API or the MCP endpoint, or export it as `COFOUNDER_API_TOKEN` for the CLI. It expires with the session — mint a company API key for durable automation."
    },
    "cofounder-api-key": {
      "type": "api_key",
      "label": "Cofounder company API key",
      "setup": "With an admin CLI session, run `cofounder company api-keys create --name <name>` (POST /cofounder-cli/v1/company/api-keys). The `cfk_…` secret prints once. Send it as `Authorization: Bearer <key>` to the REST API, or export it as `COFOUNDER_API_TOKEN` for the CLI. Keys authenticate as the company that minted them and can be revoked with `cofounder company api-keys revoke`. Accepted by the REST API and CLI — the hosted MCP endpoint takes OAuth or session tokens instead."
    }
  },
  "surfaces": [
    {
      "type": "mcp",
      "slug": "cofounder-mcp",
      "name": "Cofounder MCP server",
      "docs": "https://docs.cofounder.co/cli/get-started/connect-an-agent",
      "url": "https://api.superoptimizers.cofounder.co/mcp",
      "transports": ["streamable-http"],
      "basis": {
        "via": "declared",
        "source": "https://cofounder.co/.well-known/integrations.json"
      },
      "auth": {
        "status": "required",
        "entries": [
          {
            "use": [
              {
                "id": "cofounder-account",
                "mechanics": { "source": "well-known" }
              }
            ],
            "basis": {
              "via": "declared",
              "source": "https://cofounder.co/.well-known/integrations.json"
            }
          },
          {
            "use": [
              {
                "id": "cofounder-session-token",
                "mechanics": {
                  "source": "http",
                  "in": "header",
                  "headerName": "Authorization",
                  "scheme": "Bearer"
                }
              }
            ],
            "basis": {
              "via": "declared",
              "source": "https://cofounder.co/.well-known/integrations.json"
            }
          }
        ]
      }
    },
    {
      "type": "http",
      "slug": "cofounder-api",
      "name": "Cofounder Agent-First API",
      "docs": "https://docs.cofounder.co/cli",
      "url": "https://api.superoptimizers.cofounder.co/cofounder-cli/v1",
      "spec": "https://api.superoptimizers.cofounder.co/openapi.json",
      "basis": {
        "via": "declared",
        "source": "https://cofounder.co/.well-known/integrations.json"
      },
      "auth": {
        "status": "required",
        "entries": [
          {
            "use": [
              {
                "id": "cofounder-api-key",
                "mechanics": {
                  "source": "http",
                  "in": "header",
                  "headerName": "Authorization",
                  "scheme": "Bearer"
                }
              }
            ],
            "basis": {
              "via": "declared",
              "source": "https://cofounder.co/.well-known/integrations.json"
            }
          },
          {
            "use": [
              {
                "id": "cofounder-session-token",
                "mechanics": {
                  "source": "http",
                  "in": "header",
                  "headerName": "Authorization",
                  "scheme": "Bearer"
                }
              }
            ],
            "basis": {
              "via": "declared",
              "source": "https://cofounder.co/.well-known/integrations.json"
            }
          }
        ]
      }
    },
    {
      "type": "cli",
      "slug": "cofounder-cli",
      "name": "cofounder CLI",
      "docs": "https://docs.cofounder.co/cli",
      "command": "cofounder",
      "packages": [
        {
          "registryType": "npm",
          "identifier": "@generalintelligence/cofounder",
          "runtimeHint": "npx"
        }
      ],
      "basis": {
        "via": "declared",
        "source": "https://cofounder.co/.well-known/integrations.json"
      },
      "auth": {
        "status": "required",
        "entries": [
          {
            "use": [
              {
                "id": "cofounder-account",
                "mechanics": {
                  "source": "cli",
                  "command": "cofounder auth login"
                }
              }
            ],
            "basis": {
              "via": "declared",
              "source": "https://cofounder.co/.well-known/integrations.json"
            }
          },
          {
            "use": [
              {
                "id": "cofounder-api-key",
                "mechanics": {
                  "source": "cli",
                  "env": ["COFOUNDER_API_TOKEN"]
                }
              }
            ],
            "basis": {
              "via": "declared",
              "source": "https://cofounder.co/.well-known/integrations.json"
            }
          },
          {
            "use": [
              {
                "id": "cofounder-session-token",
                "mechanics": {
                  "source": "cli",
                  "env": ["COFOUNDER_API_TOKEN"]
                }
              }
            ],
            "basis": {
              "via": "declared",
              "source": "https://cofounder.co/.well-known/integrations.json"
            }
          }
        ]
      }
    }
  ]
}
