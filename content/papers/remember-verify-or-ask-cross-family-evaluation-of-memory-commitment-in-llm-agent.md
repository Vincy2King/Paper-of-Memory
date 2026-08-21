# Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2608.19564v1
- Published: 2026-08-20
- Updated: 2026-08-20
- Authors: Baichuan Li, Junyi Yao, Zihao Zheng
- Tags: agent, context
- Categories: cs.CL
- URL: http://arxiv.org/abs/2608.19564v1

## One-Sentence Summary
Persistent memory can personalize an LLM agent, but an incorrect durable update can silently distort future behavior.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Persistent memory can personalize an LLM agent, but an incorrect durable update can silently distort future behavior.

进一步看，论文的核心做法或实验重点可以概括为：We study the memory-clarification boundary: whether interaction-derived information should be persisted, used only in the current context, re-verified, or clarified with the user.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CL

## Abstract Snapshot
Persistent memory can personalize an LLM agent, but an incorrect durable update can silently distort future behavior. We study the memory-clarification boundary: whether interaction-derived information should be persisted, used only in the current context, re-verified, or clarified with the user. MCB contains 140 primary scenarios, split into 70 development and 70 held-out items, plus a separate 70-item contrast set. It evaluates both action labels and structured tool-call selection. Two non-authors independently label the 70 held-out primary and 70 contrast items (97.1% agreement, Cohen's kappa = 0.962); a blind third resolves four disagreements, replacing eight author labels by non-author majority. Across Claude and Qwen, models verify changing facts more reliably than they ask users to resolve ambiguity. Bare Qwen asks on 0/12 clarification items while verifying 12/18 freshness items. Few-shot prompting raises accuracy from 0.557 to 0.771 (paired delta = +0.214, Holm-adjusted exact McNemar p_H = 0.002), yet clarification recall remains 0.333. The policy prompt reduces erroneous persistence from 0.243 to 0.100 (p_H = 0.038), although its accuracy gain is not significant. Label-tool agreement is 57% for each Claude model and 23% for Qwen; Qwen accuracy falls from 0.557 to 0.343 (p_H = 0.047). Memory evaluation must test both stated decisions and tool-call choices.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
