# Beyond Similarity: Trustworthy Memory Search for Personal AI Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.06054v1
- Published: 2026-06-04
- Updated: 2026-06-04
- Authors: Jiawen Zhang, Kejia Chen, Jiachen Ma, Yangfan Hu, Lipeng He, Yechao Zhang, Jian Liu, Xiaohu Yang, Tianwei Zhang, Ruoxi Jia
- Tags: agent, context, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.06054v1

## One-Sentence Summary
Personal AI agents increasingly rely on long-term memory to provide persistent personalization across sessions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal AI agents increasingly rely on long-term memory to provide persistent personalization across sessions.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory pipelines are largely driven by semantic similarity: memory data close to the current query is retrieved and injected into the model context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：agent memory, long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Personal AI agents increasingly rely on long-term memory to provide persistent personalization across sessions. However, existing memory pipelines are largely driven by semantic similarity: memory data close to the current query is retrieved and injected into the model context. This creates a critical trustworthiness gap, since a semantically related memory may still be contextually inappropriate, leading to threats such as cross-domain leakage, sycophancy, tool-call drift, or memory-induced jailbreaks. In this paper, we study memory search as a trust boundary in personal AI agents. We evaluate representative agentic memory frameworks, including A-Mem, Mem0, and MemOS, together with OpenClaw, a real-world personal-agent environment with persistent state and tool-use capability. Our results show that long-term memory is not merely a utility layer, but a durable control channel that can reshape how agents interpret tasks and execute actions, leaving them highly susceptible to the aforementioned threats. To mitigate these vulnerabilities, we propose MemGate, a lightweight and deployable memory plug-in for trustworthy memory search, with only 9M parameters and a 35.1MB footprint. MemGate is inserted between the vector memory store and the backbone LLM, requiring no LLM modification, memory-database rewriting, or inference-time LLM judge. It applies a query-conditioned neural gate to candidate memory representations, turning raw similarity search into task-conditioned memory admission. Across multiple mainstream memory frameworks, real-world agent settings, and diverse LLM backbones, MemGate reduces memory-induced threats while preserving long-term memory utility.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
