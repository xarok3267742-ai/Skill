# Android Product Pipeline skill pack

Eight Codex skills form a multi-agent Android pipeline for product discovery, competitor research, UI/UX, Android layout engineering, Kotlin/Compose implementation, QA, Google Play policy and ASO review, production-grade truthful store screenshots, GitHub delivery, signed AAB builds, public privacy-policy deployment, and idempotent release through an authorized Octo Browser profile.

## Skills

- `android-product-pipeline` — end-to-end orchestrator
- `android-app-developer` — phone, tablet, Android TV, and Wear OS implementation
- `mobile-ui-ux-designer` — implementation-ready flows and design systems
- `android-ui-layout-engineer` — precise adaptive layout implementation and rendered visual verification
- `android-qa-engineer` — test strategy and release evidence
- `google-play-policy-reviewer` — current policy and declaration review
- `google-play-aso-expert` — competitor research, listing, localization, and creatives
- `android-release-manager` — GitHub, CI, signing, policy deployment, Octo, and Play release

Invoke the full workflow explicitly with `$android-product-pipeline`. The orchestrator creates bounded specialist agents, parallelizes independent research and review, isolates or serializes overlapping edits, and gives one release agent exclusive ownership of GitHub/Sites/Play mutations. Repeatable AAB, metadata, screenshot, and track delivery uses pinned Fastlane after one-time Play initialization; Octo handles bootstrap, declarations, Google Sites, and final verification. Full publication defaults to production at 100% without optional Play testing tracks, while CI/QA remains mandatory; account-specific testing requirements imposed by Play are never bypassed. The intake is adaptive and includes development complexity from 0 through 10, interface/content/listing languages, privacy-policy hosting, GitHub, Play Console, Octo profile, release parameters, and the desired terminal outcome. An explicit end-to-end request plus intake answers drives autonomous execution without a separate confirmation gate; human-only challenges and missing legal facts remain blockers.

## Security boundary

The pack contains no credentials. Application source stays in a private GitHub repository by default. Upload keystores and local private files stay outside Git in a mode-`0700` directory; passwords, signing credentials, and the Octo API token belong in macOS Keychain or the active platform secret store. Only public certificates and non-secret Keychain entry locators may be committed.

Privacy-policy drafts can be prepared through the configured App Privacy Policy Generator, then reviewed against the app and stored with its source. The public policy does not name the drafting tool. Publication uses Google Sites in the selected Octo profile by default and must produce a public, app-specific HTTPS page requiring no login or device-bound session. A user-controlled custom domain is preferred for URL portability; GitHub Pages or another static host is a fallback. Policies must transparently identify the confirmed responsible developer or legal entity and must not be used to conceal ownership or evade platform enforcement.

## Validate

Run `tests/validate_pack.py`, then run the official `quick_validate.py` from Codex's `skill-creator` skill against every skill directory in an isolated environment with PyYAML installed. Forward-test contracts are listed in `tests/scenarios.md` and must not mutate a real GitHub repository or Play Console.
