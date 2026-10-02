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

- Total tracked papers: **1281**
- Last generated: **2026-10-02**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1129**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-01 | arXiv | [Typological Alignment of Stack-Based Language Models on Mildly Context-Sensitive Artificial Languages](content/papers/typological-alignment-of-stack-based-language-models-on-mildly-context-sensitive.md) | context |
| 2026-10-01 | arXiv | [TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories](content/papers/taggraph-tag-augmented-graphs-for-graph-retrieval-of-agent-persistent-histories.md) | agent, conversation, long-term |
| 2026-10-01 | arXiv | [Role-aware Heuristic Episodic Attention for Conversational LLMs](content/papers/role-aware-heuristic-episodic-attention-for-conversational-llms.md) | context, conversation, episodic |
| 2026-10-01 | arXiv | [Rethinking World Models for Safety-Critical Embodied Systems](content/papers/rethinking-world-models-for-safety-critical-embodied-systems.md) | episodic |
| 2026-10-01 | arXiv | [MemFit: Efficient Long-Term Agentic Memory](content/papers/memfit-efficient-long-term-agentic-memory.md) | agent, benchmark, compression |
| 2026-10-01 | arXiv | [Madeleine: Learning Involuntary Recall for Conversational Memory from Simulated Lives](content/papers/madeleine-learning-involuntary-recall-for-conversational-memory-from-simulated-l.md) | context, conversation, long-term |
| 2026-10-01 | arXiv | [From Knowledge Access to Source Learning: Developing Source-Specific Competence](content/papers/from-knowledge-access-to-source-learning-developing-source-specific-competence.md) | agent, benchmark |
| 2026-10-01 | arXiv | [Decision Titan: Test-Time Training for Long-Term Memory in Offline Reinforcement Learning](content/papers/decision-titan-test-time-training-for-long-term-memory-in-offline-reinforcement-.md) | context, episodic, long-term |
| 2026-10-01 | arXiv | [Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval](content/papers/causal-memory-policy-making-memory-utility-identifiable-by-intervening-on-retrie.md) | context, retrieval |
| 2026-10-01 | arXiv | [Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds](content/papers/beyond-the-remembered-world-predictive-4d-belief-for-persistent-navigation-in-ev.md) | agent, benchmark, retrieval |
| 2026-10-01 | arXiv | [AgentWebRec: Compact Evidence Fusion over the Agent Web for Personalized Recommendation](content/papers/agentwebrec-compact-evidence-fusion-over-the-agent-web-for-personalized-recommen.md) | agent |
| 2026-09-30 | arXiv | [Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision](content/papers/workspace-models-lightweight-robotic-memory-via-saliency-driven-supervision.md) | long-term |
| 2026-09-30 | arXiv | [Who Said What, and Will It Be Remembered? Evaluating Persistent Speaker Attribution Across Meetings](content/papers/who-said-what-and-will-it-be-remembered-evaluating-persistent-speaker-attributio.md) | benchmark, conversation, long-term |
| 2026-09-30 | arXiv | [When Context Changes: Understanding Update Failures in LLMs](content/papers/when-context-changes-understanding-update-failures-in-llms.md) | agent, benchmark, context |
| 2026-09-30 | arXiv | [The Evolution of Attention in Large Language Models: Mechanisms, Trade-offs, and Emerging Trends](content/papers/the-evolution-of-attention-in-large-language-models-mechanisms-trade-offs-and-em.md) | compression, context |
| 2026-09-30 | arXiv | [MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories](content/papers/memlife-curating-and-reasoning-over-long-term-egocentric-video-memories.md) | agent, benchmark, long-term |
| 2026-09-30 | arXiv | [MemCodex: Self-Programming Hierarchical Memory for Language Agents](content/papers/memcodex-self-programming-hierarchical-memory-for-language-agents.md) | agent, context |
| 2026-09-30 | arXiv | [LongEmo: Towards Emotion Understanding and Reasoning in Long Videos](content/papers/longemo-towards-emotion-understanding-and-reasoning-in-long-videos.md) | agent, benchmark, episodic |
| 2026-09-30 | arXiv | [How Can Recommendation Feedback Evolve Agent Memory?](content/papers/how-can-recommendation-feedback-evolve-agent-memory.md) | agent, benchmark, context |
| 2026-09-30 | arXiv | [Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity](content/papers/harness-as-a-language-a-minimalist-agent-framework-with-maximal-expressivity.md) | agent, context, long-term |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
