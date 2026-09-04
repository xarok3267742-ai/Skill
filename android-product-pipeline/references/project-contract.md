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
|   |   `-- privacy-policy/ Canonical policy source by locale
|   `-- .github/workflows/
|-- private/              mode 0700; never committed
|-- worktrees/            temporary isolated agent worktrees; never committed
`-- artifacts/            downloaded release outputs and evidence
    |-- agents/           per-run, per-agent reports and test evidence
    `-- pipeline-state.yaml Resumable, non-secret execution checkpoint
```

For an existing repository, do not relocate it without permission. Create sibling `private`, `worktrees`, and `artifacts` directories at a safe project root, or record explicit absolute paths in the configuration. Keep `worktrees/` and `artifacts/agents/` outside the application repository; if that is impossible, ignore them before agent work begins and verify they are not tracked before every push.

## `android-product.yaml`

Use this non-secret shape and omit sections that do not apply:

```yaml
schema_version: 1
product:
  slug: "example"
  display_name: "Example"
  application_id: "com.example.app"
  complexity: 5
  development_budget: 0
  store_pricing: "free"
  monetization: "none"
  form_factors: ["phone", "tablet"]
  default_locale: "en-US"
  locales: ["en-US"]
  play_listing_locales: ["en-US"]
  fallback_locale: "en-US"
cost_controls:
  allow_new_paid_services: false
  allow_paid_assets: false
  allow_trials_that_convert_to_paid: false
  prefer_local_or_open_source: true
git:
  provider: "github"
  owner: "owner"
  repository: "example-android"
  visibility: "private"
  default_branch: "main"
play:
  developer_account: "Developer display name"
  octo_profile_id: "profile-id"
  delivery: "fastlane"
  fastlane_metadata_path: "fastlane/metadata/android"
  track: "production"
  countries: ["US"]
  managed_publishing: false
privacy_policy:
  draft_generator_url: "https://app-privacy-policy-generator.firebaseapp.com/"
  hosting: "google-sites"
  source_path: "play/privacy-policy"
  google_sites_site_name: "Android App Policies"
  page_slug: "com-example-app"
  public_url: "https://sites.google.com/view/android-app-policies/com-example-app"
  custom_domain: null
  public_developer_name: "Example Developer"
  public_contact_email: "privacy@example.com"
  locales: ["en-US"]
  fallback_locale: "en-US"
credentials:
  octo_api_keychain_service: "codex.android-product-pipeline.octo-api"
  octo_api_keychain_account: "default"
  play_auth: "workload-identity"
  play_wif_provider_github_variable: "GOOGLE_WORKLOAD_IDENTITY_PROVIDER"
  play_service_account_github_variable: "GOOGLE_PLAY_SERVICE_ACCOUNT_EMAIL"
  play_service_account_json_github_secret_fallback: "GOOGLE_PLAY_SERVICE_ACCOUNT_JSON"
execution:
  mode: "autonomous-multi-agent"
  parallel_workers: "auto"
  desired_outcome: "play-available"
  scope_source: "explicit-user-request-and-intake"
release:
  version_name: "1.0.0"
  version_code: 1
  rollout_percent: 100
  skip_optional_play_testing_tracks: true
```

This file records the execution target but cannot broaden the user's task scope. `parallel_workers: "auto"` means use the available delegation capacity and the multi-agent contract; it is not a fixed promise of concurrency. `skip_optional_play_testing_tracks: true` means release directly to production when the account/app is eligible; it never disables build/QA verification or overrides a mandatory Play testing requirement. Validate complexity as an integer from 0 through 10, `development_budget` as a non-negative number, `store_pricing` as `free` or an explicit override, monetization against the implemented SDKs/features and Play products, package-name syntax, allowed form-factor, track and desired-outcome values, positive monotonic version codes, locale/country formats, rollout range, HTTPS policy URL, policy locale fallback, Google Sites destination, and page slug before using it. With the default values above, do not add paid downloads, ads, in-app products, subscriptions, paywalls, donations, paid APIs/assets/infrastructure, or trials that can convert to paid. Verify the current limits and licenses of every selected free service and dependency. Store `public_developer_name` and `public_contact_email` only when they are already public for the selected developer or otherwise established by user-stated facts. `credentials` contains locators only, never credential values.

## Secret boundary

Keep upload keystores and private credentials in `private/` with restrictive permissions. Store passwords and API tokens in macOS Keychain or the active platform secret store. For Octo Browser on macOS, use the configured Keychain service/account locator and retrieve the value at runtime without writing it to disk or stdout. Put CI copies only in GitHub encrypted secrets, transmit them through stdin or protected environment variables, and never print them.

The repository may contain the public upload certificate and its SHA-256 fingerprint. It must ignore `private/`, artifacts, keystores, signing properties, `.env*`, tokens, cookies, browser profiles, and generated release outputs. Before every push and package, inspect tracked files and history for secret-like paths and values.

Require an encrypted backup and a documented restore owner before the first production release. Do not test restoration by exposing or committing a private key.
