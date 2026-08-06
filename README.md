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

- Total tracked papers: **873**
- Last generated: **2026-08-06**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **738**
- OpenReview: **130**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-06 | OpenReview | [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](content/papers/profile-graph-memory-for-llm-agents-implicit-cross-entity-traversal-through-narr.md) | agent, benchmark, compression |
| 2026-08-05 | OpenReview | [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](content/papers/caching-for-the-future-scrub-jay-episodic-memory-principles-for-agent-memory-sys.md) | agent, benchmark, context |
| 2026-08-05 | OpenReview | [Beyond Retrieval: Analytic Memory for Multimodal Agents](content/papers/beyond-retrieval-analytic-memory-for-multimodal-agents.md) | agent, benchmark, context |
| 2026-08-04 | arXiv | [When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary](content/papers/when-memory-becomes-authority-benchmarking-authority-collapse-at-the-memory-cons.md) | agent, benchmark |
| 2026-08-04 | arXiv | [Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents](content/papers/verifiable-memory-learning-unified-memory-management-with-local-and-global-verif.md) | agent, benchmark, context |
| 2026-08-04 | arXiv | [TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents](content/papers/tarl-transaction-aware-reliable-ledgers-for-executable-memory-management-in-long.md) | agent, benchmark, long-term |
| 2026-08-04 | arXiv | [SPEAR: Code-Augmented Agentic Prompt Optimization](content/papers/spear-code-augmented-agentic-prompt-optimization.md) | agent, context, conversation |
| 2026-08-04 | arXiv | [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States](content/papers/romerl-balancing-feedback-coverage-and-the-memory-reward-trap-in-self-evolving-a.md) | agent |
| 2026-08-04 | OpenReview | [Reason Before Remembering: An Entity-Centric Framework for Trustworthy Conversational Memory](content/papers/reason-before-remembering-an-entity-centric-framework-for-trustworthy-conversati.md) | context, conversation, retrieval |
| 2026-08-04 | OpenReview | [Position: Task-Triggered Memory Evolution Can Destroy Memories with High Long-Term Utility](content/papers/position-task-triggered-memory-evolution-can-destroy-memories-with-high-long-ter.md) | agent, episodic, long-term |
| 2026-08-04 | arXiv | [OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery](content/papers/or-agent-bridging-evolutionary-search-and-structured-research-for-automated-algo.md) | agent, compression, long-term |
| 2026-08-04 | arXiv | [Metis: Memory Foundation Model](content/papers/metis-memory-foundation-model.md) | agent |
| 2026-08-04 | OpenReview | [Memory-Bench at Short Context: Only Persistent Memory Beats Softmax Attention at 2048 Tokens](content/papers/memory-bench-at-short-context-only-persistent-memory-beats-softmax-attention-at-.md) | context |
| 2026-08-04 | arXiv | [MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents](content/papers/mafia-query-only-memory-attacks-via-probing-and-factual-injection-against-audite.md) | agent, context, retrieval |
| 2026-08-04 | arXiv | [LeanMem: Simple and Efficient Long-Term Memory for LLM Agents](content/papers/leanmem-simple-and-efficient-long-term-memory-for-llm-agents.md) | agent, long-term, retrieval |
| 2026-08-04 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-08-04 | OpenReview | [ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models](content/papers/er-mia-black-box-adversarial-memory-injection-attacks-on-long-term-memory-augmen.md) | context, long-term, retrieval |
| 2026-08-04 | arXiv | [Distractor-Aware Truncation: Disentangling Context-Length Effects from Signal Loss in Long-Context LLM Benchmarks](content/papers/distractor-aware-truncation-disentangling-context-length-effects-from-signal-los.md) | benchmark, context, retrieval |
| 2026-08-04 | arXiv | [DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents](content/papers/dp-memview-a-memory-interface-for-attribute-level-transcript-privacy-in-long-ter.md) | agent, benchmark, long-term |
| 2026-08-04 | OpenReview | [D-ACR: Dialogue-Aware Context Retrieval for Long-Term Conversational Memory](content/papers/d-acr-dialogue-aware-context-retrieval-for-long-term-conversational-memory.md) | benchmark, context, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
