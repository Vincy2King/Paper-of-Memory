# AutoKD: Autonomous Knowledge Discovery

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.06366v1
- Published: 2026-09-06
- Updated: 2026-09-06
- Authors: Qinwen Ge, Bo Ni, Haowei Fu, Ngoc N. Tran, Erik Blasch, Tyler Derr
- Tags: agent, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2609.06366v1

## One-Sentence Summary
Scientific discovery in data-rich domains is currently constrained by human bandwidth: the growth in the volume and complexity of real-world data far outpaces the rate at which...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Scientific discovery in data-rich domains is currently constrained by human bandwidth: the growth in the volume and complexity of real-world data far outpaces the rate at which researchers can read, reason, and...

进一步看，论文的核心做法或实验重点可以概括为：Recent LLM-based multi-agent systems have begun to automate portions of the research cycle, but they target hypothesis generation in settings where validation cannot itself be automated, and each run is one-shot, with...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Scientific discovery in data-rich domains is currently constrained by human bandwidth: the growth in the volume and complexity of real-world data far outpaces the rate at which researchers can read, reason, and synthesize. Recent LLM-based multi-agent systems have begun to automate portions of the research cycle, but they target hypothesis generation in settings where validation cannot itself be automated, and each run is one-shot, with no mechanism for findings to accumulate or steer subsequent inquiry. This paper introduces AutoKD, a multi-agent framework for autonomous knowledge discovery that is both computational and cumulative, allowing validated findings to persist and inform subsequent inquiry. Six coordinated LLM agents collaborate in an open-ended discovery loop, where accepted findings are stored in a persistent insight graph that serves as both long-term memory and an exploration-steering mechanism. We evaluate AutoKD on three diverse datasets from two perspectives: Open-ended Quality against published findings, and Conditioned Quality via literature-derived queries. Across both evaluation perspectives, AutoKD covers known findings and surfaces substantive discoveries that complement human-driven research. Our code is available at https://github.com/GeQinwen/AutoKD.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
