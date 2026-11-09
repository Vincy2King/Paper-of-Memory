# Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation

- Source: arXiv
- Venue: N/A
- Paper ID: 2611.08718v1
- Published: 2026-11-05
- Updated: 2026-11-05
- Authors: Emilly Pitman de Castro, Vanessa Silva, Gustavo Kanno, Marcus Santos, Bruno Ferraz do Amaral, Marcelo Nogueira, Lucas Francisco Pellicer, Lucas Lanaro, Pedro Augusto Luiz, João Renato Ribeiro Manesco, Giovanni Carbinatti, Isabela de Lima Santos, Lucas Oliveira Jeronymo, Jeison Fappi, Raul Rotilli Aguirre, Fabio André Frantz, Renata De Paris, Fabiana Marucci, Lohan Silva, Vinicius Diniz Reolon, Wandemberg Gibaut
- Tags: agent, conversation, long-term, retrieval
- Categories: cs.AI
- URL: http://arxiv.org/abs/2611.08718v1

## One-Sentence Summary
Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time.

## Introduction
这篇论文被纳入仓库，是因为它和 `agent, conversation, long-term, retrieval` 这些主题直接相关。

它当前来自 `arXiv`。

从摘要来看，作者主要关注的是：Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time.

进一步看，论文的核心做法或实验重点可以概括为：While large language models (LLMs) have improved semantic understanding, they are typically used as isolated components, without addressing how memory, retrieval, and decision-making should be integrated at the system...

如果你在持续跟踪 LLM、Agent 或 benchmark 中的记忆能力，这篇工作值得优先阅读。

## Why It Was Included
- 来源：arXiv
- 高亮主题命中：agent, conversation, long-term, retrieval
- 检索关键词命中：long-term memory, memory retrieval
- 来源分类信息：cs.AI

## Abstract Snapshot
Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time. While large language models (LLMs) have improved semantic understanding, they are typically used as isolated components, without addressing how memory, retrieval, and decision-making should be integrated at the system level. In this work, we propose a memory-aware multi-agent architecture for conversational recommendation, in which LLMs act as orchestration layers that coordinate intent refinement, query construction, and interaction flow. A key design principle is the integration of long-term memory as a first-class component, influencing both routing decisions and semantic query formation. We evaluate the system through cross-session memory experiments, multi-turn conversational simulations, and supervisor-driven interaction studies on the Amazon Reviews dataset. Results show that memory-enabled interactions recover up to 63\% of the gap toward explicit-query scenarios and prevent semantic degradation in extended dialogues. In addition, supervisory orchestration increases user acceptance by +28.9 percentage points, highlighting the importance of structured orchestration in guiding interaction and output quality. We also observe an exposure bottleneck between retrieved candidates and displayed recommendations. While LLM-reranking does not improve Hit@K, it consistently enhances semantic consistency and diversity. To capture these effects, we introduce the Semantic Consistency Score (SCS), a complementary evaluation measure. Overall, the results emphasize the importance of system-level design choices, suggesting that effective conversational recommendation benefits from explicit memory integration, orchestration, and evaluation beyond traditional ranking metrics.

## Manual Notes
<!-- MANUAL_NOTES_START -->
在这里补充你的人工解读、和其他工作的关系、复现记录，或你认为最值得读的段落。
<!-- MANUAL_NOTES_END -->
