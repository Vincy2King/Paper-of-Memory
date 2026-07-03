# COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.01709v1
- Published: 2026-07-02
- Updated: 2026-07-02
- Authors: Zongxia Li, Dawei Liu, Fuxiao Liu, Yuhang Zhou, Xiyang Wu, Jingxi Chen, Jing Xie, Xiaomin Wu, Lichao Sun
- Tags: agent, benchmark
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2607.01709v1

## One-Sentence Summary
Agents are increasingly used to construct workflows and assist humans in completing recurring tasks more efficiently.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agents are increasingly used to construct workflows and assist humans in completing recurring tasks more efficiently.

进一步看，论文的核心做法或实验重点可以概括为：As these workflows become repeated and domain-specific, agent memory and reusable skills become increasingly important: agents should be able to recall workflow patterns, execution constraints, and user preferences...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Agents are increasingly used to construct workflows and assist humans in completing recurring tasks more efficiently. As these workflows become repeated and domain-specific, agent memory and reusable skills become increasingly important: agents should be able to recall workflow patterns, execution constraints, and user preferences from previous runs. We study this problem in workflow-based image generation and introduce COMFYCLAW, an agentic skill evolution harness for controlling ComfyUI workflows. COMFYCLAW formulates workflow construction as typed graph editing, exposes tools organized by construction stage, automatically reverts invalid edits, and uses a region-level vision-language model (VLM) verifier to translate visual failures into actionable repair suggestions. The framework further evolves a progressively disclosed skill library, where trajectories, execution errors, and verifier feedback from previous runs are distilled into reusable Agent Skills. Across four benchmark splits, three agent models, and two image backbones, COMFYCLAW achieves the best average image-generation evaluation score across all six agent configurations, outperforming a verifier-only baseline without skill evolution. Human annotations further show that annotators prefer COMFYCLAW over variants without skill evolution. Our results suggest that skill evolution is an effective mechanism for improving agent reliability and performance in recurring visual workflow construction.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
