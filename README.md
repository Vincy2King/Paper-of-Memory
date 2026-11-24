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

- Total tracked papers: **1725**
- Last generated: **2026-11-24**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1555**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-20 | arXiv | [VMSA: Video Memory Skill Agent for Long Video Understanding](content/papers/vmsa-video-memory-skill-agent-for-long-video-understanding.md) | agent, benchmark, context |
| 2026-11-20 | arXiv | [STARK: Moving towards Personalized Agents That Truly Learn and Remember](content/papers/stark-moving-towards-personalized-agents-that-truly-learn-and-remember.md) | agent, benchmark, context |
| 2026-11-20 | arXiv | [Privacy Protection in Self-Evolving Personal Agents: Persistent Memory and Cross-Carrier Transfer](content/papers/privacy-protection-in-self-evolving-personal-agents-persistent-memory-and-cross-.md) | agent |
| 2026-11-20 | arXiv | [Double counting in LLM evidence fusion: exact posteriors separate rule compliance from posterior gain](content/papers/double-counting-in-llm-evidence-fusion-exact-posteriors-separate-rule-compliance.md) | agent, retrieval |
| 2026-11-19 | arXiv | [STARK: Moving towards Personalized Agents That Truly Learn and Remember](content/papers/stark-moving-towards-personalized-agents-that-truly-learn-and-remember.md) | agent, benchmark, context |
| 2026-11-19 | arXiv | [PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory](content/papers/physscope-agentic-multimodal-physics-reasoning-with-grounded-visual-memory.md) | agent, benchmark |
| 2026-11-19 | arXiv | [On Agentic Manipulation Policies](content/papers/on-agentic-manipulation-policies.md) | agent, benchmark |
| 2026-11-19 | arXiv | [MemMend: A Selective Revision Framework for Memory Question Answering](content/papers/memmend-a-selective-revision-framework-for-memory-question-answering.md) | conversation, long-term |
| 2026-11-19 | arXiv | [MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management](content/papers/memfolder-structure-guided-memory-folding-for-efficient-agent-memory-management.md) | agent, benchmark, compression |
| 2026-11-19 | arXiv | [How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents](content/papers/how-much-should-an-agent-remember-deployment-lessons-from-self-distilled-memory-.md) | agent, benchmark |
| 2026-11-19 | arXiv | [DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents](content/papers/driftguard-online-memory-drift-detection-via-causal-attribution-for-llm-agents.md) | agent, retrieval |
| 2026-11-19 | arXiv | [Decoupled Knowledge Retrieval and Compact Memory Enable Reliable Lifelong Model Editing](content/papers/decoupled-knowledge-retrieval-and-compact-memory-enable-reliable-lifelong-model-.md) | benchmark, long-term, retrieval |
| 2026-11-19 | arXiv | [Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding](content/papers/broad-persistent-advising-in-interactive-reinforcement-learning-via-latent-state.md) | persistent memory |
| 2026-11-19 | arXiv | [AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress](content/papers/astronautbench-measuring-agent-self-improvement-across-episodes-through-knowledg.md) | agent, benchmark, episodic |
| 2026-11-19 | arXiv | [ActMem: From Latent Memory Reasoning to Grounded Robotic Action](content/papers/actmem-from-latent-memory-reasoning-to-grounded-robotic-action.md) | context |
| 2026-11-18 | arXiv | [Twists and Turns: A Graph-Based Benchmark and Framework for Long-Term Memory in Exploration Tasks](content/papers/twists-and-turns-a-graph-based-benchmark-and-framework-for-long-term-memory-in-e.md) | benchmark, long-term, retrieval |
| 2026-11-18 | arXiv | [Resolution as Attention for Efficient Agent Memory Perception](content/papers/resolution-as-attention-for-efficient-agent-memory-perception.md) | agent |
| 2026-11-18 | arXiv | [On Agentic Manipulation Policies](content/papers/on-agentic-manipulation-policies.md) | agent, benchmark |
| 2026-11-18 | arXiv | [Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents](content/papers/multi-agent-memory-inconsistency-where-factual-conflicts-disappear-in-llm-agents.md) | agent, benchmark, context |
| 2026-11-18 | arXiv | [MemoSync: Co-Managing Developer-Agent Metamemory Across Contexts](content/papers/memosync-co-managing-developer-agent-metamemory-across-contexts.md) | agent, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
