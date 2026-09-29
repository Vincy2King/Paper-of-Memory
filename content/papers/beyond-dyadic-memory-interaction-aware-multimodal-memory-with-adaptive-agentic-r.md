# Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.32522v1
- Published: 2026-09-26
- Updated: 2026-09-26
- Authors: Wenxu Jia, Xize Cheng, Zihan Zhang, Dongjie Fu, Linjun Li, Wenshi Chen, Yangyang Wu, Tao Jin
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.AI, cs.IR, cs.SD, eess.AS
- URL: http://arxiv.org/abs/2609.32522v1

## One-Sentence Summary
Long-term memory enables agents to accumulate information and reason across sessions, yet existing research primarily focuses on dyadic text or image-text conversations, leaving...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory enables agents to accumulate information and reason across sessions, yet existing research primarily focuses on dyadic text or image-text conversations, leaving long-term memory for multi-party spoken...

进一步看，论文的核心做法或实验重点可以概括为：This setting requires preserving conversational content, identifying participants across sessions, and retaining who speaks to whom.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：cs.AI, cs.IR, cs.SD, eess.AS

## Abstract Snapshot
Long-term memory enables agents to accumulate information and reason across sessions, yet existing research primarily focuses on dyadic text or image-text conversations, leaving long-term memory for multi-party spoken conversations underexplored. This setting requires preserving conversational content, identifying participants across sessions, and retaining who speaks to whom. To this end, we propose VoxPolyMem, an interaction-aware multimodal memory framework combining incremental speaker identification with a memory hierarchy comprising interaction memory, fact memory, and participant profiles. We formulate retrieval as sequential decision-making, where an agent rewrites queries and selects retrieval tools and memory layers based on accumulated evidence to address information gaps. We further introduce Evidence-Gain GRPO (EG-GRPO), which uses round-wise credit assignment to encourage complementary evidence acquisition. We also construct VoxPolyBench to evaluate memory evolution, personalized answering, memory retrieval and reasoning, and interaction reasoning and attribution in multi-party spoken conversations. VoxPolyMem achieves an overall score of 85.0 on VoxPolyBench, surpassing the strongest evaluated baseline by 23.6 points. On Mem-Gallery and H2HMem-Multi, it scores 89.6 and 74.4, respectively, exceeding the strongest evaluated public memory baselines by over 8 points each. These results highlight its potential for persistent, personalized assistance in multi-party multimodal interactions. Code and datasets are available at https://voxpolymem.github.io/VoxPolyBench/demo/

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
