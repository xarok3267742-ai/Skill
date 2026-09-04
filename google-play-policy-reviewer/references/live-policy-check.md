# Live Google Play policy check

Do not rely on memorized target SDK values, form-field wording, deadlines, testing eligibility, or form-factor requirements. Before a release, search and open current official Google Play Help, Play policy, and Android developer pages relevant to the app. Record URL, access date, effective date when stated, and the exact product behavior to which the rule applies.

At minimum, determine whether current rules affect:

- target API, 64-bit and page-size support, AAB, Play App Signing, and developer verification;
- new personal-account testing or production-access eligibility;
- permissions, foreground services, background location, photos/videos, notifications, accessibility, VPN, device administration, and exact alarms;
- Data safety, privacy policy, consent, retention, account creation/deletion, reviewer access, and user-data deletion;
- billing, subscriptions, ads, families/children, health, finance, gambling, UGC, AI-generated content, and intellectual property;
- Android TV, Wear OS, watch face, phone/tablet, and multi-device packaging/listing requirements;
- store metadata, screenshots, claims, promotions, ratings, localization, and impersonation.

Inspect implementation and, when authorized, runtime network behavior. A declaration can be complete only when each material data flow is evidenced. If a console question is ambiguous or the evidence is missing, preserve the draft and ask for the needed fact; do not select the most permissive answer.

For every policy-dependent release decision, retain enough source context to reproduce the interpretation without copying long passages. Policy review remains risk assessment, not legal advice or approval assurance.
