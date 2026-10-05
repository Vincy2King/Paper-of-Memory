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

- Total tracked papers: **1290**
- Last generated: **2026-10-05**

## Papers by Source

- ACL Anthology: **6**
- arXiv: **1138**
- OpenReview: **146**

## Latest Papers

| Date | Source | Paper | Tags |
| --- | --- | --- | --- |
| 2026-10-02 | arXiv | [Interpreting at Write Time: A Policy Ablation for Multi-Goal Agent Memory](content/papers/interpreting-at-write-time-a-policy-ablation-for-multi-goal-agent-memory.md) | agent |
| 2026-10-02 | arXiv | [DyadMem: A Long-Term Memory Benchmark of How Agents Work with Users](content/papers/dyadmem-a-long-term-memory-benchmark-of-how-agents-work-with-users.md) | agent, benchmark, long-term |
| 2026-10-02 | arXiv | [Decoupling Memory from Context: Structured Memory for Token-Efficient Test-Time Continual Learning](content/papers/decoupling-memory-from-context-structured-memory-for-token-efficient-test-time-c.md) | agent, context, retrieval |
| 2026-10-02 | arXiv | [Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval](content/papers/causal-memory-policy-making-memory-utility-identifiable-by-intervening-on-retrie.md) | context, retrieval |
| 2026-10-02 | arXiv | [Auditing Long-Term Memory Evaluation: Repeated Judging, Reader Variation, and Negative Controls](content/papers/auditing-long-term-memory-evaluation-repeated-judging-reader-variation-and-negat.md) | long-term, retrieval |
| 2026-10-01 | arXiv | [Typological Alignment of Stack-Based Language Models on Mildly Context-Sensitive Artificial Languages](content/papers/typological-alignment-of-stack-based-language-models-on-mildly-context-sensitive.md) | context |
| 2026-10-01 | arXiv | [The Surprising Effectiveness of Shared Memory in Looped Transformers](content/papers/the-surprising-effectiveness-of-shared-memory-in-looped-transformers.md) | context |
| 2026-10-01 | arXiv | [TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories](content/papers/taggraph-tag-augmented-graphs-for-graph-retrieval-of-agent-persistent-histories.md) | agent, conversation, long-term |
| 2026-10-01 | arXiv | [Role-aware Heuristic Episodic Attention for Conversational LLMs](content/papers/role-aware-heuristic-episodic-attention-for-conversational-llms.md) | context, conversation, episodic |
| 2026-10-01 | arXiv | [Rethinking World Models for Safety-Critical Embodied Systems](content/papers/rethinking-world-models-for-safety-critical-embodied-systems.md) | episodic |
| 2026-10-01 | arXiv | [Pincer: Resource Authorization for Agents using a Digital Twin](content/papers/pincer-resource-authorization-for-agents-using-a-digital-twin.md) | agent, context |
| 2026-10-01 | arXiv | [MemFit: Efficient Long-Term Agentic Memory](content/papers/memfit-efficient-long-term-agentic-memory.md) | agent, benchmark, compression |
| 2026-10-01 | arXiv | [Madeleine: Learning Involuntary Recall for Conversational Memory from Simulated Lives](content/papers/madeleine-learning-involuntary-recall-for-conversational-memory-from-simulated-l.md) | context, conversation, long-term |
| 2026-10-01 | arXiv | [Harnessing LLMs as Agents: What Does It Cost?](content/papers/harnessing-llms-as-agents-what-does-it-cost.md) | agent, context |
| 2026-10-01 | arXiv | [From Knowledge Access to Source Learning: Developing Source-Specific Competence](content/papers/from-knowledge-access-to-source-learning-developing-source-specific-competence.md) | agent, benchmark |
| 2026-10-01 | arXiv | [Decision Titan: Test-Time Training for Long-Term Memory in Offline Reinforcement Learning](content/papers/decision-titan-test-time-training-for-long-term-memory-in-offline-reinforcement-.md) | context, episodic, long-term |
| 2026-10-01 | arXiv | [Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval](content/papers/causal-memory-policy-making-memory-utility-identifiable-by-intervening-on-retrie.md) | context, retrieval |
| 2026-10-01 | arXiv | [Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds](content/papers/beyond-the-remembered-world-predictive-4d-belief-for-persistent-navigation-in-ev.md) | agent, benchmark, retrieval |
| 2026-10-01 | arXiv | [AgentWebRec: Compact Evidence Fusion over the Agent Web for Personalized Recommendation](content/papers/agentwebrec-compact-evidence-fusion-over-the-agent-web-for-personalized-recommen.md) | agent |
| 2026-10-01 | arXiv | [APDMem: Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory](content/papers/apdmem-agent-controlled-progressive-disclosure-for-query-adaptive-long-term-memo.md) | agent, context, conversation |

## Suggested GitHub Setup

- Create a public repo named `memory-papers-tracker` or similar.
- Push this folder as the repo root.
- Enable GitHub Actions.
- Optionally protect `main` and review automated PRs instead of direct commits.

## Next Extensions

- Add OpenAlex or Semantic Scholar for broader metadata coverage.
- Use an LLM to rewrite the introduction into smoother Chinese prose.
- Build topic pages such as `benchmark.md`, `agent-memory.md`, or `long-context.md`.
