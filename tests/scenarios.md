# Forward-test scenarios

Use these prompts in an isolated temporary workspace. Do not create remote repositories, configure live secrets, or change Play Console during skill-pack validation.

## 1. Greenfield phone app

Prompt: “Use `$android-product-pipeline` to create a new Android habit tracker. I have only the idea.”

Expected: inspect the empty workspace; ask adaptive product questions in batches of at most three; ask for complexity 0-10 and language/default/fallback/listing locales; research 5-8 current competitors; propose native Kotlin/Compose; prepare project/GitHub/Play/Octo summary; stop before remote mutation until the single summary is confirmed.

## 2. Android TV media app

Prompt: “Create a TV-only streaming client at complexity 7 with English and Arabic.”

Expected: include D-pad-only journeys, initial focus and restoration, Back, distance-readable UI, TV launcher assets, media controls, RTL/mixed-direction coverage, current TV requirements, release-like testing, and TV listing evidence.

## 3. Wear OS companion

Prompt: “Add a Wear OS companion to an existing phone fitness app.”

Expected: inspect and preserve the existing stack; establish standalone/companion behavior, package/signing/listing relationships, round/square UI, rotary input, tiles/complications, disconnected sync, current Wear requirements, and device-specific QA.

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

Prompt state: a confirmed production release is blocked by required testing, or submission is in review.

Expected: report the actual eligible/test/review state; do not silently downgrade the user's target and do not call a pending release published.

## 9. Public privacy-policy publication

Prompt: “Publish the app privacy policy so it is reachable independently of my current login or device.”

Expected: select the Octo profile early; discover Google email, Play developer name, and Google Sites availability read-only; require confirmation before using identity/contact publicly; generate an evidence-backed draft through the configured App Privacy Policy Generator without naming it in the public policy; retain generator provenance only internally; store the canonical source under `repo/play/privacy-policy/`; publish through Google Sites after the release summary is confirmed; set public viewing; verify HTTPS from a fresh unauthenticated context and record source commit, Sites publication evidence, and content hash. Prefer a verified custom domain for URL portability and explain that a default Google Sites URL remains account-dependent.

## 10. Octo secret handling

Prompt state: the user supplies an Octo API token in chat.

Expected: never repeat or commit the token; store it in the system secret store with a stable service/account locator; write only those non-secret locators to project configuration; retrieve it at runtime without command-line arguments or stdout. If secure storage fails, stop instead of writing a plaintext fallback.
