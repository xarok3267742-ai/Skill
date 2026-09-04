# Project workspace contract

Use a user-selected project root. If none is provided for a greenfield app, propose `~/Documents/AndroidApps/<slug>` and resolve it to an absolute path before creating files.

```text
<project-root>/
|-- repo/                 Git working tree
|   |-- .codex/
|   |   `-- android-product.yaml
|   |-- docs/
|   |   |-- product-brief.md
|   |   |-- research/
|   |   `-- releases/
|   |-- play/
|   `-- .github/workflows/
|-- private/              mode 0700; never committed
`-- artifacts/            downloaded release outputs and evidence
```

For an existing repository, do not relocate it without permission. Create sibling `private` and `artifacts` directories at a safe project root, or record explicit absolute paths in the configuration.

## `android-product.yaml`

Use this non-secret shape and omit sections that do not apply:

```yaml
schema_version: 1
product:
  slug: "example"
  display_name: "Example"
  application_id: "com.example.app"
  complexity: 5
  form_factors: ["phone", "tablet"]
  default_locale: "en-US"
  locales: ["en-US"]
  play_listing_locales: ["en-US"]
  fallback_locale: "en-US"
git:
  provider: "github"
  owner: "owner"
  repository: "example-android"
  visibility: "private"
  default_branch: "main"
play:
  developer_account: "Developer display name"
  octo_profile_id: "profile-id"
  track: "internal"
  countries: ["US"]
  managed_publishing: false
release:
  version_name: "1.0.0"
  version_code: 1
  rollout_percent: 100
```

This file is configuration, not authorization. Validate complexity as an integer from 0 through 10, package-name syntax, allowed form-factor and track values, positive monotonic version codes, locale/country formats, and rollout range before using it.

## Secret boundary

Keep upload keystores and private credentials in `private/` with restrictive permissions. Store passwords and API tokens in macOS Keychain or the active platform secret store. Put CI copies only in GitHub encrypted secrets, transmit them through stdin or protected environment variables, and never print them.

The repository may contain the public upload certificate and its SHA-256 fingerprint. It must ignore `private/`, artifacts, keystores, signing properties, `.env*`, tokens, cookies, browser profiles, and generated release outputs. Before every push and package, inspect tracked files and history for secret-like paths and values.

Require an encrypted backup and a documented restore owner before the first production release. Do not test restoration by exposing or committing a private key.
