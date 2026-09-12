---
name: android-release-manager
description: Deliver a verified Android release through GitHub and Google Play. Use for CI, signing, Fastlane, Octo/Console, submission, rollout, or release recovery.
---

# Android Release Manager

Turn one tested commit into an idempotent release for the recorded repository, Play account, package, version, countries, track, and rollout. An explicit build/publish request plus resolved intake authorizes in-scope release actions without another confirmation gate.

## Route by operation

Read only what the release needs:

- [GitHub, CI, and signing](references/github-actions.md) for repository setup, secrets, PR/merge, upload signing, or tags;
- [Fastlane delivery](references/fastlane-play-delivery.md) for API credentials, lanes, metadata, screenshots, AAB upload, or retry behavior;
- [Octo publishing](references/octo-publishing.md) for Google Sites, new-app bootstrap, unsupported declarations, or visual Console verification;
- [rollout and monitoring](references/rollout.md) when choosing, starting, observing, halting, or recovering a rollout.

Verify current Play eligibility, target SDK, form-factor requirements, and pricing at release time. Resolve the exact commit, artifact, package/version, certificate, policy URL, locales, countries, track, rollout, QA/policy disposition, and terminal outcome.

For the default zero-cost/free/no-monetization contract, verify the binary, dependencies, listing, declarations, products, and Console pricing contain no unintended monetization. Do not create payments products, paid services, or auto-converting trials. Record the current Play consequence of offering the package for free.

## Build and publish

Use the repository’s pinned toolchain and the exact AAB from the successful GitHub workflow. Verify package, version code, upload certificate, modules, checksum, installable bundle-derived APK set, source commit/tag, and produced mapping/symbol/provenance artifacts. Keep the upload key separate from Play App Signing; never commit or log private signing material.

Publish or reconcile the app-specific privacy policy before entering its URL in Play. The page must work over HTTPS without login; public text must match observed behavior and must not name the drafting tool.

Prefer pinned `bundle exec fastlane` for repeatable metadata, screenshot, track, rollout, and AAB delivery after required one-time app initialization. Use Octo for that bootstrap, Google Sites, declarations unavailable through the API, and final account/app/status verification. Never run competing browser and Fastlane mutations.

Before any retry, inspect the canonical Play state for the version code and release status. After every upload, save, submit, or rollout request, re-read the result. A workflow dispatch, local artifact, API response, click, toast, or page transition is not completion evidence.

Stop and preserve the draft for CAPTCHA, 2FA, reauthentication, changed terms, insufficient permissions, signing mismatch, unknown legal declaration, or changed Console flow. Do not bypass or guess.

Report the commit, verified signed tag, workflow URL/run, AAB path and SHA-256, upload-certificate fingerprint, policy URL/hash, checks, exceptions, Play account/track/countries/rollout, and observed status. `In review` is not publicly available.
