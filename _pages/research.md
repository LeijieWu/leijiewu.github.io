---
layout: single
title: "Research Portfolio"
permalink: /research/
author_profile: true
description: "Detailed research projects, industrial translation, and ongoing AI research by Leijie Wu."
---

My research connects efficient, knowledge-enhanced, and trustworthy AI systems. This portfolio records the problems, contributions, evaluation context, and current status behind the highlights in my [CV]({{ '/cv/' | relative_url }}). Peer-reviewed outputs are listed separately under [Publications]({{ '/publications/' | relative_url }}).

**Explore:** [Efficient inference](#efficient-inference) · [Agentic retrieval](#agentic-retrieval) · [Knowledge systems](#knowledge-systems) · [Ongoing research](#ongoing-research) · [Academic foundations](#academic-foundations)

The industrial work below was carried out during my current Research Scientist appointment at Huawei Hong Kong Research Center, which began in December 2024. Quantitative results are from internal evaluations under the stated conditions; they are not general performance guarantees or a substitute for peer-reviewed evidence. Related algorithms are grouped as research programmes rather than counted as separate products.

<h2 id="efficient-inference">Efficient inference and deployment</h2>

### R1 · Long-context sparse attention and KV-cache management

**Focus:** Efficient LLM systems · Long context · GQA and MLA · Hardware-aware optimization

**Problem.** Long-context and agentic workloads increase the cost of attention and KV-cache access. Selecting important KV blocks efficiently can reduce decoding work while retaining useful context.

**Contribution.** I developed hash-based KV-block selection and dynamic sparse-attention methods, with model-specific treatment of grouped-query attention (GQA) and multi-head latent attention (MLA). Related work investigates orthogonal representations, selective aggregation across heads, and adaptive reuse across layers. These are connected parts of the same research direction.

**System integration.** The GQA approach was integrated into Huawei's Unified Cache Management (UCM) framework. The MLA and cross-layer methods have been developed and evaluated; they are not all described here as deployed UCM components.

**Selected evaluation.** On Ascend 910B2 (64 GB) hardware, output-throughput improvements relative to full attention were:

| Model | 16K input / 2K output | 30K input / 4K output | 60K input / 4K output |
| --- | ---: | ---: | ---: |
| Qwen3-32B-BF16 | +13% | +24% | +46% |
| Qwen3-32B-W8A8C16 | +12% | +20% | +46% |

These are configuration-specific output-throughput results. They do not imply the same benefit for every model, batch size, hardware configuration, or end-to-end application. Accuracy measurements and theoretical claims require their full evaluation or proof context and are not reduced to an unqualified headline here.

### R2 · Resource-efficient DeepSeek deployment

**Focus:** Model quantization · LLM deployment · Inference systems

**Problem.** Large model deployment can require multiple servers, making inter-server communication and accelerator cost significant constraints.

**Contribution.** I developed per-channel W4A8 quantization for single-server deployment of a 671B-parameter DeepSeek model on Ascend 910B hardware, reducing reliance on inter-server communication.

**Selected evaluation.** Internal tests reported 2,031.25 tokens/s per-device prefill throughput, an average 95% improvement over the W8A8 baseline in the evaluated setup, and 50% lower accelerator-card cost for the deployment configuration. The latter is a cost comparison, not a claim about total operating cost or a universal reduction in card count. Prefill throughput is a stage-specific metric, not an end-to-end inference-speed claim.

**Related work.** My broader inference research includes speculative decoding and hardware-aware Vision Transformer optimization. The vision solution was commercialized for a hospital medical-image-recognition application.

<h2 id="agentic-retrieval">Agentic retrieval and reasoning</h2>

### R3 · Query decomposition and adaptive retrieval chains

**Focus:** Agentic RAG · Multi-hop question answering · Small-model fine-tuning

**Problem.** Complex questions may require evidence gathered through several dependent retrieval steps; a single retrieval pass can miss the necessary connections.

**Contribution.** I developed a chain-of-retrieval framework that decomposes queries, retrieves evidence, and adapts subsequent subqueries using earlier results. Training combines sampled and verified retrieval trajectories with supervised fine-tuning of a small model. Potential applications include complex question answering and knowledge-intensive assistants.

**Selected evaluation.** Retrieval recall improved over the internally evaluated baseline as follows:

| Dataset | Baseline recall | Method recall | Absolute gain |
| --- | ---: | ---: | ---: |
| 2WikiMultiHopQA | 70.5% | 85.4% | 14.9 percentage points |
| MuSiQue | 35.9% | 64.2% | 28.3 percentage points |

These figures describe retrieval recall, not answer accuracy. The baseline implementation, model versions, and precise recall definition are required for a reproducible comparison; this summary does not claim superiority over every published method.

<h2 id="knowledge-systems">Knowledge construction, retrieval, and maintenance</h2>

### R4 · Hybrid graph retrieval and knowledge lifecycle

**Focus:** Knowledge graphs · Graph-RAG · Dynamic knowledge · Data quality

**Problem.** Knowledge-based assistants need both effective evidence retrieval and a graph that remains usable as source data changes.

**Contribution.** I developed vector-based entry-point retrieval combined with graph-neighbourhood exploration and relation-based filtering. I also developed automated evaluation of extracted triples, formatting repair, and incremental insertion/deletion so that knowledge can be corrected and updated over time.

**Application context.** Related Graph-RAG and knowledge-graph technologies have been used for question answering in financial services, energy, and digital government. Deployment experience and research prototypes are distinguished from formal publications.

**Related publication.** I collaborated with Prof. Yangqiu Song's team at HKUST on [AutoSchemaKG: Autonomous Knowledge Graph Construction through Dynamic Schema Induction from Web-Scale Corpora](https://aclanthology.org/2026.acl-long.942/) (ACL 2026). This coauthored paper is a separate peer-reviewed output; not every industrial component described here is a contribution of that paper.

<h2 id="ongoing-research">Ongoing research</h2>

### R5 · Long-term memory for AI agents

I am developing mechanisms for agents to acquire, organize, retrieve, update, and maintain knowledge over time. A prototype evaluated on LoCoMo showed gains of 29.6 percentage points in Recall@20 and 12.4 percentage points in question-answering accuracy over the evaluated Jiuwen-Memory baseline. These internal prototype results remain separate from published work; model and baseline versions matter when interpreting the comparison. Current research examines memory quality, consistency, privacy, and downstream task performance.

### R6 · Graph-based code intelligence

I am developing graph representations and indexes over large repositories to support retrieval, reasoning, and automated repair. An internal SWE-bench Pro evaluation showed a 13.5-percentage-point issue-resolution improvement over the evaluated Codex baseline. This is a prototype comparison under a specific setup, not a benchmark-wide claim across versions. Follow-up research focuses on repository-level reasoning and reproducible evaluation.

<h2 id="academic-foundations">Academic foundations and student research</h2>

### R7 · Federated learning, unlearning, and edge intelligence

My doctoral research studied incentives, resource allocation, personalized collaboration, and unlearning in distributed AI systems. Representative first-author work includes *Rethinking Personalized Client Collaboration in Federated Learning* (IEEE TMC), *Long-Term Adaptive VCG Auction Mechanism for Sustainable Federated Learning* (IEEE TMC), and *QuickDrop* (Middleware 2024). These provide the foundation for my current interest in efficient and trustworthy agents.

See the [full publication records]({{ '/publications/' | relative_url }}) for authorship, publication status, and paper links. My [CV]({{ '/cv/' | relative_url }}) also records English-medium teaching in AI and data analytics, student mentoring, and academic service.

### Possible student projects

Document-grounded question answering, memory-augmented assistants, efficient model deployment, graph-based code retrieval, and federated learning/unlearning can be scoped as undergraduate prototypes or postgraduate investigations. Evaluation quality, reproducibility, and responsible use of data are central to these directions.
