---
name: google-play-policy-reviewer
description: Audit an Android build and Play configuration for current policy and disclosure risks. Use before release or when resolving a specific Play compliance issue.
---

# Google Play Policy Reviewer

Produce an evidence-backed preflight, not legal certification or an approval guarantee. Identify the exact build, package, form factors, markets, languages, audience, accounts, SDKs, permissions, data behavior, monetization, and listing claims.

Read [live policy check](references/live-policy-check.md) for a release review or any rule that may have changed; use current official Google Play and Android sources and record URL plus access date. Read [review format](references/review-format.md) when reporting findings.

Reconcile code and runtime behavior with manifests, SDK/data flows, privacy policy, Data safety, consent/deletion, reviewer access, payments/ads, target audience, screenshots, metadata, and form-factor declarations. Inspect configuration or runtime evidence before attributing behavior to an SDK.

Under the default `store_pricing: free` and `monetization: none` contract, any paid download, product, subscription, paywall, donation, or advertising surface is a release-blocking mismatch unless the project contract explicitly says otherwise. Free pricing does not imply no data collection.

Verify the canonical privacy-policy URL over unauthenticated HTTPS and its consistency with the exact app, responsible developer, retention, deletion, recipients, and markets. Treat generator output as a draft. Do not conceal developer identity, app relationships, generated/edited asset origin, or required declarations. If an AI/content declaration is required, answer truthfully or replace the asset; unresolved applicability blocks submission.

Classify each item as confirmed mismatch, likely risk, missing evidence, or recommendation and cite the controlling rule. Never choose a declaration merely to unblock release. This skill is review-only; return Console changes to the `$android-release-manager` release owner.
