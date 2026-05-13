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

- Total tracked papers: **203**
- Last generated: **2026-05-13**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **168**
- OpenReview: **34**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-12 | arXiv | [SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs](content/papers/skillgraph-skill-augmented-reinforcement-learning-for-agents-via-evolving-skill-.md) | agent |
| 2026-05-12 | arXiv | [SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory](content/papers/sage-a-self-evolving-agentic-graph-memory-engine-for-structure-aware-associative.md) | agent, benchmark, long-term |
| 2026-05-12 | arXiv | [Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs](content/papers/retrieve-then-steer-online-success-memory-for-test-time-adaptation-of-generative.md) | long-term, retrieval |
| 2026-05-12 | arXiv | [Mitigating Context-Memory Conflicts in LLMs through Dynamic Cognitive Reconciliation Decoding](content/papers/mitigating-context-memory-conflicts-in-llms-through-dynamic-cognitive-reconcilia.md) | benchmark, context |
| 2026-05-12 | arXiv | [MemQ: Integrating Q-Learning into Self-Evolving Memory Agents over Provenance DAGs](content/papers/memq-integrating-q-learning-into-self-evolving-memory-agents-over-provenance-dag.md) | agent, benchmark, context |
| 2026-05-12 | arXiv | [MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare](content/papers/medmemorybench-benchmarking-agent-memory-in-personalized-healthcare.md) | agent, benchmark, conversation |
| 2026-05-12 | arXiv | [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](content/papers/longmemeval-v2-evaluating-long-term-agent-memory-toward-experienced-colleagues.md) | agent, benchmark, context |
| 2026-05-12 | arXiv | [Improving the Performance and Learning Stability of Parallelizable RNNs Designed for Ultra-Low Power Applications](content/papers/improving-the-performance-and-learning-stability-of-parallelizable-rnns-designed.md) | benchmark, long-term |
| 2026-05-12 | arXiv | [Goal-Oriented Reasoning for RAG-based Memory in Conversational Agentic LLM Systems](content/papers/goal-oriented-reasoning-for-rag-based-memory-in-conversational-agentic-llm-syste.md) | agent, context, conversation |
| 2026-05-12 | arXiv | [GRC: Unifying Reasoning-Driven Generation, Retrieval and Compression](content/papers/grc-unifying-reasoning-driven-generation-retrieval-and-compression.md) | agent, benchmark, compression |
| 2026-05-12 | arXiv | [Executable Agentic Memory for GUI Agent](content/papers/executable-agentic-memory-for-gui-agent.md) | agent, retrieval |
| 2026-05-12 | arXiv | [Automated Reformulation of Robust Optimization via Memory-Augmented Large Language Models](content/papers/automated-reformulation-of-robust-optimization-via-memory-augmented-large-langua.md) | benchmark |
| 2026-05-11 | arXiv | [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](content/papers/rubricem-meta-rl-with-rubric-guided-policy-decomposition-beyond-verifiable-rewar.md) | agent, benchmark |
| 2026-05-11 | arXiv | [Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs](content/papers/retrieve-then-steer-online-success-memory-for-test-time-adaptation-of-generative.md) | long-term, retrieval |
| 2026-05-11 | arXiv | [Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](content/papers/remember-the-decision-not-the-description-a-rate-distortion-framework-for-agent-.md) | agent, benchmark, compression |
| 2026-05-11 | arXiv | [Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents](content/papers/nautilus-compass-black-box-persona-drift-detection-for-production-llm-agents.md) | agent, conversation, retrieval |
| 2026-05-11 | arXiv | [MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading](content/papers/memreread-enhancing-agentic-long-context-reasoning-via-memory-guided-rereading.md) | agent, context, retrieval |
| 2026-05-11 | arXiv | [Mela: Test-Time Memory Consolidation based on Transformation Hypothesis](content/papers/mela-test-time-memory-consolidation-based-on-transformation-hypothesis.md) | context, episodic, retrieval |
| 2026-05-11 | arXiv | [MAGE: Multi-Agent Self-Evolution with Co-Evolutionary Knowledge Graphs](content/papers/mage-multi-agent-self-evolution-with-co-evolutionary-knowledge-graphs.md) | agent, benchmark, episodic |
| 2026-05-11 | arXiv | [Layered Mutability: Continuity and Governance in Persistent Self-Modifying Agents](content/papers/layered-mutability-continuity-and-governance-in-persistent-self-modifying-agents.md) | agent |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
