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

- Total tracked papers: **545**
- Last generated: **2026-06-23**

## Papers by Source

- ACL Anthology: **4**
- arXiv: **458**
- OpenReview: **83**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-06-23 | OpenReview | [AgenticLOCI: A Multi-Agent Memory Framework for Conversational AI with Longitudinal Personalization](content/papers/agenticloci-a-multi-agent-memory-framework-for-conversational-ai-with-longitudin.md) | agent, benchmark, context |
| 2026-06-22 | OpenReview | [GATEMEM: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents](content/papers/gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents.md) | agent, benchmark, context |
| 2026-06-22 | ACL Anthology | [CloneMem: Benchmarking Long-Term Memory for AI Clones](content/papers/clonemem-benchmarking-long-term-memory-for-ai-clones.md) | benchmark, long-term |
| 2026-06-22 | ACL Anthology | [Beyond Markovian Forgetfulness: Episodic Memory for Reasoning-Intensive Retrieval](content/papers/beyond-markovian-forgetfulness-episodic-memory-for-reasoning-intensive-retrieval.md) | episodic, retrieval |
| 2026-06-22 | ACL Anthology | [BMAM: Brain-inspired Multi-Agent Memory Framework](content/papers/bmam-brain-inspired-multi-agent-memory-framework.md) | agent |
| 2026-06-22 | OpenReview | [AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation](content/papers/atommem-learnable-dynamic-agentic-memory-with-atomic-memory-operation.md) | agent, benchmark, context |
| 2026-06-21 | OpenReview | [EngramaBench: Evaluating Long-Term Conversational Memory with Structured Graph Retrieval](content/papers/engramabench-evaluating-long-term-conversational-memory-with-structured-graph-re.md) | benchmark, context, conversation |
| 2026-06-21 | OpenReview | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-06-20 | OpenReview | [TAME: A Trustworthy Test-Time Evolution of Agent Memory with Systematic Benchmarking](content/papers/tame-a-trustworthy-test-time-evolution-of-agent-memory-with-systematic-benchmark.md) | agent, benchmark |
| 2026-06-20 | OpenReview | [Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks](content/papers/same-ranking-different-winner-how-scoring-targets-shape-llm-memory-benchmarks.md) | benchmark, conversation, retrieval |
| 2026-06-20 | OpenReview | [SHM-GATE: Structured Hierarchical Memory with Gated Admission for Multi-Agent LLM Hallucination Containment](content/papers/shm-gate-structured-hierarchical-memory-with-gated-admission-for-multi-agent-llm.md) | agent, benchmark, conversation |
| 2026-06-19 | OpenReview | [MemoNav: Working Memory Model for Visual Navigation](content/papers/memonav-working-memory-model-for-visual-navigation.md) | agent, long-term |
| 2026-06-19 | OpenReview | [MemoNav: Working Memory Model for Visual Navigation](content/papers/memonav-working-memory-model-for-visual-navigation.md) | agent, long-term |
| 2026-06-19 | OpenReview | [HGP: An on-device personalized agent memory via hybrid graph storage](content/papers/hgp-an-on-device-personalized-agent-memory-via-hybrid-graph-storage.md) | agent, benchmark, episodic |
| 2026-06-19 | OpenReview | [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](content/papers/h2hmem-a-multimodal-memory-benchmark-for-agents-in-human-human-interactions.md) | agent, benchmark, conversation |
| 2026-06-19 | OpenReview | [H2G-Mem: Heterogeneous HyperGraphs for Fine-Grained Long-term Conversational Agent Memory](content/papers/h2g-mem-heterogeneous-hypergraphs-for-fine-grained-long-term-conversational-agen.md) | agent, benchmark, context |
| 2026-06-18 | OpenReview | [The Override Cliff: How Agent Memory Hijacks LLM Reasoning](content/papers/the-override-cliff-how-agent-memory-hijacks-llm-reasoning.md) | agent, benchmark, retrieval |
| 2026-06-18 | arXiv | [RTSGameBench: An RTS Benchmark for Strategic Reasoning by Vision-Language Models](content/papers/rtsgamebench-an-rts-benchmark-for-strategic-reasoning-by-vision-language-models.md) | agent, benchmark |
| 2026-06-18 | arXiv | [RACL: Reasoning-Agent Control Layers for Continuous Metaheuristic Learning](content/papers/racl-reasoning-agent-control-layers-for-continuous-metaheuristic-learning.md) | agent |
| 2026-06-18 | arXiv | [PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents](content/papers/pacms-submodular-context-selection-as-a-pluggable-engine-for-llm-agents.md) | agent, compression, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
