# Enhancing Group Recommendation with Memory-Augmented Reasoning in LLM Agent

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.21939v1
- Published: 2026-08-22
- Updated: 2026-08-22
- Authors: Qimeng Niu, Bowen Hao, Zixuan Zhang, Shuyu Qu, Hongzhi Yin
- Tags: agent, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2608.21939v1

## One-Sentence Summary
The core challenge in group recommendation lies in modeling the dynamic evolution of user preferences and explain?ing the consensus formation process.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：The core challenge in group recommendation lies in modeling the dynamic evolution of user preferences and explain?ing the consensus formation process.

进一步看，论文的核心做法或实验重点可以概括为：Existing Large Language Model (LLM)-based methods, despite improved interpretability, treat interaction history as fixed text, ignoring the natural evolution of group/user preferences over time, and lacking explicit...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.IR

## Abstract Snapshot
The core challenge in group recommendation lies in modeling the dynamic evolution of user preferences and explain?ing the consensus formation process. Existing Large Language Model (LLM)-based methods, despite improved interpretability, treat interaction history as fixed text, ignoring the natural evolution of group/user preferences over time, and lacking explicit modeling of the complex group decision-making process. To address these issues, we propose AGR, a LLM-based agent, which consists of a Memory Module and a Reasoning Module. The Memory Module employs a token-based hash table to dynamically manage the historical interactions of groups and users. This design supports fundamental operations including insertion, updating, retrieval, forgetting of irrelevant records, and summarization of evolving group and user profiles for efficiently tracking. Based on these retrieved dynamic profiles, the Reason?ing Module then performs a multi-step reasoning process includ?ing Group Interests Collection, Group Consensus Refinement, Multi-dimensional Evaluation and Explainable Recommendation Generation, thereby moving beyond black-box inference to de?liver fully interpretable recommendations. In practice, we adopt the Reinforcement Fine-Tuning (RFT) paradigm, where we first use Supervised Fine-Tuning (SFT) to equip the model with basic capabilities for invoking the Memory and Reasoning modules, and then employ Group Relative Policy Optimization (GRPO) to enhance its autonomous ability to coordinate these modules. Experiments on LastFM and Douban datasets demonstrate that AGR significantly outperforms existing state-of-the-art methods in both recommendation accuracy and explainability. Our model is open-sourced at https://huggingface.co/niuqimeng/AGR.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
