# Workerville: Towards an Organizational Behavior Account of Agent Safety

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.11561v1
- Published: 2026-10-08
- Updated: 2026-10-08
- Authors: Hanjun Luo, Junting Mao, Yuhan Lu, Haobo Zhang, Zhimu Huang, Yankai Chen, Hanan Salam, Xue Liu
- Tags: agent, benchmark, long-term
- Categories: cs.AI
- URL: http://arxiv.org/abs/2610.11561v1

## One-Sentence Summary
LLM-based agents now interact with their environments continuously, shaped by such organizational channels as user instructions, peer messages, and long-term memory.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：LLM-based agents now interact with their environments continuously, shaped by such organizational channels as user instructions, peer messages, and long-term memory.

进一步看，论文的核心做法或实验重点可以概括为：Existing safety research has examined these influences, but largely as separate agent components.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.AI

## Abstract Snapshot
LLM-based agents now interact with their environments continuously, shaped by such organizational channels as user instructions, peer messages, and long-term memory. Existing safety research has examined these influences, but largely as separate agent components. How such factors jointly shape an agent's safety behavior from a unified perspective remains unmeasured. To bridge this gap, we advocate organizational behavior (OB) as a framework for studying the safety of advanced agents, reorganizing the objects of study, theoretical foundations, and experimental design around the relational structure in which agents operate. We present the first systematic formalization of counterproductive work behavior (CWB), a canonical safety-relevant subfield of OB, as Agentic Counterproductive Behavior (ACB). ACB specifies three organizational antecedents (vertical supervisor relations, horizontal peer norms, and internal cognitive structures) and maps them onto three counterproductive outcome dimensions (unauthorized disclosure, destructive operations, and production deviation). To operationalize ACB, we introduce Workerville, a controlled benchmark that manipulates organizational conditions over shared tasks, applying 16 organizational configurations to 210 tasks to yield 3,360 challenges, evaluated by human-validated agentic judges. Benchmarking 6 frontier LLMs, we find that (I) negative organizational antecedents exhibit non-monotonic amplification when combined, with the unauthorized-disclosure rate rising from 16.5% under no negative antecedent to 60.1% under two and falling back to 50.3% under three; (II) agents reproduce typical behavioral patterns predicted by human CWB research; (III) these results establish OB as a systematic framework for agent safety research, pointing toward a new research agenda.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
