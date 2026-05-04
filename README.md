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

- Total tracked papers: **108**
- Last generated: **2026-05-04**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **76**
- OpenReview: **31**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-03 | OpenReview | [From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents](content/papers/from-single-to-multi-granularity-toward-long-term-memory-association-and-selecti.md) | agent, benchmark, context |
| 2026-05-01 | arXiv | [Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory](content/papers/learning-how-and-what-to-memorize-cognition-inspired-two-stage-optimization-for-.md) | agent, benchmark, context |
| 2026-05-01 | arXiv | [HyMem: Hybrid Memory Architecture with Dynamic Retrieval Scheduling](content/papers/hymem-hybrid-memory-architecture-with-dynamic-retrieval-scheduling.md) | agent, benchmark, compression |
| 2026-05-01 | arXiv | [From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction](content/papers/from-unstructured-recall-to-schema-grounded-memory-reliable-ai-memory-via-iterat.md) | agent, benchmark, context |
| 2026-04-30 | arXiv | [Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents](content/papers/learning-when-to-remember-risk-sensitive-contextual-bandits-for-abstention-aware.md) | agent, context, retrieval |
| 2026-04-30 | arXiv | [From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction](content/papers/from-unstructured-recall-to-schema-grounded-memory-reliable-ai-memory-via-iterat.md) | agent, benchmark, context |
| 2026-04-30 | arXiv | [Exploring Interaction Paradigms for LLM Agents in Scientific Visualization](content/papers/exploring-interaction-paradigms-for-llm-agents-in-scientific-visualization.md) | agent, benchmark, context |
| 2026-04-30 | arXiv | [EviMem: Evidence-Gap-Driven Iterative Retrieval for Long-Term Conversational Memory](content/papers/evimem-evidence-gap-driven-iterative-retrieval-for-long-term-conversational-memo.md) | conversation, long-term, retrieval |
| 2026-04-30 | arXiv | [Event-Centric World Modeling with Memory-Augmented Retrieval for Embodied Decision-Making](content/papers/event-centric-world-modeling-with-memory-augmented-retrieval-for-embodied-decisi.md) | agent, retrieval |
| 2026-04-30 | arXiv | [Contextual Agentic Memory is a Memo, Not True Memory](content/papers/contextual-agentic-memory-is-a-memo-not-true-memory.md) | agent, benchmark, context |
| 2026-04-30 | arXiv | [Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](content/papers/agentic-harness-engineering-observability-driven-automatic-evolution-of-coding-a.md) | agent, benchmark, long-term |
| 2026-04-29 | arXiv | [When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents](content/papers/when-continual-learning-moves-to-memory-a-study-of-experience-reuse-in-llm-agent.md) | agent, context, retrieval |
| 2026-04-29 | arXiv | [StratMem-Bench: Evaluating Strategic Memory Use in Virtual Character Conversation Beyond Factual Recall](content/papers/stratmem-bench-evaluating-strategic-memory-use-in-virtual-character-conversation.md) | benchmark, conversation, long-term |
| 2026-04-29 | arXiv | [OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory](content/papers/ocr-memory-optical-context-retrieval-for-long-horizon-agent-memory.md) | agent, benchmark, context |
| 2026-04-29 | arXiv | [MemOVCD: Training-Free Open-Vocabulary Change Detection via Cross-Temporal Memory Reasoning and Global-Local Adaptive Rectification](content/papers/memovcd-training-free-open-vocabulary-change-detection-via-cross-temporal-memory.md) | benchmark |
| 2026-04-29 | arXiv | [Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent](content/papers/hierarchical-long-term-semantic-memory-for-linkedin-s-hiring-agent.md) | agent, context, long-term |
| 2026-04-29 | arXiv | [Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture](content/papers/detecting-clinical-discrepancies-in-health-coaching-agents-a-dual-stream-memory-.md) | agent, conversation |
| 2026-04-29 | arXiv | [A Dual-Task Paradigm to Investigate Sentence Comprehension Strategies in Language Models](content/papers/a-dual-task-paradigm-to-investigate-sentence-comprehension-strategies-in-languag.md) | working memory |
| 2026-04-28 | arXiv | [PsychAgent: An Experience-Driven Lifelong Learning Agent for Self-Evolving Psychological Counselor](content/papers/psychagent-an-experience-driven-lifelong-learning-agent-for-self-evolving-psycho.md) | agent |
| 2026-04-28 | OpenReview | [PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](content/papers/plugmem-a-task-agnostic-plugin-memory-module-for-llm-agents.md) | agent, benchmark, context |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
