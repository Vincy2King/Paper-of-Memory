# ShiJianBench: From Dialogue to Decision for Long-Horizon Evaluation of Investment Advisors

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.01204v1
- Published: 2026-08-02
- Updated: 2026-08-02
- Authors: Jie Gong, Maowei Jiang, Zhiwei Liu, Yang Qiao, Wenxi Wu, Mengxi Xiao, Enze Zhang, Ziyan Kuang, Yankai Chen, Caishuang Huang, Meng Zhou, Xiku Du, Xue Liu, Guojun Xiong, Min Peng, Qianqian Xie, Sophia Ananiadou
- Tags: agent, conversation, long-term
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.01204v1

## One-Sentence Summary
Conversational investment advisors influence not only what users know, but also how they make subsequent decisions as market conditions evolve.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational investment advisors influence not only what users know, but also how they make subsequent decisions as market conditions evolve.

进一步看，论文的核心做法或实验重点可以概括为：Existing evaluations primarily assess response quality or observed outcomes, leaving the long-horizon pathway from advisor language to investor behavior difficult to audit.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Conversational investment advisors influence not only what users know, but also how they make subsequent decisions as market conditions evolve. Existing evaluations primarily assess response quality or observed outcomes, leaving the long-horizon pathway from advisor language to investor behavior difficult to audit. We introduce ShiJianBench, an offline framework for evaluating conversational investment advisors through matched investor trajectories under fixed historical market feedback. At its core is a multi-agent investor simulator with explicit evolving state variables, motive-driven deliberation, long-term memory, and dialogue-grounded updates. The simulator is calibrated against aggregate behavioral patterns from 7,199 real users, and advisor policies are evaluated using separate investor-side, service-side, and content-side metrics under a hard compliance gate. Experiments on Chinese fund-market traces from 2021 to 2026 identify a stable leading group of LLM advisors that combines substantially stronger personalized content with competitive investor-side trajectory outcomes. These results reveal a systematic distinction between producing a high-quality response and delivering an effective long-horizon intervention, motivating trajectory-aware evaluation of conversational advisors.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
