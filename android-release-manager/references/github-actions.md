# GitHub, CI, and signing

Check the current official signing and secrets documentation before setup:

- https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-tags
- https://docs.github.com/en/actions/reference/security/secrets
- https://developer.android.com/studio/publish/app-signing

## Repository workflow

Use the user-selected existing repository or create a private GitHub repository inside the recorded release scope. Work on a `codex/<task-slug>` branch, push coherent commits, open a pull request, and require the agreed build, test, lint, QA, and policy checks. Squash-merge only after required checks pass and exceptions are recorded.

For release tags, use a dedicated SSH signing key. Keep its private key in the system key store and register only the public signing key in GitHub. Verify the tag signature locally and its expected GitHub verification state before using it as release provenance. Key creation and public-key registration may proceed automatically when required by the explicit release request; key replacement or rotation requires a separate explicit instruction.

## Upload key and CI secrets

Prefer Play App Signing with a separate upload key. Store the local keystore outside the Git tree with restrictive permissions and an encrypted backup. Use these standard GitHub Actions secret names unless the repository already has documented equivalents:

- `ANDROID_SIGNING_KEY_BASE64`
- `ANDROID_KEYSTORE_PASSWORD`
- `ANDROID_KEY_ALIAS`
- `ANDROID_KEY_PASSWORD`

Transmit secret values via protected stdin/environment mechanisms. Never pass them on a command line, print them, persist them in caches, or include them in artifacts.

## Release workflow requirements

The workflow must use least privileges and the repository's pinned tools. It must run tests and lint, restore the upload keystore into a runner temporary directory, build the signed AAB, verify package/version/certificate, compute SHA-256, retain relevant mapping/native-symbol/baseline-profile files, upload bounded-retention artifacts, and delete temporary signing material in an always-run cleanup step.

Tag or dispatch the workflow exactly once. After it succeeds, download the artifact from that run, recompute SHA-256 locally, and verify the upload certificate against the approved public fingerprint. A locally rebuilt AAB is not interchangeable with the CI artifact unless its provenance is separately approved.

If GitHub returns an uncertain result for repository creation, push, PR, merge, tag, secret update, dispatch, or artifact download, query the corresponding API/state before retrying.
