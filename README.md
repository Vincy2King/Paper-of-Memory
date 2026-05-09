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

- Total tracked papers: **144**
- Last generated: **2026-05-09**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **110**
- OpenReview: **33**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-07 | arXiv | [When Quantization Is Free: An int4 KV Cache That Outruns fp16 on Apple Silicon](content/papers/when-quantization-is-free-an-int4-kv-cache-that-outruns-fp16-on-apple-silicon.md) | compression, context |
| 2026-05-07 | arXiv | [When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI](content/papers/when-agents-handle-secrets-a-survey-of-confidential-computing-for-agentic-ai.md) | agent, context |
| 2026-05-07 | arXiv | [What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis](content/papers/what-happens-inside-agent-memory-circuit-analysis-from-emergence-to-diagnosis.md) | agent, context |
| 2026-05-07 | arXiv | [SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety](content/papers/safeharbor-hierarchical-memory-augmented-guardrail-for-llm-agent-safety.md) | agent, context |
| 2026-05-07 | arXiv | [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](content/papers/stale-can-llm-agents-know-when-their-memories-are-no-longer-valid.md) | agent, benchmark, context |
| 2026-05-07 | arXiv | [PairAlign: A Framework for Sequence Tokenization via Self-Alignment with Applications to Audio Tokenization](content/papers/pairalign-a-framework-for-sequence-tokenization-via-self-alignment-with-applicat.md) | retrieval |
| 2026-05-07 | arXiv | [PEPA: a Persistently Autonomous Embodied Agent with Personalities](content/papers/pepa-a-persistently-autonomous-embodied-agent-with-personalities.md) | agent, episodic, long-term |
| 2026-05-07 | arXiv | [MiA-Signature: Approximating Global Activation for Long-Context Understanding](content/papers/mia-signature-approximating-global-activation-for-long-context-understanding.md) | agent, context |
| 2026-05-07 | arXiv | [MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval](content/papers/memreranker-reasoning-aware-reranking-for-agent-memory-retrieval.md) | agent, benchmark, context |
| 2026-05-07 | arXiv | [I see artifacts: ICA-based EEG artifact removal does not improve deep network decoding across three BCI tasks](content/papers/i-see-artifacts-ica-based-eeg-artifact-removal-does-not-improve-deep-network-dec.md) | long-term |
| 2026-05-07 | OpenReview | [GAAMA: Graph Augmented Associative Memory for Agents](content/papers/gaama-graph-augmented-associative-memory-for-agents.md) | agent, benchmark, compression |
| 2026-05-07 | arXiv | [Contextual Memory-Enhanced Source Coding for Low-SNR Communications](content/papers/contextual-memory-enhanced-source-coding-for-low-snr-communications.md) | context |
| 2026-05-07 | arXiv | [Belief Memory: Agent Memory Under Partial Observability](content/papers/belief-memory-agent-memory-under-partial-observability.md) | agent, benchmark, context |
| 2026-05-07 | arXiv | [Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination](content/papers/attractor-geometry-of-transformer-memory-from-conflict-arbitration-to-confident-.md) | context |
| 2026-05-07 | OpenReview | [A Brain System for Auditory Working Memory](content/papers/a-brain-system-for-auditory-working-memory.md) | retrieval |
| 2026-05-06 | arXiv | [Storage Is Not Memory: A Retrieval-Centered Architecture for Agent Recall](content/papers/storage-is-not-memory-a-retrieval-centered-architecture-for-agent-recall.md) | agent, conversation, retrieval |
| 2026-05-06 | arXiv | [RLDX-1 Technical Report](content/papers/rldx-1-technical-report.md) | benchmark, long-term |
| 2026-05-06 | arXiv | [LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents](content/papers/longseeker-elastic-context-orchestration-for-long-horizon-search-agents.md) | agent, benchmark, context |
| 2026-05-06 | arXiv | [Contextual Memory-Enhanced Source Coding for Low-SNR Communications](content/papers/contextual-memory-enhanced-source-coding-for-low-snr-communications.md) | context |
| 2026-05-06 | arXiv | [A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework](content/papers/a-systematic-survey-of-security-threats-and-defenses-in-llm-based-ai-agents-a-la.md) | agent, benchmark |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
