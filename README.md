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

- Total tracked papers: **1047**
- Last generated: **2026-09-01**

## Papers by Source

- ACL Anthology: **5**
- arXiv: **900**
- OpenReview: **142**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-08-31 | OpenReview | [D-ACR: Dialogue-Aware Context Retrieval for Long-Term Conversational Memory](content/papers/d-acr-dialogue-aware-context-retrieval-for-long-term-conversational-memory.md) | benchmark, context, conversation |
| 2026-08-30 | OpenReview | [Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents](content/papers/memory-makes-the-difference-evaluating-how-different-memory-roles-shape-conversa.md) | agent, context, conversation |
| 2026-08-30 | OpenReview | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](content/papers/knowledge-graph-enhanced-memory-augmented-retrieval-for-long-context-modeling.md) | context, retrieval |
| 2026-08-30 | OpenReview | [Geometry-Conditioned Turn Scoring for Conversational Memory Compression](content/papers/geometry-conditioned-turn-scoring-for-conversational-memory-compression.md) | benchmark, compression, context |
| 2026-08-29 | OpenReview | [Reason Before Remembering: An Entity-Centric Framework for Trustworthy Conversational Memory](content/papers/reason-before-remembering-an-entity-centric-framework-for-trustworthy-conversati.md) | context, conversation, retrieval |
| 2026-08-29 | OpenReview | [MemoryVLN: Memory-Augmented Vision-Language Navigation](content/papers/memoryvln-memory-augmented-vision-language-navigation.md) | agent, benchmark, context |
| 2026-08-28 | arXiv | [When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory](content/papers/when-stale-constraints-go-unchecked-budgeted-verification-failures-in-inherited-.md) | agent |
| 2026-08-28 | OpenReview | [When Should LLMs Use Behavioral Memory? Task-Dependent Retrieval for Personalized Long-Term Memory](content/papers/when-should-llms-use-behavioral-memory-task-dependent-retrieval-for-personalized.md) | long-term, retrieval |
| 2026-08-28 | arXiv | [What Makes Agent Memory Useful for Reliable Unanswerable Question Handling?](content/papers/what-makes-agent-memory-useful-for-reliable-unanswerable-question-handling.md) | agent |
| 2026-08-28 | OpenReview | [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](content/papers/profile-graph-memory-for-llm-agents-implicit-cross-entity-traversal-through-narr.md) | agent, benchmark, compression |
| 2026-08-28 | arXiv | [MAIL: Memory-driven, Adaptive, Incremental, and Literature-grounded Framework for Hypothesis Generation in Chemistry](content/papers/mail-memory-driven-adaptive-incremental-and-literature-grounded-framework-for-hy.md) | memory-augmented |
| 2026-08-28 | arXiv | [LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment](content/papers/llm-based-agents-for-software-and-systems-security-approaches-applications-and-a.md) | agent |
| 2026-08-28 | arXiv | [LINE Conversation History Retrieval for Personal Memory RAG: Evaluating Search Representations and Hybrid Retrieval](content/papers/line-conversation-history-retrieval-for-personal-memory-rag-evaluating-search-re.md) | conversation, retrieval |
| 2026-08-28 | arXiv | [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](content/papers/contextpilot-teaching-agents-for-proactive-context-management-via-fine-grained-r.md) | agent, benchmark, compression |
| 2026-08-27 | arXiv | [When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory](content/papers/when-stale-constraints-go-unchecked-budgeted-verification-failures-in-inherited-.md) | agent |
| 2026-08-27 | arXiv | [When Memory Takes Gradients: Collaborative Vector Memory for Agentic Recommender Systems](content/papers/when-memory-takes-gradients-collaborative-vector-memory-for-agentic-recommender-.md) | agent, benchmark, context |
| 2026-08-27 | arXiv | [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](content/papers/visa-agentic-self-evolving-data-synthesis-for-multimodal-instruction-following.md) | agent, benchmark |
| 2026-08-27 | arXiv | [GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory](content/papers/graphmemix-query-aware-evidence-forests-for-long-term-multimodal-agent-memory.md) | agent, benchmark, context |
| 2026-08-26 | arXiv | [When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory](content/papers/when-stale-constraints-go-unchecked-budgeted-verification-failures-in-inherited-.md) | agent |
| 2026-08-26 | arXiv | [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](content/papers/visa-agentic-self-evolving-data-synthesis-for-multimodal-instruction-following.md) | agent, benchmark |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
