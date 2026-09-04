# Autonomous execution, recovery, and completion

Use this contract for every end-to-end build or release so the workflow survives pauses, context compaction, CI latency, browser timeouts, and ambiguous remote responses.

## Scope and initiative

An explicit instruction to use `$android-product-pipeline` to build, release, publish, ship, or finish an app, together with the user's questionnaire answers, authorizes ordinary in-scope operations required for that app/version. Do not request a second approval for the execution brief, branch, PR, CI run, encrypted-secret setup, Google Sites publication, AAB upload, Play submission, or configured rollout. Preflight identity, artifact, and destination checks are internal verification steps, not reasons to ask whether the already-authorized action should be performed.

Infer routine reversible details from repository conventions, existing Play configuration, and the safest consistent default. Record each inference. Ask only when a fact is undiscoverable and choosing it would materially change public identity, legal declarations, cost, destructive behavior, the destination account, or the intended release result. A question for a missing fact is not a confirmation gate.

Do not extend this authority to deleting or overwriting unrelated resources, replacing/rotating keys, changing ownership, unpublishing, switching developer accounts, accepting new legal terms, or operating a different app/version.

## Desired outcome

Record one terminal outcome before implementation:

- `aab-ready`: verified signed CI artifact is downloaded with matching commit, version, certificate, and SHA-256.
- `aab-uploaded`: `aab-ready`, and the exact version code is observed in the intended Play app's App bundle explorer.
- `play-submitted`: `aab-uploaded`, and the intended track release is observed as sent for review, in review, approved under managed publishing, rollout active, or available rather than draft/unsent.
- `play-available`: all prior criteria, and Play reports the release available or the configured rollout active for the requested countries/form factors.

If the user says to do everything, publish, or finish the full pipeline without narrowing the goal, use `play-available`. Never reinterpret `in review` as `play-available`.

## Persistent checkpoint

Create `artifacts/pipeline-state.yaml` before the first implementation mutation. It contains no secrets and records at least:

```yaml
schema_version: 1
app_id: "com.example.app"
version_code: 1
desired_outcome: "play-available"
phase: "research"
status: "in_progress"
last_verified_at: "ISO-8601 timestamp"
milestones:
  research: {status: "in_progress", evidence: []}
  design: {status: "pending", evidence: []}
  implementation: {status: "pending", evidence: []}
  qa_policy_aso: {status: "pending", evidence: []}
  github_merge_tag: {status: "pending", evidence: []}
  ci_aab: {status: "pending", evidence: []}
  privacy_policy: {status: "pending", evidence: []}
  play_upload: {status: "pending", evidence: []}
  play_submission: {status: "pending", evidence: []}
  play_availability: {status: "pending", evidence: []}
blocker: null
```

Update a milestone only after observing evidence such as a commit SHA, PR state, workflow run ID/conclusion, artifact checksum/certificate, public policy URL/content hash, Play version code, track release ID, or visible Console status. A planned action, local file, dispatched workflow, button click, toast, navigation, or assistant statement is not evidence of completion.

## Resume loop

At the start of every continuation or after any interruption:

1. Read `repo/.codex/android-product.yaml`, the checkpoint, and the latest release record.
2. Inspect local Git plus the configured GitHub repository, workflow runs/artifacts, public policy URL, and Play Console state relevant to the current milestone.
3. Reconcile stale or ambiguous checkpoint entries with observed remote state; remote evidence wins.
4. Select the earliest unmet quality gate and continue automatically, including from policy publication into Play upload/submission without pausing for consent already supplied by the end-to-end request.
5. After every state-changing request, re-read the canonical remote state before advancing or retrying.

Never mark the workflow complete merely because a package exists locally or appears in a prior message. For `aab-uploaded` or any Play outcome, inspect the intended developer account/app and observe the exact version code. For submission/availability, also inspect the intended track, countries, rollout, and status.

## Waiting and blockers

Wait for active CI, upload processing, and short remote transitions using bounded polling with backoff. When Google review is the only remaining step for `play-available` and a recurring monitoring mechanism is available, create a quiet monitor that checks the same app/version/track and reports only a meaningful change, completion, failure, or required user action. Keep the checkpoint incomplete while review is pending.

CAPTCHA, 2FA, reauthentication, identity verification, unavailable permissions, changed legal terms, an unknown legally significant declaration, or a signing-identity mismatch requires the user or new authority. Preserve all completed work, write the exact page/state and single required action into `blocker`, and ask only for that action or fact. A blocker is not successful completion.

## Final audit

Before the final response, re-read every terminal condition from its authoritative surface. Set `status: complete` only when all criteria for `desired_outcome` are observed. Report exact remote status, identifiers, URLs, checksums, and any pending external review. If the goal is not satisfied, continue or report the blocker; never end with an offer to continue or a claim that the local build means the package is on the account.
