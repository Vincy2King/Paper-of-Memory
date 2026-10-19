# GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.23709v1
- Published: 2026-10-16
- Updated: 2026-10-16
- Authors: Hyunseo Kim, Suil Choe, Sukkyoung So, Daeyeon Yi
- Tags: agent, episodic
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2610.23709v1

## One-Sentence Summary
Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, episodic` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories.

进一步看，论文的核心做法或实验重点可以概括为：However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, episodic
- 检索关键词命中：agent memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable agentic memory. To address this limitation, we introduce GLOBE, an agentic framework that drives continual self-improvement by storing optimization knowledge in an evolving handbook of explicit, field-scoped behaviors. In each episode, an Editor applies relevant behaviors and receives rank-based feedback, which a Reflector converts into behavior updates. Crucially for dependable execution in real-world settings, a Moderator removes redundant proposals, a Curator commits accepted changes, and consistently harmful behaviors are deactivated. This cycle transforms episodic feedback into a persistent, field-scoped optimization memory. Experiments show that structured behaviors outperform monolithic prompt optimization, while feedback-driven evolution and moderation further improve effectiveness and reduce downside risk. The learned behaviors also remain effective on unseen product categories, suggesting that agentic memory evolution supports interpretable and transferable product optimization.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
