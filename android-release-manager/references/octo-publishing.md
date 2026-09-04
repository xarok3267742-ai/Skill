# Google Play publishing through Octo Browser

Use the configured Octo Browser profile rather than a generic browser session. Obtain the Octo API token from the system secret store without displaying it. On macOS, resolve the configured Keychain service/account entry at runtime; never place its value in project YAML, repository files, shell arguments, screenshots, browser code, or logs. Resolve the exact profile ID or unique name, start it through the supported Octo API, and attach Playwright through CDP. Do not modify, export, transfer, or delete profiles.

Check the current Octo automation documentation before connecting: https://docs.octobrowser.net/en/api/start-api/

Prefer current accessible labels, roles, visible text, and DOM state over coordinates or stale selectors. Inspect the page before every transition and retain redacted evidence around important mutations.

## Generate and publish the policy

Near the beginning of intake, use the selected profile read-only to discover the visible Google account email, Play developer display name, existing public developer contact, and Google Sites availability. Prefer unambiguous values already published for the selected Play developer. Do not infer a public contact or legal identity from a private account alone; ask for the missing fact only when it cannot be discovered safely.

Within the recorded release scope, open `https://app-privacy-policy-generator.firebaseapp.com/` in that profile, populate only verified public identity and evidence-backed app/data fields, and export a draft. Never put credentials, unpublished personal data, or guessed declarations into the generator. Review and normalize the result in the app repository; the public policy must not mention the generator. If removing supplied attribution would conflict with current terms or licensing, create independent policy text from verified facts instead.

Open Google Sites in the same selected profile. Reconcile an existing site/page for the package before creating a new one, preview changes, publish the reviewed locale pages, and set the published site to public viewing. Do not pause after preview or ask whether to publish. Use a custom domain when it is part of the recorded scope; otherwise retain the exact `sites.google.com` URL and state its account dependency in the release record. Re-open the public URL in a fresh unauthenticated context, compare its content hash, and continue directly to Play Console without requesting approval already granted by the end-to-end task. On CAPTCHA, 2FA, identity mismatch, unavailable Sites permissions, unexpected sharing restrictions, or uncertain publication state, preserve the draft and stop.

## Identity and artifact checks

Before mutation, verify the visible Google account, Play developer account, app/package ID, version, target track, countries, rollout, and managed-publishing setting. For a new app, verify the confirmed name, default language, app/game choice, pricing model, and required declarations before creation.

Inspect the target track and App bundle explorer for the version code. Upload only the AAB downloaded from the verified GitHub run after local checksum and certificate verification. If the version already exists, reconcile it rather than uploading again.

Before entering the privacy-policy field, verify that the approved canonical URL resolves over HTTPS without authentication, cookies, device binding, or expiring parameters and that its content names the exact app/package and responsible developer/legal entity. Complete app content, reviewer access, Data safety, privacy-policy, audience/content-rating, ads, billing, pricing/distribution, listing, localization, and form-factor declarations only from confirmed facts and observed behavior. Never choose an answer for convenience.

After each create, upload, save, submit, or rollout action, inspect the visible result and record its status. On ambiguous feedback, reload or visit the canonical publication/status view before retrying. When preflight values match the recorded scope, upload, submit, and roll out immediately; never replace execution with a yes/no confirmation question.

Stop for CAPTCHA, 2FA, reauthentication, identity verification, changed terms, insufficient account permissions, unknown legal/policy answers, missing reviewer credentials, or an unrecognized console flow. Preserve the draft and state the exact action or fact needed to resume.

Report Play's actual state: draft, internal/closed testing, changes ready to send, in review, approved under managed publishing, rollout active, or available. Account testing rules or review can prevent immediate production availability even after a successful submission.
