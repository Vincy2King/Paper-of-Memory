# MemHarness: Memory Is Reconstructed, Not Replayed

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.28272v1
- Published: 2026-07-30
- Updated: 2026-07-30
- Authors: Rong Wu, Daocheng Fu, Licheng Wen, Xuemeng Yang, Shu Zou, Jianbiao Mei, Yuxin Wang, Hairong Zhang, Yu Yang, Tao Hu, Cong Zhang, Botian Shi, Pinlong Cai
- Tags: agent, context
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.28272v1

## One-Sentence Summary
Retrieving past experiences has become a common strategy to enhance large language model agents.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Retrieving past experiences has become a common strategy to enhance large language model agents.

进一步看，论文的核心做法或实验重点可以概括为：However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Retrieving past experiences has become a common strategy to enhance large language model agents. However, most existing memory-augmented agents treat retrieved experiences as static records to be replayed verbatim, injecting them into the context regardless of whether they align with the agent's current situation. This ``replay'' paradigm ignores the gap between the abstract, general nature of stored experience and the concrete, ever-changing states encountered at decision time, frequently causing negative transfer. In contrast, humans rarely recall past experiences verbatim; instead, they reorganize and adapt retrieved memories to fit the present context. Inspired by this, we propose MemHarness, a framework that equips LLM agents to actively harness and reconstruct past experiences based on the present context. At each decision step, a unified policy model critiques and reconstructs the retrieved experience conditioned on the current state, producing context-grounded guidance before acting. This reconstructive ability emerges naturally through end-to-end training with GRPO. Experiments on ALFWorld and WebShop show that MemHarness substantially outperforms pure RL and static memory-augmented baselines, demonstrating strong robustness in out-of-distribution (OOD) scenarios. Furthermore, our analyses reveal that this reconstruction objective not only prevents negative transfer but also serves as latent guidance during training, fundamentally improving the agent's intrinsic reasoning capabilities.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
