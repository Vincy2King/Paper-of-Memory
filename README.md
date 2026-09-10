# Memory Papers Tracker

A GitHub-friendly tracker for memory-related papers with one page of introduction per paper.

This repository is designed for one very specific maintenance goal: keep tracking new memory-related papers and make sure **every tracked paper has its own introduction page**.

## What This Repo Gives You

- A scheduled GitHub Action that pulls new papers from arXiv, OpenReview, and ACL Anthology.
- One Markdown page per paper under `content/papers/`.
- A generated intro for every paper, so new entries are never empty.
- A manual notes block that is preserved across automatic updates.
- A simple JSON config that you can edit without changing the code.

## Source Strategy

- `arXiv`: keyword search over recent submissions in configurable categories.
- `OpenReview`: keyword search over public forum notes, optionally narrowed by venue groups.
- `ACL Anthology`: scan the official RSS paper feed and enrich matched papers with per-paper XML metadata.

## Local Usage

```bash
python3 scripts/update_papers.py
```

Only rebuild pages and the index:

```bash
python3 scripts/update_papers.py --build-only
```

## Manual Curation

- Add non-indexed papers to `data/manual_entries.json`.
- Add your reading notes inside the `Manual Notes` block of any paper page.
- Edit `config/topics.json` when you want to tighten or broaden the notion of "memory-related".
- If you want OpenReview to focus on specific venues, fill `sources.openreview.group_ids`.

## Repository Snapshot

- Total tracked papers: **1126**
- Last generated: **2026-09-10**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **977**
- OpenReview: **143**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-09 | arXiv | [What Should an Agent Forget? Separating What Is Stored from What Is Used](content/papers/what-should-an-agent-forget-separating-what-is-stored-from-what-is-used.md) | agent, context, conversation |
| 2026-09-09 | arXiv | [PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations](content/papers/pragma-evaluating-personalized-guidance-with-memory-alignment-in-lifelong-conver.md) | benchmark, context, conversation |
| 2026-09-09 | arXiv | [Myocardial Strain Drift Correction in Deep Learning Based Ultrasound Tracking](content/papers/myocardial-strain-drift-correction-in-deep-learning-based-ultrasound-tracking.md) | persistent memory |
| 2026-09-09 | arXiv | [HyperTrace: Hypothesis-Based Preference Tracing for Online LLM Personalization](content/papers/hypertrace-hypothesis-based-preference-tracing-for-online-llm-personalization.md) | long-term |
| 2026-09-08 | arXiv | [What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory](content/papers/what-eviction-destroys-a-restore-counterfactual-audit-of-forgetting-in-agent-mem.md) | agent, benchmark, context |
| 2026-09-08 | arXiv | [T-Mem: Memory That Anticipates, Not Archives](content/papers/t-mem-memory-that-anticipates-not-archives.md) | agent, context, conversation |
| 2026-09-08 | arXiv | [Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems](content/papers/revoked-but-still-authoritative-an-empirical-study-of-revocation-enforcement-in-.md) | agent, retrieval |
| 2026-09-08 | OpenReview | [Rational Episodic Memory: From Rational Action to Agent-Centered Memory in Egocentric Video](content/papers/rational-episodic-memory-from-rational-action-to-agent-centered-memory-in-egocen.md) | agent, episodic |
| 2026-09-08 | OpenReview | [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](content/papers/profile-graph-memory-for-llm-agents-implicit-cross-entity-traversal-through-narr.md) | agent, benchmark, compression |
| 2026-09-08 | arXiv | [Personalizing LLM Agent Memory Using Biometrics](content/papers/personalizing-llm-agent-memory-using-biometrics.md) | agent, benchmark, retrieval |
| 2026-09-08 | arXiv | [MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging](content/papers/memforest-efficient-agent-memory-management-via-eventtree-partitioning-and-progr.md) | agent, benchmark, compression |
| 2026-09-08 | arXiv | [MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents](content/papers/meclear-cooperative-game-theoretic-attribution-and-risk-aware-memory-clearance-f.md) | agent, context, retrieval |
| 2026-09-08 | arXiv | [Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation](content/papers/graph-based-personalized-memory-for-llm-agents-representation-evolution-retrieva.md) | agent, context, long-term |
| 2026-09-08 | arXiv | [Does Episodic Memory Help Close the Lexical Frequency Gap in Sensitivity to Syntactic Contrasts? A Test Using Retrieval-Augmented Language Models](content/papers/does-episodic-memory-help-close-the-lexical-frequency-gap-in-sensitivity-to-synt.md) | episodic, retrieval |
| 2026-09-08 | arXiv | [Do LLMs Make More Mistakes If They Do Not Believe the Input Data?](content/papers/do-llms-make-more-mistakes-if-they-do-not-believe-the-input-data.md) | context, retrieval |
| 2026-09-08 | arXiv | [CreaMem: A Scene-Aware Memory Architecture for Personalized Agents](content/papers/creamem-a-scene-aware-memory-architecture-for-personalized-agents.md) | agent, benchmark, episodic |
| 2026-09-08 | arXiv | [Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course](content/papers/closing-the-consistency-gap-self-evolving-agents-that-learn-to-stay-on-course.md) | agent, benchmark, episodic |
| 2026-09-08 | OpenReview | [CIRCUIT Memory: Confidence-Aware Multi-Axis Retrieval for Episodic Memory in LLM Agents](content/papers/circuit-memory-confidence-aware-multi-axis-retrieval-for-episodic-memory-in-llm-.md) | agent, episodic, retrieval |
| 2026-09-07 | arXiv | [Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational Memory Question Answering](content/papers/where-to-look-and-what-to-use-retrieve-localize-generate-for-long-term-conversat.md) | benchmark, context, conversation |
| 2026-09-07 | arXiv | [On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing](content/papers/on-the-recall-scaling-laws-in-mamba-a-theoretical-and-mechanistic-study-via-hash.md) | benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
