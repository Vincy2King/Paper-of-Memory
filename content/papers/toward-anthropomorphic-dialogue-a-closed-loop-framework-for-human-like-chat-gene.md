# Toward Anthropomorphic Dialogue: A Closed-Loop Framework for Human-Like Chat Generation, Evaluation, and Preference Alignment

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.17191v1
- Published: 2026-07-19
- Updated: 2026-07-19
- Authors: Wentao Liu, Siyu Song, Xi Chen, Youjia Li, Xiaokun Wang, Min Ji, Ji Wang
- Tags: benchmark, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2607.17191v1

## One-Sentence Summary
Human-like private chat requires more than fluent response generation: a system must preserve persona, relationship, memory, bounded knowledge, medium-specific timing, and a...

## Introduction
这篇论文被纳入仓库，是因为它和 `benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Human-like private chat requires more than fluent response generation: a system must preserve persona, relationship, memory, bounded knowledge, medium-specific timing, and a coherent multi-turn arc.

进一步看，论文的核心做法或实验重点可以概括为：We present AnthroDial, a closed-loop framework that formulates anthropomorphic dialogue as a joint problem of system architecture, executable evaluation, and diagnostic alignment.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：benchmark, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Human-like private chat requires more than fluent response generation: a system must preserve persona, relationship, memory, bounded knowledge, medium-specific timing, and a coherent multi-turn arc. We present AnthroDial, a closed-loop framework that formulates anthropomorphic dialogue as a joint problem of system architecture, executable evaluation, and diagnostic alignment. It combines (1) a role-conditioned scheduled dialogue runtime with persona and scenario cards, long-term memory, virtual time, and single-draft message decisions; (2) an executable benchmark with an L0 validity gate, five per-turn dimensions, and five dialogue-level dimensions; and (3) a post-training pipeline that filters 16,436 scheduled-decision examples for SFT and applies GRPO with a cognitive-diagnostic, ZPD-aware reward. The reward maintains Kalman-filtered capability estimates for each behavioral dimension, upweights dimensions with larger capability deficits, and uses rollout scores as task-level ZPD matches to focus optimization on learnable weak skills. On a benchmark with 55 personas, 50 scenarios, 50 persona-scenario bindings, and 100 role-conditioned cases per model, we evaluate 16 systems spanning frontier baselines, open models, thinking/no-think variants, and SFT/RL ablations. The strongest non-trained baseline reaches 32.00% strict ACC, while Qwen3.6-27B-SFT+RL reaches 39.00% strict ACC and a 98.5 overall score. In the 9B no-think setting, SFT and RL improve strict ACC from 0.00% to 13.00% and 18.37%. These results show that anthropomorphic dialogue benefits when generation, evaluation, and reward shaping share the same behavioral dimensions.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
