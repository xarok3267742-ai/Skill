# Octo Browser and Google Play Console

Use mutations in this procedure when the user's explicit end-to-end build/release request and intake answers place them inside the recorded execution scope. Do not request an additional authorization summary. Read-only profile selection and identity discovery may occur near the beginning of intake.

Check the current Octo automation documentation before connecting: https://docs.octobrowser.net/en/api/start-api/

## Connect to the intended profile

Retrieve the Octo API token from the system secret store without printing it. On macOS, resolve it using `credentials.octo_api_keychain_service` and `credentials.octo_api_keychain_account`; configuration contains only those locators. A token supplied interactively may be written directly into the secret store once, but never replay it from the transcript or read it from a repository file, project YAML, command-line argument, browser script, or log. Resolve the configured profile ID or unique profile name, launch that exact profile through the supported Octo API, and attach Playwright through its CDP endpoint. Do not create, edit, export, transfer, or delete profiles unless separately requested.

Use accessibility roles, labels, visible text, and current DOM state instead of fixed coordinates. Console structure changes frequently; inspect each page before acting. Keep screenshots or state notes around important transitions, redacting account and personal information.

## Early read-only identity discovery

Ask the user to select the Octo profile near the beginning of intake. Connect to that exact profile without navigating away from or changing unrelated account state. Inspect the active Google identity, Play developer display name, existing public developer contact, and Google Sites availability only as needed. Record candidate email/name values as discovered and redact them from logs and screenshots. Prefer values already published for the selected Play developer; ask a factual question only if the public identity or destination remains ambiguous. Do not change the account, create a site, or publish anything during this read-only phase.

Use the same selected profile for the policy generator, Google Sites, and Play Console unless the recorded execution scope explicitly names different profiles. If identity changes between stages, stop before mutation.

## Preflight identity

Before changing Play Console, verify all of the following from visible state:

- expected Google account and Play developer account;
- expected app and package ID, or the confirmed new-app creation target;
- expected version code/name, track, countries, rollout, and managed-publishing mode;
- completed app-content, policy, listing, access, pricing, and distribution prerequisites.
- the canonical privacy-policy URL returns the approved policy over HTTPS in a fresh unauthenticated session and identifies this exact app/package.

A mismatch is a blocker. Do not switch accounts, apps, packages, tracks, or countries by guessing.

## Idempotent release flow

Inspect the target track and App bundle explorer for the version code before uploading. If the exact bundle already exists, reconcile its certificate, checksum/provenance when available, release notes, and status instead of uploading again.

Upload the locally verified artifact from the exact successful GitHub run. Resolve warnings only when supported by code, policy evidence, or verified product facts. Reconcile declarations and store assets with the tested build. Then submit and roll out according to the recorded track, countries, percentage, and managed-publishing setting.

After every create, upload, save, submit, or rollout action, re-read the resulting page and record the visible status. On timeout or ambiguous feedback, reload or navigate to the canonical status page before any retry.

## Human-only blockers

Stop with the draft preserved for CAPTCHA, 2FA, reauthentication, unavailable permissions, changed terms, identity verification, an unknown legal/policy declaration, missing reviewer credentials, or a materially changed console flow. State the exact blocking page, what is preserved, and the single action or fact needed to resume.

Google review and new-account testing eligibility can prevent a requested production release. Report the actual state such as draft, internal, closed testing, changes sent for review, in review, approved with managed publishing, rollout active, or available. Never translate a pending state into `published`.
