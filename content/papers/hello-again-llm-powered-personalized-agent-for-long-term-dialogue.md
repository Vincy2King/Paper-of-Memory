# Hello Again! LLM-powered Personalized Agent for Long-term Dialogue

- Source: OpenReview
- Venue: NAACL (Long Papers) 2025
- Paper ID: openreview:LeE9lXiGUC
- Published: 2025-01-01
- Updated: 2026-05-30
- Authors: Hao Li, Chenghao Yang, An Zhang, Yang Deng, Xiang Wang, Tat-Seng Chua
- Tags: agent, benchmark, long-term, retrieval
- Categories: DBLP.org/-/Record
- URL: https://openreview.net/forum?id=LeE9lXiGUC

## One-Sentence Summary
Open-domain dialogue systems have seen remarkable advancements with the development of large language models (LLMs).

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term, retrieval` 这些主题直接相关。

它当前来自 `OpenReview`，并与 `NAACL (Long Papers) 2025` 这个 venue 相关。

从摘要来看，作者主要关注的是：Open-domain dialogue systems have seen remarkable advancements with the development of large language models (LLMs).

进一步看，论文的核心做法或实验重点可以概括为：Nonetheless, most existing dialogue systems predominantly focus on brief single-session interactions, neglecting the real-world demands for long-term companionship and personalized interactions with chatbots.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：OpenReview
- Venue：NAACL (Long Papers) 2025
- 高亮主题命中：agent, benchmark, long-term, retrieval
- 检索关键词命中：memory retrieval
- 来源分类信息：DBLP.org/-/Record

## Abstract Snapshot
Open-domain dialogue systems have seen remarkable advancements with the development of large language models (LLMs). Nonetheless, most existing dialogue systems predominantly focus on brief single-session interactions, neglecting the real-world demands for long-term companionship and personalized interactions with chatbots. Crucial to addressing this real-world need are event summary and persona management, which enable reasoning for appropriate long-term dialogue responses. Recent progress in the human-like cognitive and reasoning capabilities of LLMs suggests that LLM-based agents could significantly enhance automated perception, decision-making, and problem-solving. In response to this potential, we introduce a model-agnostic framework, the Long-term Dialogue Agent (LD-Agent), which incorporates three independently tunable modules dedicated to event perception, persona extraction, and response generation. For the event memory module, long and short-term memory banks are employed to separately focus on historical and ongoing sessions, while a topic-based retrieval mechanism is introduced to enhance the accuracy of memory retrieval. Furthermore, the persona module conducts dynamic persona modeling for both users and agents. The integration of retrieved memories and extracted personas is subsequently fed into the generator to induce appropriate responses. The effectiveness, generality, and cross-domain capabilities of LD-Agent are empirically demonstrated across various illustrative benchmarks, models, and tasks. The code is released at https://github.com/leolee99/LD-Agent.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
