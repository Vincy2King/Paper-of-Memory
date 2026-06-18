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

- Total tracked papers: **523**
- Last generated: **2026-06-18**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **441**
- OpenReview: **81**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-18 | OpenReview | [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory](content/papers/memory-beyond-recall-a-dual-process-cognitive-memory-system-for-self-evolving-ag.md) | agent, benchmark, long-term |
| 2026-06-18 | OpenReview | [AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](content/papers/atommem-learnable-dynamic-agentic-memory-with-atomic-memory-operation.md) | agent, benchmark, context |
| 2026-06-17 | OpenReview | [TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking](content/papers/tame-a-trustworthy-test-time-evolution-of-agent-memory-with-systematic-benchmark.md) | agent, benchmark |
| 2026-06-17 | OpenReview | [LightGMEM: Lightweight Agent Graph Memory Generation](content/papers/lightgmem-lightweight-agent-graph-memory-generation.md) | agent, context, conversation |
| 2026-06-17 | OpenReview | [HGP: An on-device personalized agent memory via hybrid graph storage](content/papers/hgp-an-on-device-personalized-agent-memory-via-hybrid-graph-storage.md) | agent, benchmark, episodic |
| 2026-06-17 | OpenReview | [H2G-Mem: Heterogeneous HyperGraphs for Fine-Grained Long-term Conversational Agent Memory](content/papers/h2g-mem-heterogeneous-hypergraphs-for-fine-grained-long-term-conversational-agen.md) | agent, benchmark, context |
| 2026-06-17 | OpenReview | [GATEMEM: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents](content/papers/gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents.md) | agent, benchmark, context |
| 2026-06-17 | OpenReview | [GAMBIT: A Benchmark for Active Memory in Long-Horizon LLM Agents](content/papers/gambit-a-benchmark-for-active-memory-in-long-horizon-llm-agents.md) | agent, benchmark, context |
| 2026-06-17 | OpenReview | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-06-17 | OpenReview | [BenchPreS: A Benchmark for Context-Aware Personalized Preference Selectivity of Persistent-Memory LLMs](content/papers/benchpres-a-benchmark-for-context-aware-personalized-preference-selectivity-of-p.md) | benchmark, context |
| 2026-06-16 | OpenReview | [When Users Don’t Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents](content/papers/when-users-dont-ask-benchmarking-context-driven-memory-retrieval-in-conversation.md) | agent, benchmark, context |
| 2026-06-16 | OpenReview | [Remembering by Asking: Retrieval-Induced Memory Evolution for LLM Agents](content/papers/remembering-by-asking-retrieval-induced-memory-evolution-for-llm-agents.md) | agent, long-term, retrieval |
| 2026-06-16 | arXiv | [OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation](content/papers/opd-evolver-cultivating-holistic-agent-evolver-via-on-policy-distillation.md) | agent, benchmark |
| 2026-06-16 | OpenReview | [MemRefine: LLM-Guided Compression for Long-Term Agent Memory](content/papers/memrefine-llm-guided-compression-for-long-term-agent-memory.md) | agent, benchmark, compression |
| 2026-06-16 | OpenReview | [HMARS: A Hierarchical Multi-Agent Memory System for Long-Context Reasoning](content/papers/hmars-a-hierarchical-multi-agent-memory-system-for-long-context-reasoning.md) | agent, benchmark, context |
| 2026-06-16 | arXiv | [From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents](content/papers/from-agent-traces-to-trust-a-survey-of-evidence-tracing-and-execution-provenance.md) | agent, benchmark, retrieval |
| 2026-06-16 | arXiv | [FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](content/papers/finacumen-financial-multimodal-reasoning-via-self-evolving-experience-memory-har.md) | agent, benchmark, retrieval |
| 2026-06-16 | OpenReview | [Episodic Memory from Compression Boundaries in Latent Representation Space](content/papers/episodic-memory-from-compression-boundaries-in-latent-representation-space.md) | agent, compression, context |
| 2026-06-16 | arXiv | [Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations](content/papers/control-plane-placement-shapes-forgetting-an-architectural-study-of-agent-memory.md) | agent, benchmark |
| 2026-06-16 | OpenReview | [AIM: Constructing Adaptive Structured Memory via Agentic Information Management](content/papers/aim-constructing-adaptive-structured-memory-via-agentic-information-management.md) | agent, benchmark, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
