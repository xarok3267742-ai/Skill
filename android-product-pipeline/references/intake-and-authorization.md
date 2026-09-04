# Adaptive intake and execution scope

Build on discovered facts and never make the user repeat repository information. Ask no more than three related questions at a time. Mark each value as user-stated, discovered, inferred, or unresolved. Prefer a documented reversible default over a question when the answer does not materially change the product, public identity, cost, or release target.

## Product block

Establish the product name, primary audience, user problem, success event, must-have journey, excluded scope, business model, launch deadline, and any regulated or trust-sensitive domain. Ask for examples or competitors only if the desired behavior remains ambiguous.

Ask the user to choose a development-complexity target from 0 to 10 and explain it in product terms:

- 0-2: disposable proof of concept or one-screen utility with minimal operational surface;
- 3-4: small MVP with a narrow journey and limited integrations;
- 5-6: production app with persistence, resilience, analytics, accessibility, and normal release controls;
- 7-8: complex integrations, accounts, payments, sync, offline behavior, or multiple form factors;
- 9-10: high-assurance, regulated, safety-critical, large-scale, or deeply multi-device product.

Treat the score as a scope and assurance preference, not an excuse to skip mandatory security, privacy, Play, accessibility, or signing requirements. If the requested features contradict the selected score, show the mismatch and ask which one to change.

## Octo identity block

Select the Octo profile near the beginning of intake, before requesting developer identity or contact details. List only the minimum profile identifiers needed for the user to choose; never expose cookies, tokens, or unrelated profile data. After selection, a read-only connection may inspect the signed-in Google account, Play developer display name, and existing Google Sites workspace.

Mark the observed email and developer name as discovered. Prefer a developer name and contact already published for the selected app/account in Play Console. If one unambiguous public value exists and matches the selected account, record and use it without requesting approval. Never assume that a private Google sign-in email is the support/privacy contact or that a Play display name is the legal data controller. Ask one factual question only when public identity remains ambiguous or legally material information cannot be discovered.

## Platform and experience block

Resolve phone/tablet, Android TV, Wear OS, or a combination; minimum supported devices; orientation; offline behavior; account model; accessibility constraints; brand inputs; notifications; background work; billing; ads; media; user-generated content; and third-party services. Ask conditional questions only when a feature makes them relevant.

For languages, record the default in-app locale, every supported interface/content locale, Google Play listing locales, fallback locale, whether content differs by market, and whether any locale requires RTL or specialized typography. Distinguish launch locales from later localization. Never assume that the user's conversation language is the app's default language.

## Data, policy, and review block

Record each collected/shared data type, purpose, retention, deletion path, encryption, SDK recipient, and whether collection is required or optional. Resolve permissions, target age, content rating inputs, app-access credentials for reviewers, privacy-policy URL ownership, account deletion, financial/health/children/location behavior, and any factual claims that need evidence.

For privacy-policy publication, resolve the developer or legal entity displayed on the page, public support/privacy contact, package ID, effective date, policy locales and fallback, canonical URL, and hosting ownership. Use `https://app-privacy-policy-generator.firebaseapp.com/` as a drafting aid when configured, but validate every generated statement against the tested app and current policy evidence. Do not mention the generator in the public policy. Publish through Google Sites in the selected Octo profile by default. Use a custom domain only when the user states it during intake or it is already mapped to the chosen site; otherwise use the public `sites.google.com` URL and record its dependency on the selected Google account. The page must work in a fresh unauthenticated browser without cookies, device identifiers, access tokens, private-share links, or account-specific redirects.

Never infer a legally significant declaration from silence. An unresolved declaration is a release blocker, not a default value.

## Delivery block

Resolve or discover:

- new or existing repository, GitHub owner, repository name, visibility, and default branch;
- Google Sites site/page or alternative static host, selected Octo profile, custom domain if any, canonical public URL, and publication workflow;
- application ID/package name before its first Play upload;
- Play developer account and whether the app already exists;
- Octo Browser profile ID or unique profile name and the expected Google account;
- version name/code, release notes, countries, track, rollout percentage, and managed-publishing choice;
- local project root, backup location, upload-key status, Git signing-key status, and required CI environments.

Use a private GitHub repository by default for a new project. Preserve a user-stated production target; do not silently downgrade it. If eligibility prevents production, complete every valid prerequisite and preserve the release in the furthest eligible state while recording the blocker.

## Decision record

Keep a compact decision record in `repo/docs/product-brief.md` and non-secret automation values in `repo/.codex/android-product.yaml`. Do not write secrets, passwords, recovery codes, cookies, tokens, or private keys into either file.

After research and before remote mutation, show one execution brief containing:

1. product, complexity score, form factors, languages, package ID, and selected differentiation;
2. GitHub owner/repository/visibility, branch/PR strategy, policy source path, drafting tool, Google Sites destination or alternative host, canonical policy URL, and any repository/site creation;
3. version, build variant, upload certificate, signed-tag identity, and CI secrets to configure;
4. Play developer account, app, Octo profile, track, countries, rollout, managed publishing, and declarations to submit;
5. exact external actions, including public policy publication, and any irreversible consequences.

The execution brief is an informational record, not an approval screen. Do not ask the user to confirm it or reply with phrases such as “publish the site?”, “upload/send the app to Google Play?”, “start the release?”, or “continue?”. Record the originating task instruction, intake answers, resolved scope, assumptions, desired terminal outcome, and timestamp, then continue immediately through site publication, AAB upload, Play submission, and the configured rollout. The scope is app- and version-specific and does not authorize future releases, other repositories, other Play accounts, key replacement, deletion, unpublishing, or unrelated console changes. Ask only for a missing fact that is both undiscoverable and outcome-changing; phrase it as one precise factual question, not an approval request.
