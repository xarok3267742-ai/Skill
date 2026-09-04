# TV and Wear OS design

Verify current official platform guidance before fixing measurements, required assets, navigation models, or quality criteria.

## Android TV

- Design for distance viewing, landscape composition, safe visual margins, and clear hierarchy.
- Every action must work with D-pad/remote input. Specify initial focus, focus movement, focus visibility, restoration after navigation, and Back behavior.
- Avoid dense text, hover assumptions, touch gestures, hidden controls, and long keyboard entry.
- For media, define transport controls, resume behavior, errors, subscriptions, account linking, and picture-in-picture only when relevant.
- Provide implementation-ready launcher icon/banner and Play screenshot direction based on the actual TV UI.

## Wear OS

- Optimize for glanceable, interruptible, short interactions; keep the primary action immediate.
- Specify round and square layouts, edge avoidance, rotary input, tiles, complications, notifications, haptics, ambient behavior, and battery implications when relevant.
- Do not require direct username/password entry on the watch when a safer phone or platform authentication flow is available.
- Treat watch faces separately from apps and use current Watch Face Format constraints.

## Languages and cross-device journeys

Test real strings from every script family, including long translations, RTL, mixed-direction content, numerals, fonts, and truncation. State which device owns setup, authentication, payment, settings, data entry, and recovery. Define disconnected, stale, unavailable-companion, and delayed-sync behavior. Shared branding does not require identical navigation.
