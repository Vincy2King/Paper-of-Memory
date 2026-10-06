# GitSwarm: Decentralized Compounding Inference

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.04862v1
- Published: 2026-10-04
- Updated: 2026-10-04
- Authors: Vedant Shah, Ankur Samanta, Paras Dahal, Mikhail Plekhanov, Carole-Jean Wu, Scott Yih, Remi Munos, Rob Fergus, Jakob Foerster, Ruslan Salakhutdinov, Sanjeev Arora, Jason Weston, Aaron Courville, Anirudh Goyal
- Tags: agent
- Categories: cs.AI, cs.LG
- URL: http://arxiv.org/abs/2610.04862v1

## One-Sentence Summary
Long-horizon problem solving and scientific research require computation to accumulate across successive attempts.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon problem solving and scientific research require computation to accumulate across successive attempts.

进一步看，论文的核心做法或实验重点可以概括为：Partial solutions, experimental findings, and unsuccessful approaches can inform later work, yet most inference-time computation is organized around individual trajectories or candidates rather than a persistent body...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.AI, cs.LG

## Abstract Snapshot
Long-horizon problem solving and scientific research require computation to accumulate across successive attempts. Partial solutions, experimental findings, and unsuccessful approaches can inform later work, yet most inference-time computation is organized around individual trajectories or candidates rather than a persistent body of reusable work. We call this paradigm compounding inference: organizing inference-time computation so that intermediate work persists and can be inspected, extended, combined, or challenged by subsequent computation. We instantiate compounding inference in GitSwarm, an asynchronous system where homogeneous agents independently decide how to advance a task while collaborating through structured persistent memory. Agents explore, experiment, verify, refine, and synthesize previous work in a shared, branch-able Git repository. Atomic commits preserve intermediate artifacts, while explicit semantic dependencies record how later contributions build on work across branches. We evaluate GitSwarm on long-horizon problem solving and sustained GPU-backed experimental research. On IMOProofBench-Advanced, GitSwarm solves all 30 problems in one run using GPT-5.5. On ProgramBench, it achieves a $79.4\%$ mean score, versus $65.1\%$ for the strongest reported baseline under the stated budget. On three neural architecture research tasks (Residual Matrix Transformer, Looped Transformer, NanoChat), GitSwarm improves upon the starting architectures through successive experimentation. Beyond final performance, we measure whether computation accumulates: on ProgramBench, $94.7\%$ of contributions are subsequently built upon, while the selected solution's ancestry covers $82-93\%$ of the contribution graph. These results show that inference-time computation can accumulate across otherwise independent episodes, forming an evolving body of work that subsequent inference can reuse.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
