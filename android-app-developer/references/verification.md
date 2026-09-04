# Android verification routing

Prefer repository wrappers and documented tasks. Discover tasks and variants only when needed. Run narrow checks first, then the release-like variant selected for delivery.

- Kotlin/domain logic: affected module unit tests and static analysis.
- Compose/View behavior: semantics or instrumentation tests plus emulator/device interaction when focus, lifecycle, permissions, input, or rendering matters.
- Resources, manifest, dependencies, shrinking, or packaging: assemble/bundle the affected variant and run lint.
- Database or serialized-state migrations: migration tests and upgrade paths from every supported schema/app version.
- Localization: every launch locale, fallback behavior, missing resources, expansion, fonts, number/date formatting, and RTL where applicable.
- TV: D-pad navigation, focus restoration, Back, launcher entry, remote-only completion of core journeys, media controls, and low-memory behavior.
- Wear OS: round/square rendering, standalone/companion flows, tiles/complications, rotary input, ambient behavior, and battery-sensitive work.
- Performance-sensitive changes: measure a release-like build; debug timings are not representative.
- Release-only behavior: verify the release/baseline-profile variant without exposing signing credentials.

When an AAB is the deliverable, verify its manifest, package, version, signing certificate, included modules/ABIs, and an installable APK set derived with the project's supported bundle tooling.

If the environment lacks an SDK, emulator, physical device, credentials, backend, or proprietary dependency, identify the exact missing prerequisite and complete every independent check.
