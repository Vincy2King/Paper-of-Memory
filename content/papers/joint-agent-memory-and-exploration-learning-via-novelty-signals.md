# Joint Agent Memory and Exploration Learning via Novelty Signals

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.01528v1
- Published: 2026-06-01
- Updated: 2026-06-01
- Authors: Shizuo Tian, Xiaohong Weng, Rui Kong, Yuxuan Chen, Guohong Liu, Yuebing Song, Jiacheng Liu, Yuchen Li, Dawei Yin, Ting Cao, Yunxin Liu, Yuanchun Li
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2606.01528v1

## One-Sentence Summary
In open-ended environments, exploration is fundamental for autonomous agents, yet current language model agents struggle with this.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In open-ended environments, exploration is fundamental for autonomous agents, yet current language model agents struggle with this.

进一步看，论文的核心做法或实验重点可以概括为：Effective exploration requires memory, but retaining raw interaction histories is computationally expensive over long trajectories.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
In open-ended environments, exploration is fundamental for autonomous agents, yet current language model agents struggle with this. Effective exploration requires memory, but retaining raw interaction histories is computationally expensive over long trajectories. While latent memory offers a solution to compress interaction histories, its training lacks reliable supervisory signals. We introduce \textbf{J}oint \textbf{A}gent \textbf{M}emory and \textbf{E}xploration \textbf{L}earning (\textbf{JAMEL}), a framework that trains agentic memory and exploration policy together through novelty-driven interaction. We observe that memory and exploration form a mutually dependent loop: sustained exploration requires memory to distinguish exhausted behaviors from unseen ones, while novelty-seeking interaction provides the supervision needed to make memory useful for future exploration. By utilizing deterministic and persistent novelty signals such as code coverage in the GUI domain, we provide natural, annotation-free supervision for the memory module. Empirical evaluations demonstrate that \ours successfully generalizes to unseen environments. Its exploration capability outperforms open-weight baselines and rivals the exploration depth of a closed-source model while reducing token consumption. Our code and model are open-sourced at https://github.com/MobileLLM/JAMEL.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
