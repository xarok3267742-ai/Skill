# Form-factor and localization test matrix

Build the smallest matrix that covers material risk. Pairwise representative coverage is acceptable for ordinary combinations; critical journeys must be exercised on every supported form factor and launch locale.

## Phone and tablet

Cover the minimum supported Android version, current target behavior, compact and expanded widths, multi-window where supported, portrait/landscape policy, keyboard/insets, notifications, deep links, permissions, process recreation, and relevant low-memory/offline conditions.

## Android TV

Complete every critical journey using only the remote/D-pad. Verify launcher presence and artwork, initial focus, visible focus, focus order and restoration, Back, media controls, authentication, text entry alternatives, low-memory behavior, and TV-specific store claims. Include representative 1080p and 4K layouts when supported.

## Wear OS

Cover representative round and square devices, small screens, rotary input, tiles, complications, notifications, ambient behavior, standalone/companion operation, disconnected phone, delayed sync, authentication, and battery-sensitive work. Test watch faces against the current required format and quality checks.

## Languages

For each launch locale, verify resource completeness, locale switching/restart behavior, fallback locale, real content, fonts and glyphs, line breaking, plural and number/date formatting, text expansion, accessibility labels, screenshots, and store metadata. For RTL, verify mirroring, navigation direction, mixed-direction identifiers, media controls, icons that must not mirror, and cursor/selection behavior.

## Complexity scaling

- 0-2: narrow device set and core proof, while retaining mandatory release checks if publication is requested.
- 3-4: core journey, common failures, supported locales, and basic compatibility regression.
- 5-6: production lifecycle, resilience, accessibility, release-like bundle, and meaningful device/locale coverage.
- 7-8: integration contracts, concurrency, migration, multi-form-factor, offline/sync, performance, and expanded regression.
- 9-10: high-assurance traceability, threat/risk-driven tests, extensive compatibility, recovery, observability, and domain-specific validation.
