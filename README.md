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

- Total tracked papers: **1628**
- Last generated: **2026-11-09**

## Papers by Source

- ACL Anthology: **24**
- arXiv: **1458**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-11-06 | arXiv | [TimeOmni-Live: Continuous & Live Time Series Understanding with Long-Term Memory](content/papers/timeomni-live-continuous-live-time-series-understanding-with-long-term-memory.md) | context, long-term |
| 2026-11-06 | arXiv | [Oscillatory Phase Coding Emerges in Adaptive RNNs for Flexible Working Memory](content/papers/oscillatory-phase-coding-emerges-in-adaptive-rnns-for-flexible-working-memory.md) | working memory |
| 2026-11-06 | arXiv | [On Agentic Manipulation Policies](content/papers/on-agentic-manipulation-policies.md) | agent, benchmark |
| 2026-11-06 | arXiv | [Not Your Diary, Just Your Topic: Grading the Wrong-User Control](content/papers/not-your-diary-just-your-topic-grading-the-wrong-user-control.md) | memory |
| 2026-11-06 | arXiv | [MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory](content/papers/memorydojo-benchmarking-poisoning-through-llm-agent-memory.md) | agent, benchmark |
| 2026-11-06 | arXiv | [HomeLoop: A Simulation Framework and Benchmark for Robot-IoT Coordination in Everyday Domestic Assistance and Safety](content/papers/homeloop-a-simulation-framework-and-benchmark-for-robot-iot-coordination-in-ever.md) | agent, benchmark, long-term |
| 2026-11-06 | arXiv | [HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes](content/papers/himem-hippocampus-inspired-memory-consolidation-pruning-and-composition-for-visi.md) | episodic |
| 2026-11-06 | arXiv | [Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning](content/papers/encoding-memory-in-world-models-with-test-time-model-based-reinforcement-learnin.md) | agent, benchmark, context |
| 2026-11-06 | arXiv | [Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation](content/papers/compaction-decay-and-reinforcement-in-a-two-tier-conversational-memory-a-paired-.md) | agent, conversation, retrieval |
| 2026-11-05 | arXiv | [The Memory Trap: Language Agents Overgeneralize from Benign Interactions](content/papers/the-memory-trap-language-agents-overgeneralize-from-benign-interactions.md) | agent |
| 2026-11-05 | arXiv | [NEAR: Neighborhood-Aware Residuals for Memory Retrieval](content/papers/near-neighborhood-aware-residuals-for-memory-retrieval.md) | benchmark, context, retrieval |
| 2026-11-05 | arXiv | [Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation](content/papers/memory-aware-multi-agent-architecture-with-llm-based-orchestration-for-conversat.md) | agent, conversation, long-term |
| 2026-11-05 | arXiv | [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation](content/papers/memory-before-goal-role-of-pre-history-memory-for-humanoid-loco-manipulation.md) | benchmark |
| 2026-11-05 | arXiv | [MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents](content/papers/memoir-a-training-free-memory-lifecycle-for-long-horizon-llm-agents.md) | agent, compression, retrieval |
| 2026-11-05 | arXiv | [Jacobian-Causal Memory Control for Persistent Memory in Language Model Systems](content/papers/jacobian-causal-memory-control-for-persistent-memory-in-language-model-systems.md) | benchmark, retrieval |
| 2026-11-05 | arXiv | [HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding](content/papers/hyflash-a-prefix-memory-prior-for-on-device-speculative-decoding.md) | context |
| 2026-11-05 | arXiv | [FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](content/papers/fincosmos-an-open-world-evaluation-paradigm-for-agents-in-finance.md) | agent, benchmark |
| 2026-11-05 | arXiv | [Enhancing Local and Global Structure in Compressed AI Agent Memory](content/papers/enhancing-local-and-global-structure-in-compressed-ai-agent-memory.md) | agent, compression |
| 2026-11-05 | arXiv | [Decision Context: Persistent Behavioral Learning for AI Agents](content/papers/decision-context-persistent-behavioral-learning-for-ai-agents.md) | agent, benchmark, context |
| 2026-11-05 | arXiv | [Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence](content/papers/beyond-the-final-embedding-retrieving-memories-from-token-level-evidence.md) | benchmark, context, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
