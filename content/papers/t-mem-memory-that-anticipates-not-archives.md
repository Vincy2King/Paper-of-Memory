# T-Mem: Memory That Anticipates, Not Archives

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.15405v1
- Published: 2026-06-13
- Updated: 2026-06-13
- Authors: Weidong Guo, Dakai Wang, Zixuan Wang, Hui Liu, Yu Xu
- Tags: agent, context, conversation, episodic, long-term
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.15405v1

## One-Sentence Summary
Long-term memory is essential for conversational agents to remain coherent across extended dialogues, follow through on commitments made many sessions earlier, and adapt their...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term memory is essential for conversational agents to remain coherent across extended dialogues, follow through on commitments made many sessions earlier, and adapt their behaviour to each user.

进一步看，论文的核心做法或实验重点可以概括为：Current LLM-backed long-term conversational memory, however, is reachability-bounded by the similarity between a query and stored content, both lexical and dense-vector.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation, episodic, long-term
- 检索关键词命中：conversational memory, long-term memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-term memory is essential for conversational agents to remain coherent across extended dialogues, follow through on commitments made many sessions earlier, and adapt their behaviour to each user. Current LLM-backed long-term conversational memory, however, is reachability-bounded by the similarity between a query and stored content, both lexical and dense-vector. The approach is effective when query and memory share surface features such as wording or named entities (we call this descriptive). But it misses another, equally valuable class of cases, where query and memory do not share surface features and are tied only by a latent semantic arc (associative). On this regime prevailing long-term memory systems collectively fail. Covering this other half is what allows an assistant, for the first time, to actively draw on past dialogue as a semantic asset. On the memory side, this is the engineering counterpart of what cognitive science calls episodic future thinking: rehearsing past experience for the future contexts under which it will need to be found. We call these write-time rehearsals triggers. We propose T-Mem, the first long-term conversational memory architecture that covers both descriptive and associative recall. At each of two evidence granularities, single facts and full exchanges, T-Mem instantiates one descriptive trigger family and one associative trigger family, so that every memory remains reachable from both surface-similar and relevance-bound queries. As empirical validation, T-Mem reaches state-of-the-art on both LoCoMo and LoCoMo-Plus.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
