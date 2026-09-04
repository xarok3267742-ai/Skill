# GitHub release, AAB signing, and provenance

Current primary references:

- GitHub tag signing: https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-tags
- GitHub Actions secrets: https://docs.github.com/en/actions/reference/security/secrets
- Android app signing: https://developer.android.com/studio/publish/app-signing

Use an existing GitHub repository when specified; otherwise create a private repository within the recorded execution scope. Work on a `codex/<task-slug>` branch, push milestone commits, open a pull request, and require the agreed build, test, lint, QA, and policy gates. Squash-merge only after required checks succeed and known exceptions are recorded.

## Signing identities

Use Play App Signing with a separate upload key. Keep the upload keystore in `private/`, its passwords in Keychain, and CI copies in GitHub encrypted secrets. Restore the keystore into a runner temporary directory with restrictive permissions, build the release bundle, then remove the temporary file in an always-run cleanup step.

Create a dedicated SSH signing key for release tags when none is configured and this setup is required by the recorded release scope. Store the private key in the system key store, register the public key as a GitHub signing key, and record the public fingerprint. Never replace or rotate an existing signing identity without a separate explicit instruction.

## Workflow contract

Pin the repository's supported JDK, Gradle wrapper, Android plugin, and other build tools. The workflow must:

1. check out the exact merged commit with least privilege;
2. restore dependency caches without caching secrets;
3. run the required tests and lint for the release variant;
4. restore the upload keystore from encrypted secrets without logging it;
5. build the signed AAB and verify package ID, version, and signing certificate;
6. preserve mapping/native-symbol/baseline-profile outputs when produced;
7. calculate SHA-256 and upload artifacts with bounded retention;
8. remove temporary signing material even on failure.

After merge, create and verify an SSH-signed release tag. The tag should trigger or identify the release workflow. Download artifacts from the exact successful run, recompute checksums locally, and compare the certificate fingerprint with the approved public certificate before Play upload.

If a workflow, merge, tag, or artifact operation returns an uncertain result, query GitHub state before retrying. Do not create duplicate PRs, tags, releases, or workflow dispatches.
