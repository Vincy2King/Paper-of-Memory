# AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.05334v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Mahdi Farahbakhsh, Ilan Sela, Fatemeh Doudi, Vishnu Teja Kunde, Krishna Narayanan, Jean-Francois Chamberland, Dileep Kalathil
- Tags: agent, context, long-term
- Categories: cs.AI, cs.LG, cs.NE
- URL: http://arxiv.org/abs/2610.05334v1

## One-Sentence Summary
Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the model only the role of proposer.

进一步看，论文的核心做法或实验重点可以概括为：The model knows nothing of the search beyond what it is shown.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：long-term memory, working memory
- 来源分类信息：cs.AI, cs.LG, cs.NE

## Abstract Snapshot
Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the model only the role of proposer. The model knows nothing of the search beyond what it is shown. As models grow more capable, a question arises: does a search strategy chosen by a human before the run scale better than promoting the model from proposer to planner and letting it own the search? The Bitter Lesson suggests that choosing the strategy in advance is the kind of hand-designed structure that general methods eventually outscale. We introduce AgentDiscover, in which a coding agent plans the search using its context as working memory, runs experiments, and records every attempt in a database of ideas, candidates, and their relations. This database serves as the agent's long-term memory and is structured so that the selection rules of classical algorithms such as MAP-Elites and Monte Carlo tree search each reduce to a single query, which the agent is free to use, combine, or replace. A server maintains the database and steers the agent after every submission, keeping it on course over long runs. In our experiments, AgentDiscover is more cost-efficient than existing frameworks, reaching better scores at lower cost. On tasks in kernel engineering, biology, algorithm design, and mathematics, AgentDiscover outperforms prior discovery frameworks. Its programs would have placed first among human competitors in seven past AtCoder heuristic contests, and on eleven mathematical and systems optimization tasks it matches or exceeds every baseline that uses the same model. Our code is available at https://github.com/mhdfb/AgentDiscover.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
