# The Sleeping Agent: What Gist-Based Context Compression Loses and Why

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.11775v1
- Published: 2026-08-12
- Updated: 2026-08-12
- Authors: Nicholas E. Kyrkewood
- Tags: agent, compression, context, conversation, retrieval
- Categories: cs.AI, cs.CL
- URL: http://arxiv.org/abs/2608.11775v1

## One-Sentence Summary
Gist-based context compression---summarising older conversation history into compact representations---is a common approach in long-horizon language model agents, yet its effect...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, compression, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Gist-based context compression---summarising older conversation history into compact representations---is a common approach in long-horizon language model agents, yet its effect on different types of memory retrieval...

进一步看，论文的核心做法或实验重点可以概括为：We use Salience-Weighted Consolidation (SWC), a biologically-inspired compression framework motivated by sleep-based memory consolidation, as a diagnostic probe to study when gist compression helps and when it hurts.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, compression, context, conversation, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：cs.AI, cs.CL

## Abstract Snapshot
Gist-based context compression---summarising older conversation history into compact representations---is a common approach in long-horizon language model agents, yet its effect on different types of memory retrieval is poorly understood. We use Salience-Weighted Consolidation (SWC), a biologically-inspired compression framework motivated by sleep-based memory consolidation, as a diagnostic probe to study when gist compression helps and when it hurts. SWC scores conversation history by salience, partitions it into priority tiers, and applies structured gist abstraction to mid-priority content. Evaluating four conditions on all ten LoCoMo conversations---1,935 matched text-only questions in total, 1,501 used in the primary aggregate after excluding Category 5 (adversarial) questions---at temperature 0, we find a consistent task-type interaction: gist compression substantially outperforms truncation on multi-hop reasoning and single-hop factual questions, but temporal questions remain substantially harder under compression, with compressed conditions scoring well below the full-context reference on the conversations where both are evaluated. We trace this failure to a specific mechanism: the gist abstraction prompt preserves relational and event structure while discarding dates and times. A preservation analysis across all ten conversations confirms the mechanism: an approximately 20-fold increase in temporal expression preservation (3.05% to 62.39%) with a one-sentence prompt modification, while named entity and event preservation rates barely change (x1.02 and x1.11), demonstrating that the fix is a precision instrument. The prompt modification recovers +0.314 [0.254, 0.375] judge accuracy on category-2 (temporal) questions in the matched set. Code and results: https://github.com/kyrkewood/sleeping-agent.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
