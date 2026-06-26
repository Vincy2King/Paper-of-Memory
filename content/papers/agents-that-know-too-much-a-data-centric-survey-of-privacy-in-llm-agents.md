# Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.26627v1
- Published: 2026-06-25
- Updated: 2026-06-25
- Authors: Nada Lahjouji, Ashwin Gerard Colaco
- Tags: agent, benchmark, context, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2606.26627v1

## One-Sentence Summary
Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf.

进一步看，论文的核心做法或实验重点可以概括为：As they move from answering questions to operating over sensitive data, privacy becomes harder to enforce.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：agent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf. As they move from answering questions to operating over sensitive data, privacy becomes harder to enforce. An agent touches many data sources, runs multi-step workflows, keeps state across sessions, and acts with delegated permissions. Sensitive information can therefore leak not only through its final answer but through the queries it issues, the intermediate results it handles, the memory it writes, and the messages it exchanges with other agents. We survey the privacy of LLM agents from a data-centric view, organizing the field around the data an agent touches rather than by attack type, and we use data agent as shorthand for an LLM agent that works with data. Research on these risks is active but scattered across retrieval-augmented generation, text-to-SQL interfaces, agent memory, prompt injection, access control, and contextual privacy. This survey brings that work together: we taxonomize the data sources an agent touches, the privacy risks each source creates, and the governance mechanisms that address them; we map the benchmarks used to measure these risks and identify what is missing; and we set out the open problems. Two findings recur: among governance mechanisms only information-flow control covers both compositional and cross-session inference leakage, the two least-protected risks; and no benchmark drives an agent across its data surfaces under one privacy policy, the instrument the field most lacks. Our goal is a reference that situates the scattered literature and gives future work a common framing.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
