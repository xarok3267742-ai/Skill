# Android skill-pack contributor instructions

This repository contains reusable Codex skills, not an Android application.

- Keep every frontmatter description short and specific enough to prevent accidental activation.
- Keep each root `SKILL.md` as the smallest useful router. Put operation-specific procedures in a focused reference and link it at the point where it becomes relevant.
- Maintain one source of truth for each rule. Remove duplicate guidance instead of strengthening both copies.
- Preserve the eight skill names, automatic discovery, security boundary, explicit end-to-end authorization, and evidence-based completion contract unless the user changes them.
- Match detail to risk: be strict about credentials, signing, account identity, legal declarations, irreversible mutations, and idempotent retries; leave ordinary implementation choices to the executing agent.
- Do not require reading unrelated references before a small edit.
- Never add credentials, tokens, keystores, browser profiles, private certificates, or real account data to the repository, logs, fixtures, or archive.

The validation commands use local disposable inputs and have no production access. Run `python3 tests/validate_pack.py` and the `$skill-creator` `quick_validate.py` checks after relevant edits, fix failures caused by the change, and rerun the affected checks without asking for approval. Scenario tests must not mutate GitHub, Octo Browser, Google Sites, or Play Console.
