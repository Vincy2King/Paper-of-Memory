# Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning

- Source: arXiv
- Venue: N/A
- Paper ID: 2606.20954v1
- Published: 2026-06-18
- Updated: 2026-06-18
- Authors: Nusrat Jahan Lia, Aritra Mazumder
- Tags: agent, context, conversation
- Categories: cs.CL, cs.AI
- URL: http://arxiv.org/abs/2606.20954v1

## One-Sentence Summary
Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, conversation` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict.

进一步看，论文的核心做法或实验重点可以概括为：When an eviction policy drops a load-bearing detail, for example an access token issued at login or a path the next call needs, the action fails.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, conversation
- 检索关键词命中：agent memory, conversational memory
- 来源分类信息：cs.CL, cs.AI

## Abstract Snapshot
Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict. When an eviction policy drops a load-bearing detail, for example an access token issued at login or a path the next call needs, the action fails. We present LRE (Learned Relevance Eviction), a few kilobytes, CPU-only, language-model-free scorer that learns which units of history are load-bearing and keeps them by verbatim extraction. Under a matched-budget comparison, in our experiment, no baseline dominates LRE on the accuracy-cost plane. On agents, LRE matches the accuracy of keeping the entire history overall. On the simplest tasks, it exceeds that no-eviction baseline by 27%, while requiring zero compressor calls and reducing peak context size by up to 52%. A controlled study trace shows LRE completes tasks where the others loop, finishing one such task in 37% fewer calls than keeping everything and solving 14 tasks where no other run policy does. On conversational memory, LRE outranks dense and token-pruning encoders at zero neural cost. In downstream evaluation, LRE gives the best budgeted answer quality on LoCoMo reading 68% fewer tokens. Its supervision can also be annotation-free: training only on the system's own behavior recovers 95% of the supervised scorer's effectiveness. We argue that, because memory eviction in LLM agents is a fidelity problem, it requires a deployable proactive policy where the future query is unavailable and exact state is decisive, and that cheap learned relevance can be sufficient.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
