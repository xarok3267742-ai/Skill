---
name: android-app-developer
description: Create, extend, refactor, or debug Android applications for phone, tablet, TV, or Wear OS using Kotlin, Jetpack Compose, Gradle, and the architecture appropriate to the product or already established in the repository.
---

# Android App Developer

Deliver production-ready Android behavior that matches confirmed product and form-factor requirements. Inspect project instructions, modules, build logic, dependency versions, variants, and architectural patterns before editing. Preserve user changes and avoid unrelated modernization.

For a greenfield app, default to native Kotlin and Jetpack Compose. Select current stable tools only after checking official Android documentation and compatibility with the available JDK, Gradle, Android Gradle Plugin, SDK, and target devices. Read [references/greenfield-and-form-factors.md](references/greenfield-and-form-factors.md) before scaffolding a project or adding TV/Wear support.

## Implementation workflow

1. Translate the approved product brief, complexity target, and language plan into observable behavior and acceptance criteria.
2. Choose the smallest coherent architecture for the product's actual complexity; do not add layers without a concrete boundary or testability benefit.
3. For existing apps, follow the established Compose/View, navigation, dependency injection, networking, persistence, and error-model patterns unless a migration is requested.
4. Model UI state and events explicitly. Cover loading, content, empty, recoverable error, offline, disabled, and permission-denied states when applicable.
5. Keep business logic out of composables, activities, services, tiles, and complication renderers. Make lifecycle, dispatcher ownership, cancellation, retry, and persistence behavior explicit where correctness depends on them.
6. Implement adaptive behavior for every selected form factor and locale instead of stretching or translating one layout mechanically.
7. Add tests at the cheapest reliable layer, then run the affected release-like variant.

## Non-negotiable checks

- No hard-coded user-facing strings when localization infrastructure exists.
- Stable list keys, intentional state ownership, one-way event flow, and correct save/restore behavior.
- No main-thread disk/network work, unbounded coroutine scope, or lifecycle-blind collection.
- Secrets, signing material, private endpoints, and credentials never enter source control, artifacts, screenshots, or logs.
- Permissions and foreground services are minimized, declared accurately, and requested in context.
- Repeated taps, back navigation, process recreation, configuration changes, and interrupted I/O do not corrupt state.
- New dependencies have a concrete benefit, compatible licenses and versions, and no unexplained SDK/data behavior.

Read [references/verification.md](references/verification.md) before choosing build and test commands.

## Handoff

Report changed behavior, affected modules, architecture decisions, checks and results, generated artifacts, and any unverified device-, locale-, service-, or account-dependent behavior. Never claim a build, device test, or visual check that was not performed.
