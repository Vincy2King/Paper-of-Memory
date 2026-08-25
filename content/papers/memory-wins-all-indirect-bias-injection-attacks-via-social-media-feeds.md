# MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.22061v1
- Published: 2026-08-22
- Updated: 2026-08-22
- Authors: Minjae Seo, Wonwoo Choi, Geonwoo Han, Taekyoung Kwon, Yongsu Kim, Sang Seo, Jaewon Noh, Hankyul Baek, Seongyun Seo, Myoungsung You
- Tags: agent, benchmark
- Categories: cs.AI, cs.CY
- URL: http://arxiv.org/abs/2608.22061v1

## One-Sentence Summary
Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected information or execution results in persistent...

进一步看，论文的核心做法或实验重点可以概括为：We show that this ordinary ingestion of external content opens an indirect path for manipulating subsequent agent behavior.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark
- 检索关键词命中：agent memory, persistent memory
- 来源分类信息：cs.AI, cs.CY

## Abstract Snapshot
Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected information or execution results in persistent memory for later use. We show that this ordinary ingestion of external content opens an indirect path for manipulating subsequent agent behavior. Based on this observation, we present IBIA, an Indirect Bias Injection Attack that plants an adversary-aligned stance on a specific topic into a victim agent's memory through external content, without direct access to the agent, its memory, or future user queries. For this, IBIA combines three mechanisms: comment cloaking, which keeps the crafted content consistent with the surrounding discussion, comment watermarking, which enables lightweight identification during curation, and category anchoring, which makes the retained stance salient under later related requests. We evaluate IBIA on BiasBench, a benchmark of 6,000 adversary-crafted social comments and 120 email instances. The watermark-based curation identifies 95.9% of the injected comments. Under the OpenClaw setting, IBIA achieves adversary-aligned response rates (AARs) of 91.2% on average across four downstream tasks, including 86.6% on the frontier GPT-5.5. We further propose a memory boundary defense that detects the injected bias and reduces AARs to 80.6%.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
