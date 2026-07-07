# Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.04391v1
- Published: 2026-07-05
- Updated: 2026-07-05
- Authors: Serge Lacasse, Jérémie Hatier, Alex Baker
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.CL
- URL: http://arxiv.org/abs/2607.04391v1

## One-Sentence Summary
Long-term memory remains a structural weakness of AI agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory remains a structural weakness of AI agents.

进一步看，论文的核心做法或实验重点可以概括为：The dominant approach, retrieval-augmented generation (RAG), relies on embedding-based similarity search, which is opaque by construction, difficult to audit, and bounded by the theoretical limits of vector...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Long-term memory remains a structural weakness of AI agents. The dominant approach, retrieval-augmented generation (RAG), relies on embedding-based similarity search, which is opaque by construction, difficult to audit, and bounded by the theoretical limits of vector representations. We present the Memory-Orchestrated Semantic System (MOSS), an agentic memory architecture in which the agent drives retrieval over a structured relational database. MOSS is model-agnostic, storage-agnostic, and API-agnostic: it runs on any relational engine, connects to any LLM provider (or to deterministic non-LLM processes), and deploys on any infrastructure, local or cloud. Its retrieval execution is symbolic and reproducible (once a query is formulated, no LLM participates in the retrieval loop) and every step of the system, from indexing to answer formulation, is logged and inspectable, making MOSS auditable by construction. Rather than imposing an external ontology, MOSS derives its conceptual vocabulary from the corpus itself. We report on a longitudinal deployment unique in the agentic-memory literature: a year of continuous production over an individual scholar's working corpus--a conversational corpus reaching back to October 2024 (some 44 million tokens, retroactively indexed) comprising 110,183 segments, alongside 163,494 catalogued documents, 569 inductively derived concepts, 322,662 concept annotations, and eleven metadata graphs totaling approximately five million relations--across four successive infrastructure generations. While the present case is that of a single researcher, the architecture is in no way specific to one person: it serves a team, an institution, or any entity that accumulates knowledge over time. We argue that auditable, sovereign, structurally unbounded memory is a precondition for AI agents intended to accompany a person or an organization over years rather than sessions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
