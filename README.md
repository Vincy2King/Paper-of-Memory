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

- Total tracked papers: **908**
- Last generated: **2026-08-11**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **769**
- OpenReview: **134**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-10 | OpenReview | [When Should LLMs Use Behavioral Memory? Task-Dependent Retrieval for Personalized Long-Term Memory](content/papers/when-should-llms-use-behavioral-memory-task-dependent-retrieval-for-personalized.md) | long-term, retrieval |
| 2026-08-10 | OpenReview | [ReWork: Efficient Iterative Reasoning with Working Memory](content/papers/rework-efficient-iterative-reasoning-with-working-memory.md) | working memory |
| 2026-08-07 | arXiv | [The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, and ML Workflows](content/papers/the-optimizer-is-the-agent-reasoning-driven-search-across-prompts-programs-and-m.md) | agent |
| 2026-08-07 | arXiv | [The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents](content/papers/the-horizon-gap-planning-memory-execution-training-and-evaluation-for-long-horiz.md) | agent, context, long-term |
| 2026-08-07 | arXiv | [TEPA: Revoking Stale Memories for Conflict-Robust Language Agents](content/papers/tepa-revoking-stale-memories-for-conflict-robust-language-agents.md) | agent, context, long-term |
| 2026-08-07 | arXiv | [MemWM: Memory-Augmented Text-Based World Model](content/papers/memwm-memory-augmented-text-based-world-model.md) | agent, benchmark |
| 2026-08-07 | arXiv | [MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents](content/papers/memprism-task-conditioned-relational-memory-views-for-long-horizon-agents.md) | agent, benchmark, context |
| 2026-08-07 | arXiv | [MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents](content/papers/memopd-on-policy-distillation-through-memory-state-alignment-for-long-horizon-ag.md) | agent, compression, context |
| 2026-08-07 | arXiv | [LifelongCrossNav: Persistent 3D Semantic Memory for Cross-Floor Multi-Object Navigation](content/papers/lifelongcrossnav-persistent-3d-semantic-memory-for-cross-floor-multi-object-navi.md) | agent, benchmark, retrieval |
| 2026-08-07 | arXiv | [Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis](content/papers/learning-suffers-more-than-the-policy-class-under-partial-observability-a-closed.md) | agent |
| 2026-08-07 | arXiv | [LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers](content/papers/llmrouter-unified-infrastructure-for-developing-evaluating-and-deploying-llm-rou.md) | benchmark, context |
| 2026-08-07 | arXiv | [Explicit, Not Longer: What Makes Epistemic Stance Survive Memory Compression](content/papers/explicit-not-longer-what-makes-epistemic-stance-survive-memory-compression.md) | agent, compression |
| 2026-08-07 | arXiv | [DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding](content/papers/docmemo-dynamic-evidence-discovery-via-probabilistic-memory-guided-retrieval-for.md) | benchmark, episodic, retrieval |
| 2026-08-07 | arXiv | [Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution](content/papers/coupling-planning-with-episodic-memory-in-llm-agents-for-software-issue-resoluti.md) | agent, context, episodic |
| 2026-08-07 | arXiv | [Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](content/papers/agent-memory-distillation-empowering-small-llm-agents-with-hierarchical-teacher-.md) | agent, benchmark |
| 2026-08-07 | arXiv | [Addressable Memory for Video World Models](content/papers/addressable-memory-for-video-world-models.md) | benchmark, compression, episodic |
| 2026-08-06 | arXiv | [Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering](content/papers/trace-only-what-you-need-structure-aware-on-demand-hypergraph-memory-for-long-do.md) | agent, benchmark, context |
| 2026-08-06 | arXiv | [SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation](content/papers/skillmemo-expert-guided-skill-memory-framework-for-compositional-embodied-manipu.md) | benchmark, context, episodic |
| 2026-08-06 | OpenReview | [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](content/papers/profile-graph-memory-for-llm-agents-implicit-cross-entity-traversal-through-narr.md) | agent, benchmark, compression |
| 2026-08-06 | OpenReview | [MemTrace: Probing What Final Accuracy Misses in Long-Term Memory](content/papers/memtrace-probing-what-final-accuracy-misses-in-long-term-memory.md) | agent, benchmark, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
