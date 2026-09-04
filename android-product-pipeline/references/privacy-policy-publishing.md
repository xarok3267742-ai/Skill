# Public privacy-policy publishing

Publish an app-specific policy before entering its URL in Play Console. This is a product disclosure and deployment artifact, not a mechanism for obscuring ownership. Never use hosting, domains, redirects, or browser profiles to conceal the responsible developer, evade enforcement, or make unrelated developer accounts appear independent.

## Hosting model

Prefer a user-controlled custom domain such as `privacy.example.com` because the public URL can survive a move between hosting providers or GitHub owners. Verify domain ownership before attaching it and enforce HTTPS. A custom domain improves URL portability; it does not make the publisher anonymous or eliminate provider, registrar, DNS, or legal dependencies.

If no custom domain is available, default to a dedicated public GitHub Pages repository such as `<owner>/android-app-policies`, separate from private application source. Publish each app below a stable package-scoped path such as `/apps/com.example.app/`, with locale-specific pages and a documented fallback. State clearly that the default `github.io` URL remains tied to the GitHub owner and repository.

Do not use a local file, device-hosted endpoint, temporary preview URL, URL with an access token, private Drive/document share, authenticated portal, geofenced redirect, link shortener, or app-deep-link-only page.

## Content and source of truth

Keep the canonical Markdown or static-site source in `repo/play/privacy-policy/` beside the app release. Use evidence from the tested build, SDK inventory, network behavior, product decisions, and current official policy requirements. At minimum, resolve the exact app name and package, responsible developer or legal entity, contact, effective date, collected/shared data, purposes, processors/SDK recipients, retention, security, permissions, user choices, deletion/account-deletion path, audience/children treatment, cross-border handling where relevant, and change/contact process.

Create every confirmed policy locale and a canonical fallback. Make language switching explicit and keep claims equivalent across translations. Preserve earlier revisions, effective dates, source commit, deployed commit or workflow run, and a content hash. Do not silently reuse a generic policy across apps with materially different data behavior.

## Deploy and verify

Treat creation or update of the public repository, Pages settings, DNS, and policy content as remote mutations covered by the version-specific authorization summary. Use a branch, reviewable change, and GitHub Pages deployment workflow. Do not put application secrets, analytics identifiers, browser cookies, or private contact data in the public repository. Avoid analytics and cookies unless they are necessary, disclosed, and consented to where required.

After deployment:

1. Fetch the canonical URL in a fresh unauthenticated context with no stored cookies.
2. Require HTTPS, a successful response, no account/device gate, no expiring query credential, and no unexpected redirect.
3. Verify the final page displays the exact app/package, responsible entity, approved effective date, and requested locale or fallback.
4. Compare a normalized content hash with the authorized source and record source commit, deployment commit/run, final URL, response status, redirect chain, and access time.
5. Reconcile the published text with Data safety, deletion behavior, SDK inventory, listing claims, and the release candidate before submission.

On a failed deployment, TLS/DNS uncertainty, unexpected content, or inaccessible locale, keep the Play change as a draft and stop. Never substitute an unverified URL merely to satisfy a required field.
