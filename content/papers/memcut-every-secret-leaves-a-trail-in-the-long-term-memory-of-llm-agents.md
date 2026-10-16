# MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.21405v1
- Published: 2026-10-15
- Updated: 2026-10-15
- Authors: Cheng Zhang, Xuanning Cao, Zhicheng Zheng, Hui Xiong
- Tags: agent, benchmark, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.21405v1

## One-Sentence Summary
Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently.

进一步看，论文的核心做法或实验重点可以概括为：However, a dependable memory system must also forget sensitive user data upon request.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, conversation, long-term, retrieval
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently. However, a dependable memory system must also forget sensitive user data upon request. To evaluate this capability, we introduce MemCut, a systematic benchmark for user-requested forgetting. Its 456 hand-designed secrets in long-horizon conversations have fully annotated evidence trails to test recovery after deletion, including from messages that never state the secrets directly. We propose two recovery metrics. Native recovery measures reader success through the system's retrieval, whereas residual recovery measures the same reader's success when directly given surviving objects traced to annotated disclosures or evidence. We establish three reference deletion baselines to test how far existing retrievers and write models support forgetting across five memory designs and four LLMs. Disclosure removal reduces native recovery far more than residual recovery. LLM-guided deletion of ten additional turns from twenty retrieval candidates leaves 39-76% residual recovery. Subset sweeps (144 facts, three systems, two models) show that widening the pool at a fixed budget reduces residual recovery more than deleting all original candidates. These sweeps identify candidate coverage as a bottleneck in the reference baselines.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
