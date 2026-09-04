# Greenfield and form-factor implementation

## Greenfield baseline

Use Gradle Kotlin DSL and the repository's wrapper. Keep dependency versions centralized when the project is large enough to benefit. Start with one application module plus clearly justified feature or library modules; do not create a ceremonial multi-module architecture.

Use Compose for new UI, coroutines and structured concurrency for asynchronous work, and platform-recommended lifecycle/state APIs. Choose persistence, networking, dependency injection, and navigation based on product needs and the confirmed 0-10 complexity target. Pin versions that are compatible as a set and record the reason for non-obvious dependencies.

Define application ID, namespace, versioning, min/target SDK, supported locales and fallback, backup behavior, network policy, and release variants explicitly. Treat application ID and signing lineage as immutable release identities once uploaded to Play.

## Phone and tablet

Use adaptive layouts and window-size information rather than device-name checks. Verify compact and expanded widths, multi-window, system/keyboard insets, edge-to-edge, font scaling, dark theme, orientation policy, localization expansion, specialized scripts, and RTL when applicable.

## Android TV

Use the current official TV toolkit and manifest model. Implement deterministic D-pad focus, focus restoration, remote-friendly navigation, predictable Back behavior, distance-readable content, and TV launcher artwork. Do not leave touch-only interactions. For media apps, integrate playback, audio focus, and media-session behavior appropriate to the product.

## Wear OS

Use the current official Wear Compose and device APIs for apps. Define standalone versus companion behavior and phone communication before coding. Test round and square layouts, rotary input, tiles, complications, notifications, ambient behavior, and battery cost as applicable. Use the required current Watch Face Format for watch-face products.

## Multi-device products

Share domain/data code only where it remains platform-neutral. Keep device-specific navigation and presentation separate. Reconcile package names, signing keys, modules, feature delivery, listings, and data synchronization before release.
