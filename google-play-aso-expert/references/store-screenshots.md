# Production-grade Google Play screenshots

Create a high-conversion screenshot set without altering what the released app can actually do. Verify current Google Play screenshot counts, dimensions, aspect ratios, device categories, localization behavior, and policy requirements from official sources at execution time.

Before art direction, audit the screenshot strategy of 5-8 current competitors for each material market/locale/form-factor cluster, or validate and reuse a still-current dated audit. Record sequence, opening promise, proof style, caption density, device framing, localization, recurring visual conventions, and exploitable gaps with source URLs and access dates. Use patterns as evidence, never as assets to copy.

## Specialist production chain

Use the specialist skills as one evidence-backed pipeline:

1. `$google-play-aso-expert` owns the screenshot brief: audience, market, objection, benefit, proof, headline, frame order, device category, locale, and experiment hypothesis.
2. `$mobile-ui-ux-designer` owns art direction: story rhythm, hierarchy, composition, caption placement, brand consistency, contrast, safe zones, and cultural adaptation.
3. `$android-app-developer` provides deterministic demo/test data and reachable capture states without exposing real user data or introducing screenshot-only product behavior.
4. `$android-ui-layout-engineer` renders and visually verifies the actual app at the required viewport, density, theme, locale, font scale, system-bar mode, and form factor. Fix genuine product-layout defects; never add one-off offsets that only improve a store image.
5. `$imagegen` may create private moodboards and decorative concepts. When submitted assets must remain free of AI labeling, use it only for private exploration and prefer final content with evidence that it falls outside current labeling requirements. Track content-level origin for images, captions, metadata, visible demo content, and artwork; merely redrawing an AI concept deterministically does not by itself settle declaration applicability. If generated or edited material is submitted, retain provenance and complete every current required declaration truthfully. Never use image generation to regenerate, repaint, extend, or fabricate the captured application UI, unavailable functionality, results, ratings, notifications, or user content. Add exact marketing text with a deterministic design/rendering tool and retain its authorship/edit history.
6. `$android-qa-engineer` verifies every final frame against the same release-candidate commit, observable behavior, supported locale/form factor, and approved claims.
7. `$android-release-manager` uploads only the approved, checksummed final exports and verifies the visible listing after save or submission.

In multi-agent execution, the ASO agent is the single writer for `repo/play/listing/screenshots/manifest.yaml` and assigned listing-source paths. The UX, layout, linguistic, and QA agents return immutable role-specific evidence for the ASO agent to merge. The coordinator validates and integrates the ASO commit but does not co-author the manifest. The release agent returns immutable upload/preview evidence to the coordinator rather than rewriting the frozen screenshot manifest, release record, or checkpoint, and it alone mutates Play Console.

## Build the story

- Define one primary promise for the set and one clear benefit or objection per frame.
- Make the first two or three frames communicate the strongest differentiated value without requiring the viewer to read the full description.
- Order frames as a coherent product journey: outcome, proof, core action, useful depth, trust or differentiation. Change the sequence when another order better matches the audience.
- Use concise localized headlines that remain legible at store-thumbnail size. Avoid generic superlatives, keyword stuffing, unsupported numbers, fake awards, ratings, rankings, testimonials, or competitor references.
- Show the smallest amount of UI that proves the claim. Prefer meaningful content and intentional states over empty dashboards or repeated near-identical screens.
- Adapt the story, screenshots, and copy for locale and market; do not merely replace text. Check expansion, RTL/mixed direction, typography, cultural interpretation, number/date formats, and screenshot reading order.
- Give every screenshot locale an independent linguistic disposition. Record the reviewer or review method, language competence, reviewed text/version, semantic equivalence to the visible UI and reproducible behavior, cultural issues, corrections, date, and result. Machine translation without an independent linguistic pass cannot support a best-in-category quality claim.
- Produce separate sets for phone/tablet, Android TV, and Wear OS where Play or the product requires them. Show D-pad focus for TV only when natural to the proof, and use authentic round/square Wear captures without masking clipped content.

Use a comparison sheet when spreadsheet tooling is available: frame, market/locale, intended benefit, source screen/state, objection answered, headline, form factor, owner, status, and experiment variant.

