# Security Policy / Sicherheitsrichtlinie

## Reporting a Vulnerability / Sicherheitslücke melden

If you discover a security vulnerability or security concern within any repository in the `entertain-and-more` organization, please report it responsibly:

1. **Do NOT open a public issue** or disclose vulnerability details publicly before a fix is available.
2. Use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories) on the affected repository to create a private draft advisory.
3. Or contact the maintainers directly via email:
   - `security@open-bricks.org`
   - `security@ellmos.ai`
   - `lukas@open-bricks.org`
   - `support@lukasgeiger.com`

---

## Response Timeline / Reaktionszeit

- **Acknowledgment:** Within 48 hours (best effort, guaranteed within 7 days)
- **Initial Assessment & Triage:** Within 5 business days (7 to 14 calendar days)
- **Fix & Disclosure Coordination:** Best effort, typically within 30 days depending on severity

---

## Supported Versions / Unterstützte Versionen

| Repository / Tool | Supported Release | Security Updates |
|---|---|---|
| Organization profile (`entertain-and-more/.github`) | Latest commit on `main` | :white_check_mark: Supported |
| Active applications (`rpx`, `KlangpultLight`, `ChatAndChess`) | Latest release or commit on `main`/`master` | :white_check_mark: Supported |

---

## Security Invariants / Sicherheitsinvarianten

- **Zero-Egress & Local-First:** All desktop tools, session managers, audio recording suites, and games operate 100% locally with zero unconsented telemetry, analytics, or cloud data egress.
- **Unprivileged User Mode (Non-Elevation):** Applications run strictly in standard user mode without requiring elevated administrator or root privileges.
- **Data Integrity & Local Asset Preservation:** Save games, audio recordings, campaign bundles, and configuration files remain under complete user ownership on the local filesystem.
