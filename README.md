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

- Total tracked papers: **741**
- Last generated: **2026-07-24**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **621**
- OpenReview: **115**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-07-24 | OpenReview | [EvolMem: A Cognitive-Driven Benchmark for Multi-Session Dialogue Memory](content/papers/evolmem-a-cognitive-driven-benchmark-for-multi-session-dialogue-memory.md) | agent, benchmark, conversation |
| 2026-07-23 | OpenReview | [Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models](content/papers/temporal-context-reinstatement-drives-episodic-like-order-memory-in-long-context.md) | context, episodic, long-term |
| 2026-07-23 | OpenReview | [Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability](content/papers/short-term-to-long-term-memory-transfer-for-knowledge-graphs-under-partial-obser.md) | agent, benchmark, long-term |
| 2026-07-23 | OpenReview | [A Holistic System Support for Persistent Memory](content/papers/a-holistic-system-support-for-persistent-memory.md) | persistent memory |
| 2026-07-21 | arXiv | [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](content/papers/forensic-trajectory-signatures-for-agent-memory-poisoning-detection.md) | agent, retrieval |
| 2026-07-21 | ACL Anthology | [Bounded Conversational Memory with Hybrid Retrieval and Evidence Highlighting for Multi-Session Dialogue Systems](content/papers/bounded-conversational-memory-with-hybrid-retrieval-and-evidence-highlighting-fo.md) | conversation, retrieval |
| 2026-07-20 | arXiv | [ZifaMem: Structured Memory for Persona, Preference, and Emotional Continuity in AI Companions](content/papers/zifamem-structured-memory-for-persona-preference-and-emotional-continuity-in-ai-.md) | agent, context, episodic |
| 2026-07-20 | OpenReview | [Working Memory Capacity and Eye Movement Patterns in Reading: A Correlational Analysis of Regressions in the Slovenian MultiplEYE Dataset](content/papers/working-memory-capacity-and-eye-movement-patterns-in-reading-a-correlational-ana.md) | context |
| 2026-07-20 | arXiv | [Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory](content/papers/retain-or-consolidate-budget-dependent-operator-selection-for-language-agent-mem.md) | agent, benchmark, compression |
| 2026-07-20 | arXiv | [Mechanistic Attention Guidance for Agent Memory Refinement](content/papers/mechanistic-attention-guidance-for-agent-memory-refinement.md) | agent, benchmark, context |
| 2026-07-20 | arXiv | [Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory](content/papers/exploratory-and-assimilating-reflection-reflective-recall-cycle-for-long-term-me.md) | agent, benchmark, context |
| 2026-07-20 | arXiv | [Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents](content/papers/evidence-in-the-loop-trace-driven-optimization-for-customer-service-llm-agents.md) | agent, conversation, retrieval |
| 2026-07-20 | arXiv | [Autoresearch with Coding Agents: Generalizers and Metric-Maximizers on Quran Recitation Data](content/papers/autoresearch-with-coding-agents-generalizers-and-metric-maximizers-on-quran-reci.md) | agent |
| 2026-07-19 | arXiv | [Toward Anthropomorphic Dialogue: A Closed-Loop Framework for Human-Like Chat Generation, Evaluation, and Preference Alignment](content/papers/toward-anthropomorphic-dialogue-a-closed-loop-framework-for-human-like-chat-gene.md) | benchmark, long-term |
| 2026-07-19 | arXiv | [Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents](content/papers/memory-in-the-loop-in-process-retrieval-as-extended-working-memory-for-language-.md) | agent, retrieval |
| 2026-07-19 | arXiv | [Interpreting Quantum Learning Models via Stochastic Processes](content/papers/interpreting-quantum-learning-models-via-stochastic-processes.md) | episodic |
| 2026-07-18 | arXiv | [RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts](content/papers/recon-benchmarking-agent-memory-for-compositional-reasoning-over-long-contexts.md) | agent, benchmark, context |
| 2026-07-18 | arXiv | [Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration](content/papers/beyond-memory-leaderboards-evaluating-scientific-memory-as-budgeted-context-rest.md) | agent, benchmark, context |
| 2026-07-17 | arXiv | [Memory-Driven Self-Disclosure and Relational Turning Points: A Longitudinal Multimodal Study of Human-AI Interaction](content/papers/memory-driven-self-disclosure-and-relational-turning-points-a-longitudinal-multi.md) | agent, conversation |
| 2026-07-17 | arXiv | [MemoGuard: An Adaptive Runtime for Guarding Against Memory Traps in Communication-Limited Robot Navigation](content/papers/memoguard-an-adaptive-runtime-for-guarding-against-memory-traps-in-communication.md) | context, episodic, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
