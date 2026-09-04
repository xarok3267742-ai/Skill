# Rollout and monitoring

Choose internal, closed, open, or production track based on the requested audience and risk. For production, prefer a staged rollout when rollback or server-side containment is limited.

Check the developer account's current testing and production-access eligibility before promising a track. Do not silently substitute a test track for a user-stated production request; report the eligibility blocker and preserve the best valid draft.

Define before release:

- baseline and alert threshold for crash-free users/sessions, ANR, startup, key API errors, authentication, purchases, and the product's primary journey;
- observation window appropriate to traffic;
- who pauses or advances rollout;
- remote-config, backend, prior-version, or rollout-halt containment options;
- irreversible migrations and compatibility with older clients.
- managed-publishing state, review status, country/form-factor availability, and the evidence that distinguishes submission from public availability.

Do not advance merely because no alert fired when traffic is too low. Record the evidence supporting each rollout decision.
