# Android Product Pipeline skill pack

Eight focused Codex skills cover an Android product from discovery to a verified Google Play release. The pack is organized for progressive disclosure: each `SKILL.md` is a small decision router, while detailed procedures live in references that are loaded only for the relevant operation.

Invoke the complete workflow with `$android-product-pipeline`. Use a specialist directly for isolated work:

- `$mobile-ui-ux-designer` — experience and design intent;
- `$android-app-developer` — architecture and application behavior;
- `$android-ui-layout-engineer` — layout implementation and rendered comparison;
- `$android-qa-engineer` — reproducible test evidence;
- `$google-play-policy-reviewer` — current policy and disclosure review;
- `$google-play-aso-expert` — research, listing, localization, and store creatives;
- `$android-release-manager` — GitHub, signing, Fastlane, Octo, and Play delivery.

Defaults are Kotlin/Compose for greenfield apps, zero development spend, free download, no monetization, a private GitHub repository, and direct production release at 100% when Play eligibility allows it. These are defaults, not permission to contradict the user, an existing project, or current platform requirements.

End-to-end publication continues without redundant confirmation after the exact app, account, package, version, site, track, countries, and rollout are resolved. Human-only authentication, missing legal facts, signing mismatches, or mandatory Play prerequisites remain explicit blockers. Completion requires observed remote state; an AAB, upload click, or `In review` status is not a live release.

Secrets, upload keys, tokens, browser data, and private certificates never enter Git or the ZIP. Non-secret project configuration belongs in `repo/.codex/android-product.yaml`; private material stays in the system secret store or a mode-`0700` project directory.

The structure follows OpenAI’s guidance on short descriptions, conditional references, fewer prescriptive recipes, clear decision boundaries, and explicit completion criteria: [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

## Validation

Run `python3 tests/validate_pack.py`, then run `quick_validate.py` from `$skill-creator` for every skill. The local validation suite is read-only with respect to GitHub, Octo Browser, Google Sites, and Play Console.
