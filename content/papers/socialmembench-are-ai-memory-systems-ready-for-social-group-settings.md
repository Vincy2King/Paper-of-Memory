# SocialMemBench: Are AI Memory Systems Ready for Social Group Settings?

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.17789v1
- Published: 2026-05-18
- Updated: 2026-05-18
- Authors: Olukunle Owolabi
- Tags: agent, benchmark, context, conversation, retrieval
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2605.17789v1

## One-Sentence Summary
Memory systems for AI assistants were built for single-user dialogue and fail characteristically when applied to multi-party social group settings.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Memory systems for AI assistants were built for single-user dialogue and fail characteristically when applied to multi-party social group settings.

进一步看，论文的核心做法或实验重点可以概括为：This gap matters for the social assistants being built today: group-acting agents embedded in chat platforms, and proactive personal-assistant agents whose holistic model of a user must include their social context.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, conversation, retrieval
- 检索关键词命中：memory benchmark, memory benchmarks
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Memory systems for AI assistants were built for single-user dialogue and fail characteristically when applied to multi-party social group settings. This gap matters for the social assistants being built today: group-acting agents embedded in chat platforms, and proactive personal-assistant agents whose holistic model of a user must include their social context. Existing memory benchmarks evaluate dyadic or workplace dialogue; none targets multi-party social groups, where memory must anchor facts in shared history rather than professional roles, separate group norms from individual exceptions, and correctly attribute even after member departure. We introduce SocialMemBench, a benchmark of human-verified synthetic social group networks across five archetypes (close friends, family, recreational, interest community, acquaintance network) and three group-size tiers (4-30 members), with 430 personas and 7,355 conversation turns, yielding 1,031 QA pairs across nine question categories. Each category isolates an architectural capability, and the five failure modes (single-stream conflation, temporal-state overwrite, entity merging at scale, missing cross-persona knowledge, norm-individual conflation) are testable hypotheses; our two research probes Subject-Mem and SMG provide evidence on two, three remain open. A full-context Gemini 2.5 Flash reference reaches only 0.721 against a blind-critic reasoning-model mean of 0.98 on small networks, indicating the benchmark is genuinely difficult even with complete access to the conversation. Across all 43 networks, the four open-source memory frameworks evaluated (Mem0, LangMem, Graphiti, Cognee) cluster in the 0.12-0.18 question-weighted range with overlapping 95% CIs, well below an uncompressed retrieval reference of 0.345 and a matched-answerer full-context reference of 0.369 (GPT-4o-mini). Current memory systems show a measurable gap.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
