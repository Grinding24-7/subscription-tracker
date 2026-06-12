# Security Policy

Subscription Tracker may handle sensitive personal finance metadata such as subscription names, bill amounts, due dates, renewal dates, and account-related preferences. Security reports are taken seriously.

## Reporting a Vulnerability

Do not create a public GitLab issue for suspected vulnerabilities.

Report security concerns privately to the project maintainers through the GitLab project contact path or by directly contacting the repository owner. Include as much detail as possible:

- Affected feature, route, or file.
- Steps to reproduce.
- Potential impact.
- Screenshots, logs, or proof-of-concept details when safe to share.
- Suggested remediation, if known.

## Response Expectations

Maintainers should acknowledge valid reports within a reasonable timeframe, assess impact, and coordinate a fix before public disclosure. Critical issues involving authentication, authorization, data exposure, or secret leakage should be prioritized.

## Security Requirements for Contributors

- Never commit `.env` files, API keys, tokens, passwords, private certificates, or production credentials.
- Keep `.env.example` free of secrets.
- Validate and sanitize user-provided data.
- Avoid logging sensitive account or financial data.
- Keep dependencies updated once package management is added.
- Use protected branches and merge request review for changes to authentication, authorization, or deployment configuration.

## Supported Versions

The project is in initial development. Security fixes are applied to the active `main` branch until formal release versioning is established.
