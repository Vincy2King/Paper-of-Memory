# SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.34365v1
- Published: 2026-10-25
- Updated: 2026-10-25
- Authors: Cheng Gui, Xiang Zheng, Xingjun Ma, Kaidi Xu, Cong Wang, Weiying Ma
- Tags: agent, benchmark
- Categories: cs.LG, cs.AI
- URL: http://arxiv.org/abs/2610.34365v1

## One-Sentence Summary
Science agents increasingly package domain expertise as reusable skills that plan analyses, select tools, and execute workflows.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Science agents increasingly package domain expertise as reusable skills that plan analyses, select tools, and execute workflows.

进一步看，论文的核心做法或实验重点可以概括为：This modularity creates a confidentiality risk: the interactions that deliver a skill's capability can also reveal the skill itself.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：persistent memory
- 来源分类信息：cs.LG, cs.AI

## Abstract Snapshot
Science agents increasingly package domain expertise as reusable skills that plan analyses, select tools, and execute workflows. This modularity creates a confidentiality risk: the interactions that deliver a skill's capability can also reveal the skill itself. We build an extensible benchmark of 40 protected skills across eight open- and closed-source science-agent platforms, comparing direct, fixed-strategy, and bandit-guided iterative probing under reference-based and reference-free evaluation. Leakage is pervasive: all eight platforms (100%) leak at least one protected skill, and four reach 100% attack success under a single direct request. To stress-test platforms that resist simple probing, we propose SEEK (Skill Extraction with Evolving Knowledge), a black-box, self-evolving red-teaming agent that consolidates response-derived evidence in persistent memory and evolves reusable attack skills, using only user-visible responses. On 12 skills from SpatialAgent and Biomni, SEEK achieves 100% attack success while reducing the mean first-success round by 31.8% and 38.2% relative to bandit-guided probing. Against a confidentiality policy that blocks all three benchmark protocols, SEEK still extracts one of six protected skills. These findings show that current science agents do not reliably protect their skills and that defenses must be evaluated against adaptive, multi-turn attackers.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
