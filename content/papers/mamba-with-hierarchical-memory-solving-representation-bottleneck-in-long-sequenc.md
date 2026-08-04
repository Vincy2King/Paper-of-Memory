# Mamba with Hierarchical Memory: Solving Representation Bottleneck in Long Sequence Modeling

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.02347v1
- Published: 2026-08-03
- Updated: 2026-08-03
- Authors: Qinwen Wang, Jieping Luo, Aoxiang Qin, Ruoyu Zhao, Jianxiong Tang, Wei Zhang, Zhichao Lu, Luziwei Leng
- Tags: context, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.02347v1

## One-Sentence Summary
Recurrent linear attention models (RLAs) such as Mamba offer efficient linear-time sequence modeling as an alternative to Transformers, yet their fixed-capacity recurrent states...

## Introduction
这篇论文被纳入仓库，是因为它和 `context, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Recurrent linear attention models (RLAs) such as Mamba offer efficient linear-time sequence modeling as an alternative to Transformers, yet their fixed-capacity recurrent states limit long-sequence modeling.

进一步看，论文的核心做法或实验重点可以概括为：Drawing inspiration from hierarchical human memory, we propose Hierarchical Memory Mamba (HMM) to address this limitation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context, long-term, retrieval
- 检索关键词命中：long-term memory, working memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Recurrent linear attention models (RLAs) such as Mamba offer efficient linear-time sequence modeling as an alternative to Transformers, yet their fixed-capacity recurrent states limit long-sequence modeling. Drawing inspiration from hierarchical human memory, we propose Hierarchical Memory Mamba (HMM) to address this limitation. Building upon a pre-trained Mamba backbone, HMM integrates a lightweight working memory that extracts slow paragraph-level semantics (PLS) from the fast sensory memory embedded in the backbone's hidden states. The PLS is subsequently compressed into persistent long-term memory for task-relevant retrieval. The hierarchical processing of semantic information overcomes the representation bottleneck of RLAs and endows HMM cross-task generalization through parametric learning, which is not observed in other long-context enhanced Mamba variants. Evaluations on Passkey Retrieval and LongBench-E tasks demonstrate that HMM improves retrieval success by 34.3--37.1% and reasoning accuracy by 1.6--14.2% over strong Mamba-based models, while adding only 2% extra parameters and with minimal training overhead.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
