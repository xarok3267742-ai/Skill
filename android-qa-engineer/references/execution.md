# QA execution and defect format

## Evidence

Retain commit/tag, build identifier, timestamp, device/emulator, form factor, Android version, locale and script direction, theme, font scale, input method, account type, network condition, screen recording or screenshots when useful, and the relevant redacted log interval.

## Defect record

- Title: observable failure and location.
- Severity: blocker, critical, major, minor, or cosmetic based on impact.
- Preconditions and test data.
- Minimal numbered reproduction steps.
- Actual result and expected result.
- Reproduction rate.
- Environment, locale, input method, build, and bundle provenance.
- Evidence and likely affected surface; mark technical cause as unconfirmed unless proven.

Avoid vague titles, duplicate defects, and severity based only on visual annoyance. If a requirement is ambiguous, record the ambiguity separately instead of inventing expected behavior.
