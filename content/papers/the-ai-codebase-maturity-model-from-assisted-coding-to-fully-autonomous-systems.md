# The AI Codebase Maturity Model: From Assisted Coding to Fully Autonomous Systems

- Source: arXiv
- Venue: N/A
- Paper ID: 2604.09388v2
- Published: 2026-04-10
- Updated: 2026-04-27
- Authors: Andy Anderson
- Tags: agent
- Categories: cs.SE, cs.AI
- URL: http://arxiv.org/abs/2604.09388v2

## One-Sentence Summary
AI coding tools are widely adopted, but most teams plateau at prompt-and-review without a framework for systematic progression.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：AI coding tools are widely adopted, but most teams plateau at prompt-and-review without a framework for systematic progression.

进一步看，论文的核心做法或实验重点可以概括为：This paper presents the AI Codebase Maturity Model (ACMM), a 6-level framework describing how codebases evolve from basic AI-assisted coding to fully autonomous systems.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory
- 来源分类信息：cs.SE, cs.AI

## Abstract Snapshot
AI coding tools are widely adopted, but most teams plateau at prompt-and-review without a framework for systematic progression. This paper presents the AI Codebase Maturity Model (ACMM), a 6-level framework describing how codebases evolve from basic AI-assisted coding to fully autonomous systems. Inspired by CMMI, each level is defined by its feedback loop topology - the specific mechanisms that must exist before the next level becomes possible. I validate the model through a 100-day experience report maintaining KubeStellar Console, a CNCF Kubernetes dashboard built from scratch with Claude Code (Opus) and GitHub Copilot, and through the initial production deployment of Hive - an open-source multi-agent orchestration system that realizes Level 6: full autonomy. The system currently operates with 74 CI/CD workflows, 32 nightly test suites, 91% code coverage, and achieves bug-to-fix times under 30 minutes - 24 hours a day. The central finding: the intelligence of an AI-driven development system resides not in the AI model itself, but in the infrastructure of instructions, tests, metrics, and feedback loops that surround it. You cannot skip levels, and at each level, the thing that unlocks the next one is another feedback mechanism. Testing - the volume of test cases, the coverage thresholds, and the reliability of test execution - proved to be the single most important investment in the entire journey. v2 extends the model from 5 to 6 levels, adding Level 6 (Fully Autonomous) with Hive as reference implementation and Beads for cross-agent memory continuity, plus throughput acceleration data showing 5x PR throughput and 37x issue throughput from Level 2 to Level 6.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
