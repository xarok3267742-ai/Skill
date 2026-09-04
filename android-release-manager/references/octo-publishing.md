# Google Play publishing through Octo Browser

Use the configured Octo Browser profile rather than a generic browser session. Obtain the Octo API token from the system secret store without displaying it. Resolve the exact profile ID or unique name, start it through the supported Octo API, and attach Playwright through CDP. Do not modify, export, transfer, or delete profiles.

Check the current Octo automation documentation before connecting: https://docs.octobrowser.net/en/api/start-api/

Prefer current accessible labels, roles, visible text, and DOM state over coordinates or stale selectors. Inspect the page before every transition and retain redacted evidence around important mutations.

## Identity and artifact checks

Before mutation, verify the visible Google account, Play developer account, app/package ID, version, target track, countries, rollout, and managed-publishing setting. For a new app, verify the confirmed name, default language, app/game choice, pricing model, and required declarations before creation.

Inspect the target track and App bundle explorer for the version code. Upload only the AAB downloaded from the verified GitHub run after local checksum and certificate verification. If the version already exists, reconcile it rather than uploading again.

Complete app content, reviewer access, Data safety, privacy-policy, audience/content-rating, ads, billing, pricing/distribution, listing, localization, and form-factor declarations only from confirmed facts and observed behavior. Never choose an answer for convenience.

After each create, upload, save, submit, or rollout action, inspect the visible result and record its status. On ambiguous feedback, reload or visit the canonical publication/status view before retrying.

Stop for CAPTCHA, 2FA, reauthentication, identity verification, changed terms, insufficient account permissions, unknown legal/policy answers, missing reviewer credentials, or an unrecognized console flow. Preserve the draft and state the exact action or fact needed to resume.

Report Play's actual state: draft, internal/closed testing, changes ready to send, in review, approved under managed publishing, rollout active, or available. Account testing rules or review can prevent immediate production availability even after a successful submission.
