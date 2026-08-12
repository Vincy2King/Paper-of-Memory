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

- Total tracked papers: **929**
- Last generated: **2026-08-12**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **790**
- OpenReview: **134**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-11 | arXiv | [TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents](content/papers/tarl-transaction-aware-reliable-ledgers-for-executable-memory-management-in-long.md) | agent, benchmark, long-term |
| 2026-08-11 | arXiv | [StreamFlow: Dynamic Memory Flows for Streaming Video Understanding](content/papers/streamflow-dynamic-memory-flows-for-streaming-video-understanding.md) | benchmark, long-term, retrieval |
| 2026-08-11 | OpenReview | [ReWork: Efficient Iterative Reasoning with Working Memory](content/papers/rework-efficient-iterative-reasoning-with-working-memory.md) | working memory |
| 2026-08-11 | arXiv | [On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models](content/papers/on-understanding-identifying-and-mitigating-vulnerabilities-in-agentic-large-lan.md) | agent, conversation |
| 2026-08-11 | arXiv | [Living-Harness Is an Interactive-Agent Evolver](content/papers/living-harness-is-an-interactive-agent-evolver.md) | agent, context, episodic |
| 2026-08-11 | arXiv | [From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents](content/papers/from-faulty-memories-to-corrected-actions-dependency-guided-rollback-repair-for-.md) | agent, benchmark |
| 2026-08-11 | arXiv | [EvoMem: Memory-Augmented Evolution for Code Optimization](content/papers/evomem-memory-augmented-evolution-for-code-optimization.md) | benchmark, context |
| 2026-08-11 | arXiv | [Efficient Reinforcement Learning for Long-Horizon Tool-Use Agentic Tasks](content/papers/efficient-reinforcement-learning-for-long-horizon-tool-use-agentic-tasks.md) | agent, benchmark, context |
| 2026-08-11 | arXiv | [Decomposition-Induced Context-Memory Conflict: When Fact-Checking Pipelines Contradict Their Own Source Text](content/papers/decomposition-induced-context-memory-conflict-when-fact-checking-pipelines-contr.md) | context |
| 2026-08-10 | OpenReview | [When Should LLMs Use Behavioral Memory? Task-Dependent Retrieval for Personalized Long-Term Memory](content/papers/when-should-llms-use-behavioral-memory-task-dependent-retrieval-for-personalized.md) | long-term, retrieval |
| 2026-08-10 | arXiv | [TEPA: Revoking Stale Memories for Conflict-Robust Language Agents](content/papers/tepa-revoking-stale-memories-for-conflict-robust-language-agents.md) | agent, context, long-term |
| 2026-08-10 | arXiv | [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](content/papers/she-trajectory-driven-safety-harness-evolution-for-llm-agents.md) | agent, benchmark, context |
| 2026-08-10 | arXiv | [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States](content/papers/romerl-balancing-feedback-coverage-and-the-memory-reward-trap-in-self-evolving-a.md) | agent |
| 2026-08-10 | arXiv | [Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models](content/papers/omni2lora-coherence-preserving-parametric-memory-for-efficient-omni-language-mod.md) | benchmark, compression, context |
| 2026-08-10 | arXiv | [MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory](content/papers/mesa-task-adaptive-multi-structure-evidence-selection-for-long-horizon-agent-mem.md) | agent, context |
| 2026-08-10 | arXiv | [KVDiagnosis: A Diagnostic Benchmark for KV-Cache Compression in Long-Context Language Models](content/papers/kvdiagnosis-a-diagnostic-benchmark-for-kv-cache-compression-in-long-context-lang.md) | benchmark, compression, context |
| 2026-08-09 | arXiv | [REVEAL: A Rubric-Guided Agent for Explicit Evidence Sufficiency Verificationin Long-Video Question Answering](content/papers/reveal-a-rubric-guided-agent-for-explicit-evidence-sufficiency-verificationin-lo.md) | agent, context, retrieval |
| 2026-08-09 | arXiv | [AquiLLM: An Architecture for Supporting Tacit Knowledge Capture in Research Groups](content/papers/aquillm-an-architecture-for-supporting-tacit-knowledge-capture-in-research-group.md) | episodic, retrieval |
| 2026-08-08 | arXiv | [SuperLocalMemory 4.0: The Governed Memory Operating System for AI Agents](content/papers/superlocalmemory-4-0-the-governed-memory-operating-system-for-ai-agents.md) | agent, benchmark, context |
| 2026-08-08 | arXiv | [Mitigating Over-Personalization in LLMs via Structured Memory](content/papers/mitigating-over-personalization-in-llms-via-structured-memory.md) | context, conversation, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
