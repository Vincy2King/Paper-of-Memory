# A Glimpse into Long-term Physical Coexistence with Intelligent Robots

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.11377v1
- Published: 2026-07-13
- Updated: 2026-07-13
- Authors: Weiqi Jin, Peijun Tang, Kuncheng Luo, Baifu Huang, Binyan Sun, Haotian Yang, Shangjin Xie, Jianan Wang
- Tags: agent, context, long-term
- Categories: cs.RO, cs.AI
- URL: http://arxiv.org/abs/2607.11377v1

## One-Sentence Summary
Long-term physical coexistence with intelligent robots requires more than capable robot policies.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, context, long-term` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-term physical coexistence with intelligent robots requires more than capable robot policies.

进一步看，论文的核心做法或实验重点可以概括为：A persistent robotic assistant must support diverse user-facing interfaces, maintain long-horizon memory of people and preferences, coordinate across robot embodiments, and translate human intent into safe physical...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, context, long-term
- 检索关键词命中：agent memory
- 来源分类信息：cs.RO, cs.AI

## Abstract Snapshot
Long-term physical coexistence with intelligent robots requires more than capable robot policies. A persistent robotic assistant must support diverse user-facing interfaces, maintain long-horizon memory of people and preferences, coordinate across robot embodiments, and translate human intent into safe physical execution. We introduce PHILIA, a multi-robot agent built around a robot gateway abstraction. PHILIA retains the rich interaction and tool ecosystem of OpenClaw while exposing robot-local runtimes, onboard perception, navigation, speaker, and robot policies through a unified capability interface. This design decouples low-frequency, high-semantic agent reasoning from high-frequency, low-level robot execution, enabling plug-and-play integration of user interfaces, robot embodiments, and policy backends. As a result, the user experience becomes compositional: advances in user interfaces, robot embodiments, robot policies, navigation, or interaction algorithms can improve the overall experience without redesigning the system. We validate the architecture on Astribot S1 robots while designing the robot gateway contract to support future heterogeneous robot platforms through a shared capability interface for observation, task execution, navigation, speech playback, status monitoring, and task cancellation. We present representative use cases in which agent memory and scene understanding are grounded in robot actions. These span interactive household scenarios, ranging from simple organization to challenging long-horizon and dexterous service tasks, such as packing a backpack and lifting a garbage bag. We highlight the human-robot interaction flow, where contextual understanding of user intent and preferences, together with human-in-the-loop confirmation or adjustment during execution, is essential for effective assistance.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
