# Compose and Views layout rules

## Diagnose before changing

Inspect the complete modifier chain or View hierarchy and parent constraints. In Compose, modifier order changes measurement, drawing, clipping, click area, and semantics. In Views, inspect layout params, resource qualifiers, constraint relationships, minimum sizes, padding, and inherited styles. Determine whether drift originates in the parent, content padding, intrinsic text metrics, icon asset bounds, window insets, or an applied transform.

## Stable Compose patterns

- Use shared spacing, sizing, typography, shape, and color tokens rather than copying literals.
- For icon-label rows, define a reusable component with an explicit icon box, gap, text style, vertical alignment, semantics, and touch target.
- Use `Row` and `Column` alignment and arrangement for linear relationships; use `Box` for deliberate overlay; use `ConstraintLayout` only when relationships justify it.
- Use `weight` only when remaining-space distribution is intended. Avoid combining accidental intrinsic measurement with weight.
- Use `Alignment.CenterVertically` for ordinary controls and baseline alignment for text whose typographic baselines must match.
- Inspect vector viewport whitespace and raster transparent padding before compensating in layout code.
- Give text a defined width policy and overflow behavior. Test actual localized strings rather than repeated placeholder text.
- Hoist common screen gutters and content-width rules so headings, body text, cards, and controls share anchors.
- Keep state ownership and event behavior outside purely visual components. Use stable inputs and keys so layout checks are not obscured by avoidable recomposition or list movement.
- Add accessibility semantics intentionally; a visually correct control with a broken label, role, state, traversal order, or target size is not complete.

## Stable Views/XML patterns

- Preserve the repository's established View Binding, Data Binding, styles, themes, and component conventions.
- Prefer constraint relationships, guidelines, barriers, chains, and dimension resources over absolute positioning or device-specific copies.
- Use resource qualifiers only for genuine configuration differences, not to patch a layout that should be adaptive.
- Check `includeFontPadding`, baselines, drawable padding, compound drawables, minimum dimensions, and state-list assets before adding offsets.
- Keep content descriptions, focus order, and accessibility state synchronized with the visible control.

## Common causes of crooked UI

- different horizontal padding on sibling containers;
- icons with unequal internal artwork bounds;
- mixed line heights or font-padding assumptions;
- center alignment where baseline alignment is required;
- duplicated components with slightly different literals;
- applying safe-area or keyboard insets at multiple levels;
- fixed heights that fail when text wraps;
- `offset`, translation, or graphics-layer changes moving pixels without changing layout bounds;
- previews that use different fonts, content, density, or system-bar treatment from the tested build.

Prefer a component or token correction when the same defect appears more than once.
