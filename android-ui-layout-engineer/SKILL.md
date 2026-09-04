---
name: android-ui-layout-engineer
description: Implement or correct pixel-accurate Android layouts in Jetpack Compose or Views, keeping icons, controls, and text aligned consistently across screens, densities, font scales, locales, form factors, and UI states.
---

# Android UI Layout Engineer

Make the implemented interface visually stable and measurably consistent with the approved design. Use the existing design system and component architecture. Do not redesign the product flow, change business behavior, or "fix" alignment with arbitrary offsets that work only on one screenshot.

Use `$mobile-ui-ux-designer` when the product flow, hierarchy, interaction, or visual specification is unresolved. Use `$android-app-developer` for architecture, state, data, and application behavior. This skill owns layout implementation and rendered visual verification in Compose or the repository's established Views/XML stack.

## Establish the reference

Before editing, identify the authoritative source: Figma frame, screenshot, written specification, existing component, or design token. Record its viewport, density, system-bar treatment, font family and weight, text content, locale, theme, font scale, and input method when known. If no exact reference exists, infer a consistent rule from neighboring components and state the assumption.

Inspect the current UI stack, theme, reusable components, resource qualifiers, navigation host, and test setup before changing code. Preserve the established stack unless migration is explicitly requested.

## Build from constraints

- Define alignment using parent constraints, arrangements, baselines, padding, and semantic design tokens.
- Keep related icon and text geometry inside one reusable component so their positions cannot drift between screens.
- Use `dp` for spatial dimensions and `sp` or project typography tokens for text. Avoid raw pixels.
- Prefer layout relationships over absolute coordinates. Use fixed size only where the design actually requires it.
- Align text optically and by baseline where baseline alignment matters; do not assume equal bounding boxes mean visual alignment.
- Decide deliberately whether text wraps, truncates, scrolls, or expands. Never let unknown-length text silently move critical controls.
- Apply window, display-cutout, system-bar, and keyboard insets once at the correct container level.
- Keep minimum touch or focus targets independent from the visible icon size.
- Do not use negative padding, unexplained translation, repeated magic numbers, or per-device branches to hide a structural layout problem.
- Adapt by available window size, shape, posture, and input mode instead of device-model checks.

For Compose implementation and inspection rules, read [references/compose-layout.md](references/compose-layout.md). For rendered comparison, form-factor coverage, and acceptance thresholds, read [references/visual-verification.md](references/visual-verification.md).

## Required verification matrix

Render the affected screen in the configurations relevant to the product, including at least:

- the reference viewport and one smaller or narrower device;
- compact and expanded widths when phone/tablet or foldable layouts are supported;
- default font scale and an enlarged scale;
- short and long realistic localized text;
- light and dark themes when supported;
- LTR and RTL when supported;
- loading, content, empty, error, selected, disabled, and keyboard-visible states that affect geometry;
- D-pad focus and distance-readable rendering for Android TV;
- round/square screens, rotary input, and edge clipping for Wear OS.

Use screenshot comparison or an overlay when a reference image exists. Inspect the full screen and cropped high-risk regions. Fix the underlying layout rule and re-render; do not stop after code inspection. For Play captures, render deterministic states from the exact release candidate at the recorded locale, viewport, density, theme, and system-bar mode. Fix genuine UI defects in the app and recapture; never retouch app pixels, introduce screenshot-only offsets, or fabricate implemented functionality.

## Handoff

Report the reference used, tokens or component rules changed, tested configurations, visual evidence, known deviations, and why any deviation is intentional. Pass reproducible evidence to `$android-qa-engineer`. Never claim pixel accuracy or form-factor coverage without a rendered comparison.
