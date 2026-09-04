# Visual and form-factor verification

## Capture controls

Compare like with like: same build, viewport, density, font scale, locale, theme, system-bar mode, content, animation state, and keyboard visibility. Disable or stabilize clocks, remote images, cursors, asynchronous placeholders, and animations where possible. Record the commit, variant, device or emulator profile, Android version, and capture command with the evidence.

## Comparison methods

1. Side-by-side view for hierarchy and large structural differences.
2. Semi-transparent overlay for anchor, baseline, size, and spacing drift.
3. Pixel diff for deterministic regions after masking unavoidable dynamic content.

Do not judge only from a global similarity percentage; a small error on a primary control can matter more than a large background difference. Do not invent a universal pixel threshold when the specification provides none.

## Form-factor checks

- Phone/tablet/foldable: test compact and expanded widths, rotation or posture where supported, multi-pane behavior, cutouts, edge-to-edge content, and keyboard/IME resizing.
- Android TV: test D-pad reachability, initial and restored focus, clear focus indication, overscan-safe composition where relevant, long-distance legibility, dialogs, media controls, and Back behavior without touch assumptions.
- Wear OS: test round and square screens, chin or inset behavior, edge clipping, scaling text, rotary scrolling, short interactions, tiles or complications when present, and ambient mode where supported.
- Localization: render real strings for all launch locales, including long expansion, mixed-direction text, RTL mirroring, locale-specific numerals, and supported scripts/fonts.
- Accessibility: check enlarged fonts and display size, minimum targets, labels, roles, state announcements, traversal/focus order, contrast, and non-color cues.

## Acceptance checklist

- Shared left and right anchors coincide across related elements.
- Repeated component dimensions and internal gaps are identical unless a documented variant applies.
- Icon artwork appears optically centered, not merely its asset canvas.
- Text baselines, line height, weight, wrapping, truncation, and maximum lines match the specification.
- System bars, cutouts, gesture area, and keyboard do not double-shift content.
- Long content cannot overlap, clip, or unpredictably push primary controls.
- Touch, remote-focus, and rotary targets remain usable even when visible artwork is small.
- Every required screen state can be rendered deterministically for inspection.
- Differences from the reference are either removed or documented with a reason.

When exact numerical tolerances are not supplied, require no visible misalignment at normal inspection and no structural drift in the verification matrix. A passing compile or preview is not rendered visual evidence.
