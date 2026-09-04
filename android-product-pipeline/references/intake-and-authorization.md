# Adaptive intake and release authorization

Build on discovered facts and never make the user repeat repository information. Ask no more than three related questions at a time. Mark each answer as confirmed, discovered, assumed, or unresolved.

## Product block

Establish the product name, primary audience, user problem, success event, must-have journey, excluded scope, business model, launch deadline, and any regulated or trust-sensitive domain. Ask for examples or competitors only if the desired behavior remains ambiguous.

Ask the user to choose a development-complexity target from 0 to 10 and explain it in product terms:

- 0-2: disposable proof of concept or one-screen utility with minimal operational surface;
- 3-4: small MVP with a narrow journey and limited integrations;
- 5-6: production app with persistence, resilience, analytics, accessibility, and normal release controls;
- 7-8: complex integrations, accounts, payments, sync, offline behavior, or multiple form factors;
- 9-10: high-assurance, regulated, safety-critical, large-scale, or deeply multi-device product.

Treat the score as a scope and assurance preference, not an excuse to skip mandatory security, privacy, Play, accessibility, or signing requirements. If the requested features contradict the selected score, show the mismatch and ask which one to change.

## Platform and experience block

Confirm phone/tablet, Android TV, Wear OS, or a combination; minimum supported devices; orientation; offline behavior; account model; accessibility constraints; brand inputs; notifications; background work; billing; ads; media; user-generated content; and third-party services. Ask conditional questions only when a feature makes them relevant.

For languages, record the default in-app locale, every supported interface/content locale, Google Play listing locales, fallback locale, whether content differs by market, and whether any locale requires RTL or specialized typography. Distinguish launch locales from later localization. Never assume that the user's conversation language is the app's default language.

## Data, policy, and review block

Record each collected/shared data type, purpose, retention, deletion path, encryption, SDK recipient, and whether collection is required or optional. Confirm permissions, target age, content rating inputs, app-access credentials for reviewers, privacy-policy URL ownership, account deletion, financial/health/children/location behavior, and any factual claims that need evidence.

For privacy-policy publication, confirm the developer or legal entity displayed on the page, public support/privacy contact, package ID, effective date, policy locales and fallback, canonical URL, and hosting ownership. Ask whether the user controls a custom domain. Prefer that domain for a portable URL; otherwise use a dedicated public GitHub Pages policy repository and state that its default URL remains dependent on the GitHub owner. The page must work in a fresh unauthenticated browser without cookies, device identifiers, access tokens, private-share links, or account-specific redirects.

Never infer a legally significant declaration from silence. An unresolved declaration is a release blocker, not a default value.

## Delivery block

Confirm or discover:

- new or existing repository, GitHub owner, repository name, visibility, and default branch;
- dedicated privacy-policy repository or static host, custom domain if any, canonical public URL, and deployment branch/workflow;
- application ID/package name before its first Play upload;
- Play developer account and whether the app already exists;
- Octo Browser profile ID or unique profile name and the expected Google account;
- version name/code, release notes, countries, track, rollout percentage, and managed-publishing choice;
- local project root, backup location, upload-key status, Git signing-key status, and required CI environments.

Use a private GitHub repository by default for a new project. Use an internal or closed track only when selected by the user or required by Play eligibility; do not silently downgrade a confirmed production request.

## Decision record

Keep a compact decision record in `repo/docs/product-brief.md` and non-secret automation values in `repo/.codex/android-product.yaml`. Do not write secrets, passwords, recovery codes, cookies, tokens, or private keys into either file.

After research and before remote mutation, show one summary containing:

1. product, complexity score, form factors, languages, package ID, and selected differentiation;
2. GitHub owner/repository/visibility, branch/PR strategy, policy source/deployment repository, canonical policy URL, and any repository creation;
3. version, build variant, upload certificate, signed-tag identity, and CI secrets to configure;
4. Play developer account, app, Octo profile, track, countries, rollout, managed publishing, and declarations to submit;
5. exact external actions, including public policy publication, and any irreversible consequences.

Ask for one explicit confirmation of this summary. Record its scope and timestamp in the release record. The confirmation is version-specific and does not authorize future releases, other repositories, other Play accounts, key replacement, deletion, unpublishing, or unrelated console changes.
