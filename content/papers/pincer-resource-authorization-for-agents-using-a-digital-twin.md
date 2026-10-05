# Pincer: Resource Authorization for Agents using a Digital Twin

- Source: arXiv
- Venue: N/A
- Paper ID: 2610.02569v1
- Published: 2026-10-01
- Updated: 2026-10-01
- Authors: Mayank Rathee, Alexander Stepanov, Shalin Madabhavi, Jinhao Zhu, Raluca Ada Popa, Ion Stoica
- Tags: agent, context
- Categories: cs.CR, cs.AI
- URL: http://arxiv.org/abs/2610.02569v1

## One-Sentence Summary
Coding agents have become increasingly long-horizon, autonomous, reliant on general-purpose shell and maintain their own persistent memory for self-improvement.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Coding agents have become increasingly long-horizon, autonomous, reliant on general-purpose shell and maintain their own persistent memory for self-improvement.

进一步看，论文的核心做法或实验重点可以概括为：While these capabilities have made the agents powerful, they have also made them harder to defend against external adversaries.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI

## Abstract Snapshot
Coding agents have become increasingly long-horizon, autonomous, reliant on general-purpose shell and maintain their own persistent memory for self-improvement. While these capabilities have made the agents powerful, they have also made them harder to defend against external adversaries. Defenses that restrict this architecture --- typed tools, information-flow control, or policy prediction engines --- give up too much functionality to be adopted. Agents deployed today (e.g. Claude, Codex) rely on a combination of user-mediated and automode sandboxing as their primary defense. In user-mediated sandboxing, user-maintained policies decay over time and repeated permission requests cause user fatigue, while auto mode's tool-call classifiers learn no user-specific policy and are not meant to defend against adversarial setups. Pincer is a new defense that operates at the resource layer and works alongside existing defenses at the tool-call layer like the auto mode. At the core of Pincer lies a digital twin, an isolated-context model that automatically learns and enforces dynamic user-specific least-privilege policies. The digital twin keeps continually learning the user's preferences allowing it to act as the user's proxy for the agent's permission requests. To emulate the learning phase, we propose a new usercentric dataset with examples following a multi-day transcript of user-agent interaction. Our evaluation shows that Pincer performs strongly on both security and utility in comparison to several baselines which includes variants of LLM judges and adaptations of Conseca (HotOS '25). We highlight attack types where Pincer's design leads to a significant security improvement compared to all other baselines, while outperforming the baselines even for other types of attacks.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
