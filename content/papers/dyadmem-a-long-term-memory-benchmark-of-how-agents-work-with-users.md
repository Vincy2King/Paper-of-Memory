# DyadMem: A Long-Term Memory Benchmark of How Agents Work with Users

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.03020v1
- Published: 2026-10-02
- Updated: 2026-10-02
- Authors: Yifei Tao, Xinyu Zhong, Henry Hengyuan Zhao, Fanyi Wang, Tengda Guo, Wentao Qiu, Ying Wang, Liujian Tang
- Tags: agent, benchmark, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.03020v1

## One-Sentence Summary
Long-term agents must remember not only what is true about a user, but also how a particular agent should work with that user as their shared history evolves.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term agents must remember not only what is true about a user, but also how a particular agent should work with that user as their shared history evolves.

进一步看，论文的核心做法或实验重点可以概括为：Existing benchmarks primarily supervise user facts and preferences or experience reusable across users, leaving this relationship-specific agent memory implicit.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Long-term agents must remember not only what is true about a user, but also how a particular agent should work with that user as their shared history evolves. Existing benchmarks primarily supervise user facts and preferences or experience reusable across users, leaving this relationship-specific agent memory implicit. Additionally, most prior works measure the model solely with final-answer QA over long interaction histories, making the assessment still incomplete and unreliable. To this end, we introduce DyadMem with the proposed new definition User-conditioned Relational Agent Memory (URAM). DyadMem jointly annotates user-side memory and URAM along the same multi-session trajectories, resulting in 6 memory categories. To summarize, it includes 3,065 episodes, 50,961 sessions, and 61,210 QA instances, with extensive session-level Capture and Update gold annotations, query-level Recall support, and two QA settings: Gold-Memory and Full-Pipeline. Across 16 open-weight and 4 proprietary models, Gold-Memory QA is consistently strong, yet Full-Pipeline QA drops sharply. Such a gap explicitly supports our fine-grained evaluation design. Additionally, several quantitative results further reveal low Capture recall, incomplete Recall, and unsafe-deletion issues arising from even the frontier LLMs. We further conduct a rigorous experiment to validate the effectiveness of our URAM and observe the positive effects for all 20 models. In summary, DyadMem is a dual-domain, full-pipeline memory benchmark with extensive annotation efforts for advancing the domain's development.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
