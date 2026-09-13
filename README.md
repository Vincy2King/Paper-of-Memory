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

- Total tracked papers: **1130**
- Last generated: **2026-09-13**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **981**
- OpenReview: **143**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-09-12 | OpenReview | [Geometry-Conditioned Turn Scoring for Conversational Memory Compression](content/papers/geometry-conditioned-turn-scoring-for-conversational-memory-compression.md) | benchmark, compression, context |
| 2026-09-11 | OpenReview | [Representational Geometries of Perception and Working Memory](content/papers/representational-geometries-of-perception-and-working-memory.md) | working memory |
| 2026-09-11 | OpenReview | [Multiple Oscillatory Neural Rhythms Support Metacognitive Access of Working Memory](content/papers/multiple-oscillatory-neural-rhythms-support-metacognitive-access-of-working-memo.md) | working memory |
| 2026-09-11 | OpenReview | [Does Working Memory Selectively Modulate Subjective Perception?](content/papers/does-working-memory-selectively-modulate-subjective-perception.md) | working memory |
| 2026-09-10 | arXiv | [Memory Compression for High-Fanout Agent Sandboxes](content/papers/memory-compression-for-high-fanout-agent-sandboxes.md) | agent, compression |
| 2026-09-10 | arXiv | [MAPLE: Memory-Augmented Planning with Language and Evolution](content/papers/maple-memory-augmented-planning-with-language-and-evolution.md) | agent, benchmark |
| 2026-09-10 | arXiv | [Grounding Agent Memory: Environment-Probing Curation for Enterprise Agents](content/papers/grounding-agent-memory-environment-probing-curation-for-enterprise-agents.md) | agent, context |
| 2026-09-10 | arXiv | [Causal Episodic Memory for Feedback-Driven Agent Repair](content/papers/causal-episodic-memory-for-feedback-driven-agent-repair.md) | agent, benchmark, episodic |
| 2026-09-10 | OpenReview | [Beyond Retrieval: Analytic Memory for Multimodal Agents](content/papers/beyond-retrieval-analytic-memory-for-multimodal-agents.md) | agent, benchmark, context |
| 2026-09-09 | arXiv | [What Should an Agent Forget? Separating What Is Stored from What Is Used](content/papers/what-should-an-agent-forget-separating-what-is-stored-from-what-is-used.md) | agent, context, conversation |
| 2026-09-09 | arXiv | [PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations](content/papers/pragma-evaluating-personalized-guidance-with-memory-alignment-in-lifelong-conver.md) | benchmark, context, conversation |
| 2026-09-09 | arXiv | [Myocardial Strain Drift Correction in Deep Learning Based Ultrasound Tracking](content/papers/myocardial-strain-drift-correction-in-deep-learning-based-ultrasound-tracking.md) | persistent memory |
| 2026-09-09 | OpenReview | [Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents](content/papers/memory-makes-the-difference-evaluating-how-different-memory-roles-shape-conversa.md) | agent, context, conversation |
| 2026-09-09 | arXiv | [HyperTrace: Hypothesis-Based Preference Tracing for Online LLM Personalization](content/papers/hypertrace-hypothesis-based-preference-tracing-for-online-llm-personalization.md) | long-term |
| 2026-09-08 | arXiv | [What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory](content/papers/what-eviction-destroys-a-restore-counterfactual-audit-of-forgetting-in-agent-mem.md) | agent, benchmark, context |
| 2026-09-08 | arXiv | [T-Mem: Memory That Anticipates, Not Archives](content/papers/t-mem-memory-that-anticipates-not-archives.md) | agent, context, conversation |
| 2026-09-08 | arXiv | [Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems](content/papers/revoked-but-still-authoritative-an-empirical-study-of-revocation-enforcement-in-.md) | agent, retrieval |
| 2026-09-08 | OpenReview | [Rational Episodic Memory: From Rational Action to Agent-Centered Memory in Egocentric Video](content/papers/rational-episodic-memory-from-rational-action-to-agent-centered-memory-in-egocen.md) | agent, episodic |
| 2026-09-08 | OpenReview | [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](content/papers/profile-graph-memory-for-llm-agents-implicit-cross-entity-traversal-through-narr.md) | agent, benchmark, compression |
| 2026-09-08 | arXiv | [Personalizing LLM Agent Memory Using Biometrics](content/papers/personalizing-llm-agent-memory-using-biometrics.md) | agent, benchmark, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
