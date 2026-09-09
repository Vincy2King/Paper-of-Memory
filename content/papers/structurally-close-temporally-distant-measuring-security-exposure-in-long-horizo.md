# Structurally Close, Temporally Distant: Measuring Security Exposure in Long-Horizon LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2609.05911v1
- Published: 2026-09-05
- Updated: 2026-09-05
- Authors: Md Jafrin Hossain, Nur Al Hasan Haldar
- Tags: agent
- Categories: cs.CR, cs.AI, cs.CL, cs.LG
- URL: http://arxiv.org/abs/2609.05911v1

## One-Sentence Summary
Long-horizon LLM agents interact with untrusted content, persistent memory, external state, and sensitive tools.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Long-horizon LLM agents interact with untrusted content, persistent memory, external state, and sensitive tools.

进一步看，论文的核心做法或实验重点可以概括为：Existing analyses often characterize attacks by the number of execution steps between malicious input and a downstream action.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent
- 检索关键词命中：persistent memory
- 来源分类信息：cs.CR, cs.AI, cs.CL, cs.LG

## Abstract Snapshot
Long-horizon LLM agents interact with untrusted content, persistent memory, external state, and sensitive tools. Existing analyses often characterize attacks by the number of execution steps between malicious input and a downstream action. We show that temporal remoteness can overstate security separation in stateful agents. We introduce a provenance-aware execution graph linking agent events through deterministic state, identifier, and tool provenance, and define \emph{influence distance} $\DI$ as the shortest structural path from an untrusted source to a sensitive action. We compare it with \emph{sequence distance} $\DT$, the shortest injection--sink path in the ordered trajectory. Since the influence graph contains every sequence edge, $\DI \leq \DT$; $\Gap=\DT-\DI$ measures the separation hidden by step count. Across 454 injection--sink pairs from 360 long-horizon AgentDojo trajectories over OpenAI's \texttt{gpt-4o-mini} and \texttt{gpt-4o} and Claude's Haiku 4.5 and Sonnet 4.6, $\Gap>0$ for 96.9% of pairs, with a median gap of 9 hops; 91.0% remain decoupled after removing the largest provenance-only edge class. On AgentDojo's banking suite, 33.8% of 231 pairs from 377 trajectories decouple through different provenance mechanisms. Among 274 OpenAI pairs, $\Gap$ does not independently predict attack success after controlling for $\DT$, attack family, and backend ($β_{\Gap}=0.066$, $p=.088$). At matched thresholds $k=2,3$, a deterministic $\DI$-based pre-execution gate blocks five attack sinks missed by a sequence-only gate with no additional benign blocking, although the paired gain is not significant ($p=.0625$). Execution structure therefore reveals proximity hidden by step count and can support targeted runtime intervention. We measure candidate influence pathways rather than causal attribution.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
