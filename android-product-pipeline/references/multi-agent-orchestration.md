# Multi-agent orchestration

Use this contract when agent delegation is available for an end-to-end Android product task. The coordinator remains accountable for the requested terminal outcome and must create real specialist agents rather than merely describing simulated roles. Multi-agent execution does not expand the user's authorized app, version, accounts, repositories, or external actions.

## Coordinator ownership

The primary agent owns:

- the user conversation, adaptive intake, execution brief, and scope decisions;
- `repo/.codex/android-product.yaml`, `artifacts/pipeline-state.yaml`, and the final release record;
- dependency ordering, acceptance of specialist evidence, conflict resolution, and final quality gates;
- allocation of write ownership and the single release/publishing lease;
- the final audit of GitHub, public policy URL, Play app/version/track, and terminal status.

Only the coordinator updates the canonical checkpoint. Specialist agents return structured evidence; they do not declare the pipeline complete.

## Agent graph

Use the available concurrency slots and create only agents with concrete bounded work. Default to two or three workers in addition to the coordinator when capacity permits. Every delegated task names the exact specialist skill to use, inputs, allowed paths or external surfaces, required outputs, acceptance criteria, and prohibited mutations.

The coordinator creates and retires workers. A worker must not create descendants unless its task packet explicitly permits a bounded subtask; any descendant inherits the same path, secret, and external-mutation restrictions and can never acquire the release-writer lease implicitly.

Recommended dependency graph:

1. After intake, run competitor/product research with `$google-play-aso-expert`. For an existing app, a separate `$google-play-policy-reviewer` may inspect source, SDKs, permissions, and data flows read-only at the same time.
2. After the research synthesis is accepted by the coordinator, run `$mobile-ui-ux-designer` and an architecture-planning pass with `$android-app-developer` concurrently when both can work from immutable inputs.
3. Give implementation write ownership to `$android-app-developer`. Run `$android-ui-layout-engineer` after usable screens exist, or concurrently only for explicitly disjoint modules/files in isolated worktrees.
4. Integrate a single release-candidate commit, then run `$android-qa-engineer`, `$android-ui-layout-engineer`, `$google-play-policy-reviewer`, and `$google-play-aso-expert` review work concurrently against that same immutable revision and artifact.
5. After all required gates pass, assign `$android-release-manager` as the only agent allowed to mutate GitHub release state, Google Sites, the selected Octo profile, or Play Console.

Skip roles that do not add independent work. Do not create agents whose only task is to relay messages, restate the plan, or wait for another agent.

## Filesystem and Git ownership

- Parallel agents that only read files and do not invoke build, test, render, emulator, or code-generation tools may inspect the same checkout and immutable artifact.
- Never allow two agents to edit the same working tree or overlapping files concurrently.
- Prefer tool-provided isolated worktrees. Otherwise create explicit stage worktrees outside `repo/` with branches such as `codex/research-<run>`, `codex/implementation-<run>`, and `codex/layout-<run>`, and assign each agent exact paths.
- If isolation cannot be guaranteed, serialize all mutating/build/test/render work and parallelize only public research or pure file review that creates no shared generated state.
- Treat Gradle, lint, tests, screenshot rendering, instrumentation, code generation, emulators, ports, and device storage as writes even when source is nominally read-only. Parallel build/test/render agents require separate worktrees, Gradle/build-output locations, emulator or physical-device leases, ADB targets, and network ports; otherwise serialize them.
- Agents commit only their assigned changes. They do not modify the default branch, canonical configuration/checkpoint/release record, `private/`, signing configuration, credentials, another agent's branch, or another agent's evidence directory. They never force-push, rebase a shared branch, or merge their own work into the release branch.
- The coordinator reviews each diff and path ownership, integrates commits one at a time locally, resolves or returns conflicts, and reruns integration checks. The `$android-release-manager` alone performs the corresponding remote push, PR, merge, tag, and GitHub release mutations.
- Give each agent a unique evidence directory under `artifacts/agents/<run-id>/<role>/`. Do not let agents overwrite another role's report, screenshots, logs, or test output.
- Never pass secrets through agent prompts, messages, checkpoint files, or evidence. Provide only secret-store locators to the sole agent that requires them.

Assign canonical content ownership before implementation: the application writer owns in-app string resources; the ASO writer is the single writer for assigned Play listing metadata, listing localizations, screenshot manifest, and creative-source paths; the UX agent owns immutable screenshot art-direction evidence; the layout agent owns immutable raw rendered capture evidence; linguistic and QA agents own their immutable review reports; the policy writer/reviewer owns assigned canonical files under `repo/play/privacy-policy/`. Only the ASO writer merges reviewed screenshot evidence into the manifest; the coordinator validates and integrates that commit with all other sources before freezing release evidence. Only the release manager publishes remotely and returns immutable upload/preview evidence. Only the coordinator records that evidence in the canonical checkpoint and final release record.

## Single-writer external operations

External mutation uses a single-writer lease recorded by the coordinator. Only the current `$android-release-manager` agent may create or update the release PR/tag, publish the policy site, launch and control the selected Octo profile for mutations, upload an AAB, submit changes, or start a rollout.

Never run competing release agents, browser sessions, CI dispatches, uploads, submissions, or rollouts for the same app/version. Research agents may browse public sources; read-only Play inspection may be delegated only when it cannot race with a mutation. Before transferring a release lease after failure, verify the canonical remote state and explicitly close or interrupt the former owner.

## Handoff contract

Every agent reports:

- role and explicitly invoked skill;
- source commit/config revision and assigned scope;
- files or external surfaces read and changed;
- commands/checks run and their results;
- artifact paths, URLs, hashes, screenshots, or other reproducible evidence;
- assumptions, defects, blocked checks, and recommended next dependency.

The coordinator validates evidence before advancing the corresponding milestone. A specialist's success message without reproducible evidence is not a completed gate. If the integrated release-candidate commit changes, mark all layout, QA, policy, ASO, screenshot, and artifact evidence tied to the prior commit stale and rerun the affected gates.

## Failure, waiting, and resume

Wait for active agents with bounded waits and consume results as they arrive. Continue useful independent work while another role runs. Do not end the parent task while required agents are merely running, waiting, or have produced unreviewed results.

If an agent stalls or fails, preserve its evidence and either retry the same bounded task or reassign it after confirming that no write or external mutation remains active. Never retry an ambiguous GitHub, Sites, upload, submit, or rollout action through a second agent before reading canonical remote state.

On resume, inspect the checkpoint, live agent state when available, Git/worktrees, agent evidence directories, GitHub, the public policy URL, and Play Console. Reconstruct the dependency graph from observed state, retire stale assignments, and continue from the earliest unmet gate. Remote evidence wins over agent messages.