## Capture from the release candidate

Freeze the source commit and final AAB before capture. Install and capture from an APK set derived from that exact AAB whenever the tooling permits. If capture must use another build, prove equivalence of code, resources, manifest, dynamic-feature delivery, build type, feature flags, signing-relevant behavior, and runtime configuration, and record the exception. Use controlled non-personal demo data that looks realistic, remains consistent across the sequence, and contains no credentials, account identifiers, private messages, health/financial records, or other personal information.

For every raw capture, record:

- source commit, version code/name, package ID, final AAB path/SHA-256/certificate, derived split/APK-set identity and hashes, installed package/version/certificate, and any equivalence proof;
- emulator/device model, Android version, viewport, density, form factor, orientation, system bars, and navigation mode;
- locale, theme, font/display scale, time/network state, and exact app state;
- capture command or repeatable navigation steps and raw-file SHA-256.

Remove debug banners, touch indicators, unstable clocks, cursors, test overlays, unintended notifications, and personal status-bar data through controlled capture configuration. Do not retouch the application pixels to hide layout bugs; fix the app, rebuild, and recapture.

## Compose the final marketing frame

Preserve the captured UI's proportions, readable content, and functional meaning. Cropping, device framing, background composition, shadow, and caption layout are allowed when they do not imply unavailable hardware or behavior. Never cover a warning, permission state, price, limitation, ad, required disclosure, or important control in a way that changes the claim.

Record source, author/provider, license, commercial-use permission, attribution requirement, and modification terms for every non-app font, device frame, stock image/texture, illustration, icon, and generated or third-party decorative asset. Exclude any asset whose rights cannot be verified for the intended store use.

Do not add a visible AI badge or watermark on the artwork unless current law or the platform requires it. Check Play's per-asset AI self-declaration at release time. When the user requests no AI label, default to content with documented non-AI or otherwise out-of-scope provenance rather than hiding a required declaration. Treat unresolved applicability as a policy blocker at the unsent-change stage.

Quality bar:

- a consistent visual system across the set without making every frame identical;
- clear focal point, strong hierarchy, balanced spacing, precise alignment, and intentional negative space;
- legible copy and UI at listing-preview size with sufficient contrast and safe margins;
- accurate brand colors, typography, iconography, corner treatment, and device framing;
- no accidental clipping, stretching, blur, compression artifacts, moire, inconsistent scale, mixed device families, or contradictory data;
- locally natural copy and composition for each launch locale;
- exported color profile, format, dimensions, and file size that meet current Play requirements.

Generate a deterministic contact sheet from the final exports at full size and the representative thumbnail/preview sizes observed in the current Play listing surfaces. Record caption/background contrast, smallest readable text, cropping and safe-area checks, sequence coherence, and an explicit frame-by-frame art-direction result. If the value proposition or visible UI is not understandable at preview size, revise and regenerate rather than approving by subjective full-resolution inspection.

## Truth and release gate

The ASO owner maintains `repo/play/listing/screenshots/manifest.yaml` with one record per final image: locale, form factor, frame order, source commit/version, final AAB/APK-set identity, raw capture path/hash, final export path/hash, headline, benefit/claim, deterministic transformations, rights/provenance for every non-app asset, content-level AI/authorship/edit provenance for imagery/copy/metadata/demo content, linguistic disposition, contact-sheet/art-direction disposition, and QA disposition. Other agents write separate immutable evidence; only the ASO owner merges their reviewed results before the manifest and release evidence are frozen. The coordinator validates and integrates that commit. The release agent returns immutable Play upload/status/declaration/preview evidence, and only the coordinator stores it in the release record and execution checkpoint.

QA must reject a frame when its visible feature, state, data, entitlement, device support, price, result, or claim cannot be reproduced from the recorded release candidate. The ASO gate fails when a required locale/form factor is missing, provenance is incomplete, text is unreadable, the sequence lacks a clear value story, or current Play asset validation fails.

After upload, inspect the actual Play listing preview for order, crop, locale mapping, device category, compression, and visible text. A locally polished file is not complete until the intended listing displays it correctly.
