---
name: mobile-ui-ux-designer
description: Design or audit implementation-ready Android product flows, screens, design systems, prototypes, and store-facing visual direction for phone, tablet, TV, and Wear OS.
---

# Mobile UI/UX Designer

Create a coherent product experience rather than decorative screens. Start from the approved audience, job, entry point, success event, competitor evidence, form factor, language plan, usage frequency, and failure conditions. Preserve real brand inputs and avoid generic dashboard patterns when they do not serve the product.

## Design sequence

1. Define the shortest core journey plus cancellation, retry, empty, offline, permission-denied, and destructive-action paths.
2. Establish information hierarchy, real content, navigation, and trust cues before styling.
3. Define semantic tokens and reusable components rather than screen-local values.
4. Specify interaction, focus, keyboard/remote/rotary input, system bars, insets, Back behavior, loading, feedback, and motion.
5. Adapt the interaction model to every selected form factor and language; do not scale one phone mockup or translate it mechanically.
6. Review accessibility, localization expansion, RTL, specialized typography, themes, and compact/expanded dimensions.
7. Produce implementation annotations and measurable acceptance criteria appropriate to the selected complexity target.

For audits, read [references/audit.md](references/audit.md). For new systems, read [references/design-system.md](references/design-system.md). For TV or Wear OS work, read [references/platform-design.md](references/platform-design.md).

## Visual tooling and outputs

Choose the smallest useful artifact: journey, wireframe, high-fidelity screen, component inventory, design tokens, prototype, or audit. Use `$visualize` when a flow or hierarchy is materially easier to understand visually. Use `$imagegen` only for original concept imagery, icons, backgrounds, or feature graphics; track generated assets and provenance internally. Do not add a public AI badge unless required. When final Play assets must avoid AI labeling, use image generation only for private ideation and recreate the approved direction with deterministic, rights-cleared assets.

For Play listing screenshots, turn the ASO brief into a premium, coherent visual story: strong first-frame value, clear hierarchy, precise alignment, concise localized captions, consistent brand treatment, and form-factor-specific composition. The UI shown must remain a truthful capture from the tested app. Do not use image generation to fabricate implemented functionality or to repaint app pixels. Connect every recommendation to a user or business outcome and clearly label hypotheses.

Avoid invented brand facts, inaccessible contrast, tiny targets, placeholder copy in final designs, unsafe destructive actions, and novelty that obscures primary tasks.

Hand the approved reference, semantic tokens, responsive rules, real localized content, component states, and measurable acceptance criteria to `$android-ui-layout-engineer`. That skill owns implementation and rendered visual comparison; this skill owns the product experience and design intent.
