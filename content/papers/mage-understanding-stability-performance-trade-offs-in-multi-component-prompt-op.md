# MAGE: Understanding Stability-Performance Trade-offs in Multi-component Prompt Optimization

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.11944v1
- Published: 2026-07-11
- Updated: 2026-07-11
- Authors: Prateek Singh
- Tags: episodic
- Categories: cs.CL, cs.LG
- URL: http://arxiv.org/abs/2607.11944v1

## One-Sentence Summary
How do different components of iterative prompt optimization interact, and what happens when they are combined?

## Introduction
这篇论文被纳入仓库，是因为它和 `episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：How do different components of iterative prompt optimization interact, and what happens when they are combined?

进一步看，论文的核心做法或实验重点可以概括为：We investigate this through MAGE (Memory-Augmented Goal-directed Prompt Evolution), a controlled analysis framework for studying component interaction in prompt optimization.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：episodic
- 检索关键词命中：episodic memory, memory augmented, memory-augmented
- 来源分类信息：cs.CL, cs.LG

## Abstract Snapshot
How do different components of iterative prompt optimization interact, and what happens when they are combined? We investigate this through MAGE (Memory-Augmented Goal-directed Prompt Evolution), a controlled analysis framework for studying component interaction in prompt optimization. MAGE is not proposed as a superior optimizer in absolute terms; it integrates episodic memory, multi-objective Pareto selection, and adaptive evaluation as a platform for controlled ablation. Our experiments uncover a previously unreported phenomenon, the Prompt Optimization Coupling Effect (POCE): when multiple stochastic optimization signals operate within a closed reflective loop, they interact in ways that simultaneously improve performance and amplify variance, behavior that cannot be predicted by analyzing components in isolation. Three main findings emerge. First, failure-grounded reflection is essential: methods relying only on scores (OPRO) or abstract critique (Self-Refine) fail to improve prompts. Second, MAGE achieves 46.4% versus GEPA's 34.0% on GSM8K-Hard (+12.4%, P(MAGE>GEPA)=0.998, 5 seeds on gpt-4o-mini), with comparable variance (7.3% vs. 7.0%). Third, increasing candidate diversity reveals the clearest POCE signal: expanding the candidate pool from n=3 to n=5 improves mean accuracy by +21.6% while increasing variance by 3.7x. We further validate on Llama 3.1 8B and show POCE is headroom-dependent: when the base model already achieves high accuracy, variance amplification disappears. Finally, in low-data regimes (Ntrain=30), well-designed fixed prompts outperform all reflective optimizers, indicating that scaffold choice dominates optimizer choice. Our results suggest prompt optimization systems behave as coupled stochastic processes and should be evaluated in terms of both performance and stability, not just peak accuracy.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
