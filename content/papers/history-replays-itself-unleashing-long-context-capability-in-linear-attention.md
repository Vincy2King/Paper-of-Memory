# History Replays Itself: Unleashing Long-Context Capability in Linear Attention

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.15715v1
- Published: 2026-10-11
- Updated: 2026-10-11
- Authors: Li Nanbo, Firas Laakom, Yilan Zhang, Piotr Piękos, Yimeng Chen, Liangyu Wang, Yifan Xu, Mateusz Ostaszewski, Dandan Guo, Wenyi Wang, Yanning Dai, Yuhui Wang, Jürgen Schmidhuber
- Tags: agent, context, episodic, long-term, retrieval
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.15715v1

## One-Sentence Summary
Linear attention promises the efficiency needed for long-context language modelling, yet its fixed-size recurrent state must simultaneously support ongoing computation and...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, episodic, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Linear attention promises the efficiency needed for long-context language modelling, yet its fixed-size recurrent state must simultaneously support ongoing computation and preserve information from an ever-growing...

进一步看，论文的核心做法或实验重点可以概括为：This coupling has reinforced a prevailing view that the state's memory capacity defines the model's long-context capability.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, episodic, long-term, retrieval
- 检索关键词命中：episodic memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Linear attention promises the efficiency needed for long-context language modelling, yet its fixed-size recurrent state must simultaneously support ongoing computation and preserve information from an ever-growing history. This coupling has reinforced a prevailing view that the state's memory capacity defines the model's long-context capability. We challenge this presumed ceiling: \emph{recurrent computation need not bear the full burden of long-term storage}. We introduce NoteBank, a sparse episodic memory that archives selected text before future queries are known, uses the backbone's native features for writing and addressing, and reads retrieved evidence through its native forward computation via replay. This \emph{training-free, plug-and-play} interface requires no external embedding model, separately trained retriever, or separate neural reader. At one million tokens, it raises Gated DeltaNet's mean accuracy across six RULER retrieval tasks from 1.7% to 70.3%, with no observed significant retrieval degradation from 4K to 1M tokens. This recovery adds $\leqslant$0.025% to analytical FLOPs, with persistent context storage approximately 1/2,600 that of a Transformer's full MHA KV cache at matched width, depth, and precision. Experiments extend from three 1.3B recurrent backbones to Mamba-2-8B and post-trained Qwen3.5-9B, demonstrating gains on LongBench v1/v2 and MemoryAgentBench. Together, these results show that sparse evidence storage and native replay can substantially expand the long-context capability of pretrained linear attention models while retaining the efficiency of recurrent computation.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
