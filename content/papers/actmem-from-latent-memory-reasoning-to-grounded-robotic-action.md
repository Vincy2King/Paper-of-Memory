# ActMem: From Latent Memory Reasoning to Grounded Robotic Action

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.25461v1
- Published: 2026-11-19
- Updated: 2026-11-19
- Authors: Linfeng Dong, Jianwei Niu, Jiuyi Zhao, Ruibing Feng, Xinghao Wu, Wu Yang, Shuai Tao, Wulong Liu, Mu Li
- Tags: context
- Categories: cs.CV, cs.LG
- URL: http://arxiv.org/abs/2611.25461v1

## One-Sentence Summary
Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role.

## Introduction
这篇论文被纳入仓库，是因为它和 `context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role.

进一步看，论文的核心做法或实验重点可以概括为：However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full history in a shared context where it crowds out current perception.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：context
- 检索关键词命中：context memory, memory augmented, memory reasoning, memory-augmented
- 来源分类信息：cs.CV, cs.LG

## Abstract Snapshot
Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role. However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past experience to decide what to do, while perception guides how to act. We therefore propose ActMem, an in-context memory framework that decouples memory reasoning from perceptual grounding within a single vision-language backbone. Built on a vision-language model with native video understanding, ActMem infers the current subtask from a timestamped interaction history and keeps the hidden states formed during this inference as a Latent Memory Chain-of-Thought (Memory CoT), which conditions a flow-matching action expert. Perception Attention further lets the expert attend directly to the current view. To keep inference fast under long histories, Efficient Memory CoT Inference reuses computation across consecutive decisions without changing the output. ActMem achieves 71.1% task success and 80.8% completion success on RoboMemArena, surpassing the strongest baseline by 7.5 and 8.7 percentage points, and 73.8% average success on MIKASA-Robo, the best among all compared methods. In the real world, it reaches 68.8% average success on exogenous, endogenous, and traceless memory tasks, 10.0 percentage points above the strongest memory-augmented VLA. Code and checkpoints will be released at https://github.com/LigphiDonk/ActMem and https://huggingface.co/donk111/ActMem.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
