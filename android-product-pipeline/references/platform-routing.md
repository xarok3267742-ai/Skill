# Android form-factor routing

Check current official Android and Google Play documentation immediately before choosing SDK levels, libraries, manifest declarations, device filters, quality gates, or listing assets. Record source URLs and access dates in the release evidence.

Start with these canonical sources and follow their current linked requirements:

- Target API: https://developer.android.com/google/play/requirements/target-sdk
- App signing: https://developer.android.com/studio/publish/app-signing
- TV quality: https://developer.android.com/docs/quality-guidelines/tv-app-quality
- Wear OS quality: https://developer.android.com/docs/quality-guidelines/wear-app-quality

## Phone and tablet

Design responsive layouts for compact and expanded widths, edge-to-edge behavior, keyboard and system insets, orientation policy, large screens, multi-window, dynamic text, dark theme, localization expansion, and RTL where supported. Verify lifecycle restoration, offline behavior, permissions, deep links, notifications, and billing when applicable.

## Android TV

Design for distance viewing and remote/D-pad input. Define focus order and focus restoration, back behavior, overscan-safe composition, TV launcher activity/banner, search or media integration when relevant, playback controls, low-memory behavior, and absence of touch-only actions. Verify the current TV app quality checklist, architecture/page-size requirements, AAB requirement, and Play listing assets.

## Wear OS

Choose standalone, companion, or multi-device behavior explicitly. Design glanceable journeys for round and square screens, rotary input, tiles, complications, notifications, ambient behavior, battery limits, and short sessions. For watch faces, verify the current Watch Face Format requirements. For a phone companion, reconcile package name, signing key, listing strategy, and cross-device data behavior.

## Combined products

Share domain logic and data contracts only where that reduces risk. Do not force identical navigation or UI across form factors. State module, package, signing, listing, and release relationships before implementation, and test each Play-targeted form factor against its own quality checklist.
