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

- Total tracked papers: **1364**
- Last generated: **2026-10-09**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1212**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-08 | arXiv | [Workerville: Towards an Organizational Behavior Account of Agent Safety](content/papers/workerville-towards-an-organizational-behavior-account-of-agent-safety.md) | agent, benchmark, long-term |
| 2026-10-08 | arXiv | [What to Admit and How to Present: Governing Persistent Memory in LLM Agents](content/papers/what-to-admit-and-how-to-present-governing-persistent-memory-in-llm-agents.md) | agent, benchmark, context |
| 2026-10-08 | arXiv | [Using LMs to Model the Effects of Context and Coreference during Sentence Comprehension](content/papers/using-lms-to-model-the-effects-of-context-and-coreference-during-sentence-compre.md) | context |
| 2026-10-08 | arXiv | [Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents](content/papers/use-and-disuse-intent-structured-experience-consolidation-for-memory-and-learnin.md) | agent, context, long-term |
| 2026-10-08 | arXiv | [Test-Time Compute for Tabular Foundation Models: Mechanisms, Gains, and Limits](content/papers/test-time-compute-for-tabular-foundation-models-mechanisms-gains-and-limits.md) | benchmark, context, retrieval |
| 2026-10-08 | arXiv | [ReTeach: Building a Self-Teacher through Multi-Round Reflection and Retry](content/papers/reteach-building-a-self-teacher-through-multi-round-reflection-and-retry.md) | benchmark, context |
| 2026-10-08 | arXiv | [Memory Type Varies: Empowering LLM Agents for Long-Term Memory with Diverse Strategies](content/papers/memory-type-varies-empowering-llm-agents-for-long-term-memory-with-diverse-strat.md) | agent, long-term, retrieval |
| 2026-10-08 | arXiv | [MemTrace: State-Consistent Memory for Long-Horizon Coding Agents](content/papers/memtrace-state-consistent-memory-for-long-horizon-coding-agents.md) | agent, benchmark, compression |
| 2026-10-08 | arXiv | [Gated Memory: Admission-Controlled Memory Formation for Conversational AI](content/papers/gated-memory-admission-controlled-memory-formation-for-conversational-ai.md) | benchmark, context, conversation |
| 2026-10-08 | arXiv | [Event-Centric Memory with Query-Aware Graph Augmentation for Long-Term Conversational Agents](content/papers/event-centric-memory-with-query-aware-graph-augmentation-for-long-term-conversat.md) | agent, benchmark, context |
| 2026-10-08 | arXiv | [Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning](content/papers/do-llms-learn-from-rewards-in-context-rethinking-the-role-of-reward-in-in-contex.md) | agent, benchmark, context |
| 2026-10-08 | arXiv | [DeltaReplay: Task-Relative Memory Reuse for Mobile GUI Agents](content/papers/deltareplay-task-relative-memory-reuse-for-mobile-gui-agents.md) | agent |
| 2026-10-08 | arXiv | [Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval](content/papers/causal-memory-policy-making-memory-utility-identifiable-by-intervening-on-retrie.md) | context, retrieval |
| 2026-10-08 | arXiv | [Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds](content/papers/beyond-the-remembered-world-predictive-4d-belief-for-persistent-navigation-in-ev.md) | agent, benchmark, retrieval |
| 2026-10-08 | arXiv | [Beyond Sequences: Distilling Structured Decision Memory for LLM Recommendation](content/papers/beyond-sequences-distilling-structured-decision-memory-for-llm-recommendation.md) | context |
| 2026-10-08 | arXiv | [BRACE: Differential Privacy for Dense Associative Memory with LSR Energy](content/papers/brace-differential-privacy-for-dense-associative-memory-with-lsr-energy.md) | retrieval |
| 2026-10-07 | arXiv | [VideoEvolve: Co-Evolving Memory and Retrieval for Long Video Understanding](content/papers/videoevolve-co-evolving-memory-and-retrieval-for-long-video-understanding.md) | agent, benchmark, retrieval |
| 2026-10-07 | arXiv | [Stale, Misattributed, or Late: Where Personal Memory Fails Before Generation](content/papers/stale-misattributed-or-late-where-personal-memory-fails-before-generation.md) | agent, benchmark, retrieval |
| 2026-10-07 | arXiv | [SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles](content/papers/skillforge-co-evolving-skills-and-agents-via-dynamic-skill-lifecycles.md) | agent, benchmark |
| 2026-10-07 | arXiv | [Self-Supervised Keyframe Discovery for Horizon-Invariant Behavior Cloning](content/papers/self-supervised-keyframe-discovery-for-horizon-invariant-behavior-cloning.md) | benchmark, context, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
