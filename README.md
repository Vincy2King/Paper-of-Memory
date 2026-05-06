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

- Total tracked papers: **123**
- Last generated: **2026-05-06**

## Papers by Source

- ACL Anthology: **1**
- arXiv: **91**
- OpenReview: **31**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-05-05 | arXiv | [What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis](content/papers/what-happens-inside-agent-memory-circuit-analysis-from-emergence-to-diagnosis.md) | agent, context |
| 2026-05-05 | arXiv | [Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration](content/papers/trojan-hippo-weaponizing-agent-memory-for-data-exfiltration.md) | agent, benchmark, context |
| 2026-05-05 | arXiv | [ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting](content/papers/scrapmem-a-bio-inspired-framework-for-on-device-personalized-agent-memory-via-op.md) | agent, compression, episodic |
| 2026-05-05 | arXiv | [Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries](content/papers/effect-transparent-governance-for-ai-workflow-architectures-semantic-preservatio.md) | memory |
| 2026-05-04 | arXiv | [When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI](content/papers/when-agents-handle-secrets-a-survey-of-confidential-computing-for-agentic-ai.md) | agent, context |
| 2026-05-04 | arXiv | [The Dynamic Gist-Based Memory Model (DGMM): A Memory-Centric Architecture for Artificial Intelligence](content/papers/the-dynamic-gist-based-memory-model-dgmm-a-memory-centric-architecture-for-artif.md) | context, episodic, retrieval |
| 2026-05-04 | arXiv | [Recurrent Deep Reinforcement Learning for Chemotherapy Control under Partial Observability](content/papers/recurrent-deep-reinforcement-learning-for-chemotherapy-control-under-partial-obs.md) | benchmark |
| 2026-05-04 | arXiv | [MEMAUDIT: An Exact Package-Oracle Evaluation Protocol for Budgeted Long-Term LLM Memory Writing](content/papers/memaudit-an-exact-package-oracle-evaluation-protocol-for-budgeted-long-term-llm-.md) | agent, long-term, retrieval |
| 2026-05-04 | arXiv | [MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory](content/papers/mage-safeguarding-llm-agents-against-long-horizon-threats-via-shadow-memory.md) | agent, context |
| 2026-05-03 | arXiv | [WMF-AM: Probing LLM Working Memory via Depth-Parameterized Cumulative State Tracking](content/papers/wmf-am-probing-llm-working-memory-via-depth-parameterized-cumulative-state-track.md) | agent, benchmark |
| 2026-05-03 | arXiv | [Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration](content/papers/trojan-hippo-weaponizing-agent-memory-for-data-exfiltration.md) | agent, benchmark, context |
| 2026-05-03 | arXiv | [GRAVITY: Architecture-Agnostic Structured Anchoring for Long-Horizon Conversational Memory](content/papers/gravity-architecture-agnostic-structured-anchoring-for-long-horizon-conversation.md) | agent, benchmark, context |
| 2026-05-03 | OpenReview | [From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents](content/papers/from-single-to-multi-granularity-toward-long-term-memory-association-and-selecti.md) | agent, benchmark, context |
| 2026-05-02 | arXiv | [MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents](content/papers/memorai-memory-organization-and-retrieval-via-adaptive-graph-intelligence-for-ll.md) | agent, benchmark, compression |
| 2026-05-02 | arXiv | [Feedback-Normalized Developer Memory for Reinforcement-Learning Coding Agents: A Safety-Gated MCP Architecture](content/papers/feedback-normalized-developer-memory-for-reinforcement-learning-coding-agents-a-.md) | agent, benchmark, context |
| 2026-05-01 | arXiv | [Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory](content/papers/learning-how-and-what-to-memorize-cognition-inspired-two-stage-optimization-for-.md) | agent, benchmark, context |
| 2026-05-01 | arXiv | [HyMem: Hybrid Memory Architecture with Dynamic Retrieval Scheduling](content/papers/hymem-hybrid-memory-architecture-with-dynamic-retrieval-scheduling.md) | agent, benchmark, compression |
| 2026-05-01 | arXiv | [From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction](content/papers/from-unstructured-recall-to-schema-grounded-memory-reliable-ai-memory-via-iterat.md) | agent, benchmark, context |
| 2026-05-01 | arXiv | [Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries](content/papers/effect-transparent-governance-for-ai-workflow-architectures-semantic-preservatio.md) | memory |
| 2026-04-30 | arXiv | [Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents](content/papers/learning-when-to-remember-risk-sensitive-contextual-bandits-for-abstention-aware.md) | agent, context, retrieval |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
