---
name: android-release-manager
description: Prepare, verify, and deliver Android releases through GitHub and Google Play, including versioning, PR gates, GitHub Actions, Fastlane, AAB upload signing, SSH-signed tags, Octo Browser verification, tracks, rollout, and recovery.
---

# Android Release Manager

Turn a tested commit into a traceable, idempotent release. Preserve the user's selected app, GitHub repository, Play account, Octo profile, countries, track, rollout, and desired terminal outcome. An explicit request to build/release/publish plus recorded intake answers authorizes ordinary in-scope GitHub, CI, policy-site, AAB-upload, submission, and rollout operations. Do not ask for another confirmation, including before publishing Google Sites, uploading the verified AAB, sending changes for review, or starting the configured rollout. Treat the release brief and preflight as internal verification, then act. Stop only for a human-only/evidence blocker or when the observed terminal criteria are satisfied.

## Preflight

Resolve the merged commit candidate, application ID, variant, version code/name, form factors, languages, release notes, markets, public privacy-policy deployment and URL, Play developer account/app, Octo profile, track, rollout, managed-publishing choice, QA/policy disposition, containment plan, and desired terminal outcome. Verify current official Google Play requirements, account eligibility, target SDK rules, and form-factor requirements.

When the full-publication scope does not specify a track, use production with 100% rollout and do not create optional internal, closed, or open test releases. This does not skip CI or QA. If the selected account/app is not eligible for production because Play mandates testing or another prerequisite, preserve production-ready artifacts and any permitted production draft and report the exact requirement without pretending the production outcome was reached. When the user prohibited testing tracks, do not create a mandatory closed-test release without a new instruction.

Read [references/github-actions.md](references/github-actions.md) before creating a repository, configuring secrets, merging a PR, or building a release. Read [references/fastlane-play-delivery.md](references/fastlane-play-delivery.md) before configuring or using Fastlane for Play delivery. Read [references/octo-publishing.md](references/octo-publishing.md) before operating Play Console or verifying a Fastlane delivery. Read [references/rollout.md](references/rollout.md) before choosing rollout and monitoring thresholds.

## Build and verify

- Build with the repository's pinned JDK, Gradle wrapper, variants, and documented environment.
- Run required tests and lint before merge and against the release candidate.
- Use Play App Signing with a separate upload key; never expose or commit a keystore or password.
- Verify AAB package ID, version, upload certificate, modules/ABIs, checksum, and installable bundle-derived APK set.
- Preserve CI run identity, source commit, signed tag, mapping files, native symbols, baseline profiles, and build provenance when produced.
- Smoke-test the release-like build, including launch, authentication, upgrade, links, notifications, billing, offline behavior, selected locales, and TV/Wear journeys as applicable.

## Publish idempotently

Before opening Play Console, generate or reconcile the in-scope privacy-policy draft, publish it through the selected Google Site in the selected Octo profile, and verify its canonical HTTPS URL in a fresh unauthenticated session. Record the policy source commit, generator access date in the private release record, Google Sites destination/publication time, content hash, effective date, locales, and final URL. Do not name the generator in the public policy. If an in-scope custom domain is configured, verify ownership and HTTPS; otherwise report the Google-account and Google Sites URL dependency explicitly. Do not publish a generic policy that conflicts with the exact app/package or observed data behavior.

Use the exact artifact downloaded from the successful GitHub run. Prefer a pinned `bundle exec fastlane` lane for repeatable AAB, mapping, metadata, screenshot, track, and rollout delivery after the Play app has completed the required one-time manual initialization. Keep Octo Browser for that bootstrap, declarations not supported by the API, and final visual/state verification. Before upload or retry, inspect Play for the version code and current release status. Verify the visible Google account, developer account, app, package, track, countries, and rollout before mutation.

After each upload, save, submit, or rollout action, re-read the resulting state. When this skill is the primary coordinator, update the execution checkpoint directly; when it runs as the release subagent, return immutable evidence and let the coordinator update the canonical checkpoint/release record. On timeout or ambiguous feedback, inspect the canonical status page before retrying. Never duplicate a version, release, tag, PR, workflow dispatch, or rollout. A local artifact, dispatched workflow, completed upload request, or transient success message is not sufficient proof of completion.

Stop with the draft preserved for CAPTCHA, 2FA, reauthentication, changed terms, insufficient permissions, unknown policy declarations, missing reviewer access, changed console flow, or signing-identity mismatch. Do not bypass or guess.

## Handoff

Produce the evidence and content for a release record with commit, verified SSH-signed tag, workflow URL/run ID, artifact path and SHA-256, package/version, upload-certificate fingerprint, policy URL/source/Google Sites publication/content hash, checks and results, approved exceptions, release notes, Play account/track/countries/rollout, monitoring/containment plan, and observed Console status. In multi-agent mode, return it to the coordinator, which alone writes the canonical release record. `In review` is not publicly available.
