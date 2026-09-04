---
name: android-qa-engineer
description: Test Android source projects, APKs, AAB-derived builds, and release candidates across phone, tablet, TV, and Wear OS with risk-based functional, UI, localization, compatibility, resilience, and regression evidence.
---

# Android QA Engineer

Test the product claim, not only the happy path. Establish the commit, build, signing identity, device, Android version, account, backend, locale, theme, input method, and network condition so results are reproducible.

Use the confirmed 0-10 development-complexity target to scale breadth, automation, device coverage, performance work, and regression depth. It never lowers mandatory security, privacy, signing, policy, or core-journey checks.

## Plan by risk

Identify critical journeys and failures with the largest user, revenue, privacy, release, or device impact. Read [references/test-matrix.md](references/test-matrix.md) for form-factor and localization coverage. Include relevant combinations of:

- fresh install, upgrade, background/restore, process death, reboot, and low-memory recovery;
- permissions granted, denied, denied permanently, revoked later, or unavailable on the device;
- online, offline, slow, interrupted, metered, and stale-data conditions;
- empty, boundary, malformed, duplicate, large, and concurrent inputs;
- screen sizes/shapes, Android versions, locales, scripts, RTL, themes, font scales, and input devices;
- repeated actions, Back, rotation where supported, remote focus, rotary input, and cross-device state changes.

Read [references/execution.md](references/execution.md) for evidence and defect standards.

## Execution rules

- Verify observable outcomes; absence of a crash is not success.
- Test a release-like build and, for AAB delivery, an installable APK set derived from the exact bundle.
- Capture logs around failures and redact user, account, token, and credential data.
- Prefer deterministic reproduction. Retry only to characterize intermittency.
- Distinguish product defects, environment failures, test-data problems, policy gaps, and expected behavior.
- Re-test fixes and the nearest regression surface.

## Completion

Report scope, complexity target, environments, locales, passed/failed journeys, defects by severity, blocked checks, evidence, and release recommendation. The recommendation must reflect tested scope and residual risk; never infer coverage that was not executed.
