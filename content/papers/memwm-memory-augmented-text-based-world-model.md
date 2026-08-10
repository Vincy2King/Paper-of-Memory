# MemWM: Memory-Augmented Text-Based World Model

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.07107v1
- Published: 2026-08-07
- Updated: 2026-08-07
- Authors: Yujun Wang, Tao Zhang, Jinhe Bi, Aniri, Wenxuan Ye, Boliang Liu, Sikuan Yan, Shuning Wang, Xuebing Zhou, Sören Pirk, Hinrich Schütze, Yunpu Ma
- Tags: agent, benchmark
- Categories: cs.AI
- URL: http://arxiv.org/abs/2608.07107v1

## One-Sentence Summary
World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions.

进一步看，论文的核心做法或实验重点可以概括为：Yet fluent next-state predictions can still omit task-critical facts, corrupt product attributes, or apply incorrect transition rules.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：memory augmented, memory-augmented, retrieval memory
- 来源分类信息：cs.AI

## Abstract Snapshot
World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions. Yet fluent next-state predictions can still omit task-critical facts, corrupt product attributes, or apply incorrect transition rules. To address such systematic prediction errors, we introduce MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated memory bank of transition rules, state caches, and hard-to-predict facts, to condition next-state imagination. We evaluate factual state preservation with Structured State Fidelity (SSF), which scores predicted states through benchmark-specific facts and fields. Compared with SFT, memory-augmented training improves SSF by up to 206.3%. In the full planning setting, we keep the policy model frozen and provide policy-side world skill: retrieved task-level skills and step-wise corrective guidance for action selection. Across ALFWorld, WebShop, and ScienceWorld, memory-augmented agents improve downstream success over an SFT-trained world-model agent, with up to a 65.4% relative gain. Sensitivity analyses further show that retrieved memory improves task success and efficiency under different memory and action-budget settings.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
