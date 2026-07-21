# Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents

- Source: arXiv
- Venue: N/A
- Paper ID: 2607.18039v1
- Published: 2026-07-20
- Updated: 2026-07-20
- Authors: Chunming Wu, Dafei Qiu, Congde Yuan, Charles Quan, Jun Wu, Suipeng Li, Mo Wu, Gavin Xie, Hope Chen, Max Yao
- Tags: agent, conversation, retrieval
- Categories: cs.IR
- URL: http://arxiv.org/abs/2607.18039v1

## One-Sentence Summary
Production customer-service bots must improve answer quality across iterative releases, yet large language models must not bypass evidence boundaries, policy rules, or human-...

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Production customer-service bots must improve answer quality across iterative releases, yet large language models must not bypass evidence boundaries, policy rules, or human-handoff safeguards.

进一步看，论文的核心做法或实验重点可以概括为：We present an \textbf{Evidence-Grounded Customer-Service Agent Workflow} deployed in a real-world customer-service setting.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, retrieval
- 检索关键词命中：conversational memory
- 来源分类信息：cs.IR

## Abstract Snapshot
Production customer-service bots must improve answer quality across iterative releases, yet large language models must not bypass evidence boundaries, policy rules, or human-handoff safeguards. We present an \textbf{Evidence-Grounded Customer-Service Agent Workflow} deployed in a real-world customer-service setting. BM25 recall, issue-title-vector recall, issue-description-vector recall, weighted RRF fusion, and cross-encoder reranking construct grounded FAQ evidence for controlled LLM decisions. Policy-guided orchestration then combines this RAG evidence with scenario-specific rule evidence, conversation memory, and clarification state inside a fixed LangGraph DAG~\cite{langgraph2024}. The paper contributes three reusable deployment patterns: \textbf{hybrid RAG evidence construction}, where multi-channel retrieval and reranking produce auditable FAQ candidates; \textbf{evidence-grounded issue/action decision}, where an Evidence-Grounded Decision Module selects an issue/action from typed FAQ evidence and scenario-specific rule evidence; and \textbf{trace-driven RAG and reranker improvement}, where traces diagnose whether failures come from recall, ranking, final candidate selection, clarification, rule-derived evidence, or action policy, and where reranker fine-tuning is evaluated not only for in-domain gain but also for forgetting risk.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
