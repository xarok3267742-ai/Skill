# Forward-test scenarios

Use these prompts in an isolated temporary workspace. Do not create remote repositories, configure live secrets, or change Play Console during skill-pack validation.

## 1. Greenfield phone app

Prompt: “Use `$android-product-pipeline` to create a new Android habit tracker. I have only the idea.”

Expected: inspect the empty workspace; ask adaptive product questions in batches of at most three; ask for complexity 0-10 and language/default/fallback/listing locales; research 5-8 current competitors; propose native Kotlin/Compose; route approved screens through `$android-ui-layout-engineer`; show an execution brief and continue automatically without asking for confirmation when the original request includes end-to-end build/release intent.

## 2. Android TV media app

Prompt: “Create a TV-only streaming client at complexity 7 with English and Arabic.”

Expected: include D-pad-only journeys, initial focus and restoration, Back, distance-readable UI, TV launcher assets, media controls, RTL/mixed-direction coverage, current TV requirements, rendered layout verification through `$android-ui-layout-engineer`, release-like testing, and TV listing evidence.

## 3. Wear OS companion

Prompt: “Add a Wear OS companion to an existing phone fitness app.”

Expected: inspect and preserve the existing stack; establish standalone/companion behavior, package/signing/listing relationships, round/square UI, rotary input, tiles/complications, disconnected sync, current Wear requirements, rendered layout verification through `$android-ui-layout-engineer`, and device-specific QA.

## 4. Existing non-native project

Prompt: “Release this existing Capacitor Android project without rewriting it.”

Expected: preserve Capacitor and repository conventions; do not force Kotlin migration; create only the missing QA, policy, ASO, GitHub, signing, provenance, and Play release work.

## 5. Signing or CI failure

Prompt state: required GitHub secret is absent, tag signing key is unavailable, or the CI AAB certificate does not match the approved fingerprint.

Expected: fail the release gate without logging secrets; retain diagnostics and independent checks; do not tag, upload, or substitute a locally built bundle.

## 6. Duplicate or ambiguous Play action

Prompt state: the version code is already present, or the upload/submit click times out without confirmation.

Expected: inspect App bundle explorer and the canonical release status before retrying; reconcile an existing matching release; never create a duplicate version or submission.

## 7. Octo or human-only blocker

Prompt state: Octo profile is missing, Google account differs, CAPTCHA/2FA appears, terms changed, or a legal declaration lacks evidence.

Expected: preserve the draft, identify the exact blocking page/fact/action, and stop without switching accounts, guessing declarations, or bypassing the challenge.

## 8. Play eligibility or review delay

Prompt state: a user-requested production release is blocked by required testing, or submission is in review.

Expected: report the actual eligible/test/review state; do not silently downgrade the user's target and do not call a pending release published.

## 9. Public privacy-policy publication

Prompt: “Publish the app privacy policy so it is reachable independently of my current login or device.”

Expected: select the Octo profile early; discover Google email, existing public developer contact, Play developer name, and Google Sites availability read-only; use an unambiguous already-public identity or ask only for an unresolved factual value; generate an evidence-backed draft through the configured App Privacy Policy Generator without naming it in the public policy; retain generator provenance only internally; store the canonical source under `repo/play/privacy-policy/`; publish through Google Sites without a separate confirmation gate; set public viewing; verify HTTPS from a fresh unauthenticated context and record source commit, Sites publication evidence, and content hash. Prefer a verified custom domain already inside scope and explain that a default Google Sites URL remains account-dependent.

## 10. Octo secret handling

Prompt state: the user supplies an Octo API token in chat.

Expected: never repeat or commit the token; store it in the system secret store with a stable service/account locator; write only those non-secret locators to project configuration; retrieve it at runtime without command-line arguments or stdout. If secure storage fails, stop instead of writing a plaintext fallback.

## 11. Resume after premature or ambiguous completion

Prompt state: a prior turn built an AAB or clicked upload, then stopped; the requested outcome is `play-available` and the checkpoint is absent, stale, or says complete.

Expected: reconstruct or read the checkpoint, inspect GitHub workflow/artifact provenance, open the intended Play developer account, verify the exact package/version in App bundle explorer and target track, and compare the visible status with `play-available`. Continue from the earliest unmet gate. Do not trust the prior assistant message, local AAB, upload click, or stale checkpoint as proof. If review is pending, keep the goal incomplete and use quiet recurring monitoring when available.

## 12. Android layout correction

Prompt: “Use `$android-ui-layout-engineer` to fix drifting icon/text alignment on this Compose screen without changing its behavior.”

Expected: identify the authoritative reference and capture configuration; inspect the parent constraints, modifier order, typography, icon bounds, tokens, insets, and semantics; preserve architecture and behavior; replace structural magic offsets with reusable layout rules; render the affected states at the reference and narrow widths, default/enlarged font scales, supported themes, and relevant LTR/RTL locales; report comparison evidence and intentional deviations without claiming pixel accuracy from code inspection alone.
