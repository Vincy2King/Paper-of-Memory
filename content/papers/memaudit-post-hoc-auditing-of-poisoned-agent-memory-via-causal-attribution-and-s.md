# MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection

- Source: arXiv
- Venue: N/A
- Paper ID: 2605.23723v1
- Published: 2026-05-22
- Updated: 2026-05-22
- Authors: Zhewen Tan, Yilun Yao, Huiyan Jin, Wenhan Yu, Guoan Wang, Mengyuan Fan, liang lu, Feng Liu, Xiangzheng Zhang, Duohe Ma, Tong Yang, Lin Sun
- Tags: agent
- Categories: cs.AI
- URL: http://arxiv.org/abs/2605.23723v1

## One-Sentence Summary
Large language model agents increasingly rely on persistent memory to store past interactions, retrieve relevant demonstrations, and improve long-horizon task execution.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Large language model agents increasingly rely on persistent memory to store past interactions, retrieve relevant demonstrations, and improve long-horizon task execution.

进一步看，论文的核心做法或实验重点可以概括为：However, this memory mechanism also creates a practical security vulnerability: an adversarial user may inject malicious records into the agent's memory through ordinary interaction, and these records can later be...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：agent memory, memory augmented, memory-augmented, persistent memory
- 来源分类信息：cs.AI

## Abstract Snapshot
Large language model agents increasingly rely on persistent memory to store past interactions, retrieve relevant demonstrations, and improve long-horizon task execution. However, this memory mechanism also creates a practical security vulnerability: an adversarial user may inject malicious records into the agent's memory through ordinary interaction, and these records can later be retrieved to steer the agent's reasoning and actions. Existing defenses primarily focus on online intervention, such as prompt filtering or output blocking, but they do not address the post-hoc question of which stored memories are responsible after harmful behavior has already been observed. We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents. The framework combines two complementary signals: (1) a counterfactual memory influence score that measures each memory's causal contribution to harmful outputs, and (2) a memory consistency graph that identifies structurally anomalous memories within the broader memory store. We evaluate MemAudit against MINJA, a query-only memory injection attack in which malicious records are generated and stored through normal agent interactions rather than direct memory-bank modification. Across both QA and reasoning-agent settings, MemAudit substantially reduces attack success rates under realistic post-hoc auditing scenarios. The results show that QA attack success is reduced from $70\%$ to $0\%$, while RAP attack success drops from $83.3\%$ to $0\%$.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
