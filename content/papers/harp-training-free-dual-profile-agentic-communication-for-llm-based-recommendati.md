# HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.05319v1
- Published: 2026-11-03
- Updated: 2026-11-03
- Authors: Zhen Tao, Xun Zhou, Xuhui Chen, Ziyue Qiao, Qingqiang Sun
- Tags: agent, benchmark, context, retrieval
- Categories: cs.IR, cs.AI
- URL: http://arxiv.org/abs/2611.05319v1

## One-Sentence Summary
In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, benchmark, context, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone.

进一步看，论文的核心做法或实验重点可以概括为：Yet users and items remain asymmetric: only the user is given a structured profile; it enters a bandwidth-limited reranker prompt; and it is frozen after warmup.

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, benchmark, context, retrieval
- 检索关键词命中：memory augmented, memory-augmented
- 来源分类信息：cs.IR, cs.AI

## Abstract Snapshot
In LLM-based recommendation, memory acts as a user-level agent in a memory-augmented backbone. Yet users and items remain asymmetric: only the user is given a structured profile; it enters a bandwidth-limited reranker prompt; and it is frozen after warmup. We recast LLM-based recommendation as an agentic-communication process in four stages: BUILD a self-description, TRANSMIT it along the collaborative graph, UNDERSTAND the other side, and SYNC it from the next interaction. This formulation reveals three unresolved communication challenges: the item side never produces a comparable self-description (one-sided BUILD); profile-level signals enter only the bandwidth-limited reranker prompt rather than retrieval, where they would not compete for context tokens (prompt-trapped UNDERSTAND); and the user's description is frozen after warmup with no principled update rule (absent SYNC). We instantiate the missing stages as HARP (Homophily-aware Agentic Recommendation via dual Profiles), a training-free, three-operator addition to a frozen LLM backbone: a rule-extracted symmetric item profile (zero extra LLM calls), a channel-decomposable profile-level homophily H(phi_u, phi_i) consumed at retrieval time rather than inside the reranker prompt, and a single-pass reflective update realising in-context profile evolution without any gradient step. On four public benchmarks (Yelp, Books, MovieTV, Goodreads), HARP lifts Hit@1 over the strongest published baseline by 6.9%-24.0%, with family-wise Holm-corrected p < 1e-9 on every dataset. Ablations and a per-case attribution study show that the operators contribute complementary gains, with the retrieval-side gate as the main source; we also report the trade-off introduced by the reflective pass. We formulate agentic communication and provide a training-free instantiation. Code is available at https://github.com/Jove-Zhen/HARP.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
