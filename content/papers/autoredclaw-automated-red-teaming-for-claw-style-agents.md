# AutoRedClaw: Automated Red-Teaming for Claw-Style Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.27244v1
- Published: 2026-10-19
- Updated: 2026-10-19
- Authors: Hao Li, Tongyan Hu, Weidi Luo, Shanghao Shi, Xiaogeng Liu, Aiden Suh, Yulong Cao, Ning Zhang, William Yeoh, Yevgeniy Vorobeychik, Chaowei Xiao
- Tags: agent, benchmark, context, long-term
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2610.27244v1

## One-Sentence Summary
Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw.

进一步看，论文的核心做法或实验重点可以概括为：These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, long-term
- 检索关键词命中：long-term memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly reloaded into the agent's context, creating persistent threats across tasks and sessions. Existing security evaluation systems struggle to evaluate these complex claw-style systems since they rely heavily on manually constructed test cases and environments, which limits their scale and coverage; in addition, these manually designed cases quickly become outdated as agents evolve, and their evaluation settings leave a gap with how claw-style agents are deployed in practice. To address this, we introduce AutoRedClaw, an automated red-teaming framework that generates end-to-end attacks together with the environments needed to execute them. AutoRedClaw combines a strict quality-checking protocol with execution-based validation to ensure the correctness, realism, and effectiveness of generated samples, and adopts task-driven environment construction to keep costs low. To achieve broad coverage, it organizes generation along risk categories, attack strategies, attack stages, and attack surfaces, and uses experience-guided exploration to steer generation toward under-explored regions. AutoRedClaw achieves an effective attack rate above 30% at less than $0.10 per successful sample. From its outputs, we construct RedClaw-Bench, a 330-case benchmark that yields substantially higher attack success rates (ASRs) than AgentDojo, AgentDyn, and DTap. Across seven harnesses and four frontier models, most agent systems exceed 50% ASR, showing that our red-teaming pipeline provides a strong evaluation signal even for the most advanced agent systems. Our code and benchmark are released at https://github.com/SaFo-Lab/AutoRedClaw.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
