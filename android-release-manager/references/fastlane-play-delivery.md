# Fastlane delivery to Google Play

Use Fastlane `supply` as the default repeatable delivery path for an existing Play application when Google Play Developer API access is configured. Check the current official documentation at execution time:

- https://docs.fastlane.tools/actions/upload_to_play_store/
- https://developers.google.com/android-publisher/getting_started

Fastlane can upload AABs, release notes, metadata, images, screenshots, mappings, tracks, and rollouts, and can read track version codes. It does not replace Play Console for creating and manually initializing a new app, completing app-content/Data safety/content-rating declarations, accepting terms, handling eligibility, or visually confirming final listing and release state. Current Fastlane documentation requires at least one build to be uploaded manually before `supply` is used for that app; use the selected Octo profile for that bootstrap and then switch routine delivery to Fastlane.

## Repository contract

Commit the automation, never credentials:

```text
repo/
|-- Gemfile
|-- Gemfile.lock
`-- fastlane/
    |-- Appfile
    |-- Fastfile
    `-- metadata/android/
        `-- <locale>/
            |-- title.txt
            |-- short_description.txt
            |-- full_description.txt
            |-- changelogs/<versionCode>.txt
            `-- images/
                |-- phoneScreenshots/
                |-- sevenInchScreenshots/
                |-- tenInchScreenshots/
                |-- tvScreenshots/
                `-- wearScreenshots/
```

Pin Fastlane and its transitive dependencies with `Gemfile.lock` and invoke it through `bundle exec fastlane`. Keep package, metadata path, track, release status, rollout, and skip/sync behavior explicit in the lane. Screenshot filenames must have deterministic alphanumeric order; a complete intended screenshot set is required because `supply` replaces existing listing images rather than appending to them.

Separate validation, binary, metadata, screenshot, and promotion operations into idempotent lanes or explicit parameters. This lets a failed metadata update be retried without uploading a second binary and lets a binary reconciliation avoid replacing screenshots.

## API identity and credentials

Use a dedicated Google service account with only the Play permissions required for the recorded app and release operations. Reuse a matching account when one exists. When API setup is inside the explicit end-to-end scope and the selected Cloud project/developer account is unambiguous, configure it without a redundant confirmation; an unresolved destination project or permission grant is a factual blocker, not a yes/no release gate.

Prefer GitHub Actions OIDC with Google Workload Identity Federation and Application Default Credentials. Restrict the workload identity provider by repository owner, exact repository, protected ref/environment, and any other supported claims needed to prevent forks or unrelated workflows from impersonating the release service account. Grant `id-token: write` only to the release job and keep all Google/Play permissions least-privilege.

Use a service-account JSON key only as a fallback when WIF is unavailable. Store it in the platform secret store and the GitHub encrypted secret `GOOGLE_PLAY_SERVICE_ACCOUNT_JSON`, or a documented repository-specific equivalent, with an owner and rotation/revocation procedure. Configuration may contain only the secret name, never JSON content. In CI, write it from a protected environment variable to a runner temporary file, pass only that file path to Fastlane, and delete it in an always-run cleanup step. Never use `json_key_data` in a command, log, artifact, cache, or repository file.

Validate the credential against the expected package/account with Fastlane's key-validation action or a read-only API call before release. A credential that can access an unexpected developer account does not authorize switching targets.

## Idempotent lane sequence

1. Verify the expected account/app/package and production eligibility in Play Console through the selected Octo profile. For a new app, complete the one-time app creation, declarations, and first manual build upload required before `supply`. When eligible and the release brief does not request staging, target production directly rather than creating an optional testing release.
2. Read target-track version codes and release names through Fastlane/Google Play Developer API, then reconcile the exact version in App bundle explorer. Do not upload when the version already exists unless the observed artifact/release is the intended one and only metadata remains.
3. Validate repository metadata, complete screenshot set, locale directories, release notes, AAB certificate/checksum/provenance, and current Play constraints locally.
4. Run `supply` with `validate_only` for the intended change set. Validation success is not publication evidence.
5. Upload metadata and the complete screenshot/image set without the AAB using the relevant skip flags plus `changes_not_sent_for_review: true`. Use `sync_image_upload` only after current Fastlane behavior and the intended replacement set have been verified. Treat these as unsent listing changes.
6. Open Play Console through Octo, reconcile every newly introduced asset and its content-level provenance, complete any required per-asset declaration, and verify the saved unsent state. Fastlane must not infer or bypass Console-only declarations.
7. Only after declarations and listing/policy checks pass, execute the binary-only non-interactive lane exactly once using the exact AAB from the verified GitHub run and the recorded package, production track, `release_status`, rollout, and mapping/symbols while skipping already-reconciled metadata, images, and screenshots.
8. Re-read version codes and track state through the API. If Fastlane exits ambiguously, do not rerun; inspect the canonical API state and Play Console first.
9. Open the actual Play listing and release pages through Octo to verify screenshot order/crop/locale/device category, version code, track, countries, rollout, declarations, and status. API success alone is not `play-available`.

Use skip flags deliberately on retries so already-reconciled AAB, metadata, changelogs, images, or screenshots are not resent. Never run two Fastlane release lanes or a Fastlane lane and browser upload concurrently for the same app/version.

Default to `track: production`, `release_status: completed`, and rollout `1.0` only when those values match the recorded release brief and Play reports production access. A validation-only Fastlane call is a preflight, not a testing-track release. Do not create internal/closed/open releases merely as an agent preference. Platform-mandated closed testing and production-access applications cannot be bypassed or truthfully replaced with automation-only activity. If the user prohibited testing tracks, retain the production-ready artifact/draft and stop on the eligibility blocker instead of creating the mandatory closed release.

## AI-asset declarations

Do not add a visible “AI-generated” badge, watermark, or marketing disclaimer unless the current platform flow or applicable law requires it. Pixel provenance alone is insufficient: record whether every submitted image/video, caption, metadata field, visible demo-content element, and non-app artwork was AI-generated, AI-edited, AI-assisted, human-authored, or deterministically derived, including its source and transformation history. Deterministically recreating an AI concept does not automatically make its content out of scope.

When the user requires store assets without AI labeling, use `$imagegen` only for private exploration and prefer submitted content with evidence that it falls outside current labeling requirements. Before submission, inspect the current asset-specific AI self-declaration flow in Play Console, applicable law, and the content-level provenance manifest. If submitted content falls within a required declaration, declare it truthfully or replace it; if applicability cannot be resolved, stop at the unsent-change stage as a policy blocker. Do not suppress, falsify, or automate an unsupported answer. Fastlane upload does not remove the need to complete or verify declarations in Play Console.
