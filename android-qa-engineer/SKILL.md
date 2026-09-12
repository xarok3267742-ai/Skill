---
name: android-qa-engineer
description: Test an Android build or release candidate and produce reproducible risk evidence. Use for functional, compatibility, localization, or regression verification.
---

# Android QA Engineer

Verify product claims and failure behavior against an identified commit and artifact. Record the build/signing identity, device and Android version, account/backend, locale, theme, input method, and network condition needed to reproduce each result.

Scale breadth and automation with the product’s 0–10 complexity target and actual risk. The score never relaxes security, privacy, signing, policy, or core-journey checks.

Read [test matrix](references/test-matrix.md) when device, form-factor, lifecycle, network, permission, or localization coverage needs planning. Read [execution and defect format](references/execution.md) when running tests or reporting defects.

Prioritize critical journeys and failures with the largest user, privacy, data-loss, release, or device impact. Test observable outcomes, not merely absence of crashes. Use a release-like build; for AAB delivery, verify an APK set derived from the exact bundle. Retry only to characterize intermittency, redact sensitive logs, retest fixes, and cover the nearest regression surface.

Consume layout evidence from `$android-ui-layout-engineer` but independently exercise high-risk visual states. For Play screenshots, verify that the visible state, data, locale, form factor, entitlement, and claim are reproducible from the recorded release candidate; reject fabricated functionality, retouched UI, personal data, or unreadable localization.

Report tested scope, environments, passed and failed journeys, defects by severity, blocked checks, evidence locations, residual risk, and a release recommendation. Do not infer coverage that was not executed.
