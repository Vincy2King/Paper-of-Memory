# MNC: Scope-Bound Semantic Declassification for Private LLM-Agent Communication

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01719v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Jinghan Xu, Longze Fan, Zeyuan Wang, Xinjin Li, Hankai Liu
- Tags: agent, retrieval
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2608.01719v1

## One-Sentence Summary
Multi-agent large language model (LLM) systems can expose protected state through internal messages, tool arguments, logs, and persistent memory even when their public outputs...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Multi-agent large language model (LLM) systems can expose protected state through internal messages, tool arguments, logs, and persistent memory even when their public outputs appear innocuous.

进一步看，论文的核心做法或实验重点可以概括为：Existing privacy prompts, redaction methods, and source-level access controls restrict surface content or data access, but do not specify what a legitimately informed agent should disclose or how that disclosure may...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory retrieval, persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Multi-agent large language model (LLM) systems can expose protected state through internal messages, tool arguments, logs, and persistent memory even when their public outputs appear innocuous. Existing privacy prompts, redaction methods, and source-level access controls restrict surface content or data access, but do not specify what a legitimately informed agent should disclose or how that disclosure may be reused downstream. We introduce Minimum-Necessary Communication (MNC), a typed semantic-declassification protocol that selects a task-sufficient disclosure from an application-authored candidate family and binds it to explicit recipient, purpose, forwarding, lifetime, logging, and memory scopes. A reference monitor enforces these scopes across subsequent operations, while a history-aware extension accounts for inference risk accumulated over repeated disclosures. Controlled semantic-join, memory, probing, and longitudinal experiments show that conventional defenses can preserve protocol-level utility while exposing substantial additional inference signal. Under identical receipt text, MNC preserves authorized delivery while blocking unauthorized forwarding, logging, durable storage, and retrieval after expiration that a text-only semantic declassifier permits. Two-backbone MAGPIE executions further show that mediated disclosures propagate through subsequent planning, tool use, coordination, and memory retrieval. These results support scope-bound semantic declassification as a practical communication boundary for private LLM-agent systems.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
