{% include base_path %}

Academic Profile
======
Research scientist specializing in **efficient, knowledge-enhanced, and trustworthy AI systems**. My research connects federated and edge intelligence with efficient foundation-model inference and knowledge- and memory-augmented AI agents. I combine algorithm and system development with real-world deployment across financial services, digital government, energy, and healthcare. My future research focuses on agentic AI systems that can construct structured knowledge, maintain reliable long-term memory, and operate efficiently under practical data and computing constraints.

Research Interests
======
Agentic AI and long-term memory; graph-based retrieval-augmented generation and knowledge graphs; efficient foundation-model inference; federated, privacy-preserving, and edge intelligence.

Research Appointments and Experience
======
* __Research Scientist, Dec. 2024 – Present__
  * System Group, Theory Lab (Huawei 2012 Labs), Huawei Hong Kong Research Center.
  * **Efficient LLM inference:** Developed model-quantization algorithms that achieve more than 2× inference acceleration without measurable accuracy degradation, and a speculative-decoding method that delivers more than 50% speedup over the multi-token prediction baseline on DeepSeek models. Both have been incorporated into a joint Huawei–DeepSeek LLM inference-acceleration project.
  * **Knowledge-enhanced AI:** Collaborated with Prof. Yangqiu Song's team at HKUST on [AutoSchemaKG](https://aclanthology.org/2026.acl-long.942/). Related Graph-RAG and knowledge-graph technologies have been deployed for high-precision question answering over financial transactions, nuclear power plant technical manuals, and digital government services.
  * **Agentic AI:** Developed graph-based code intelligence and agentic-memory prototypes with measurable gains on SWE-bench Pro and LoCoMo; detailed results are summarized under Research Agenda and Current Pipeline.
  * **Multimodal inference acceleration:** Developed hardware-aware optimizations for Vision Transformer models on Huawei NPUs; the solution was commercialized for a medical image-recognition project at a leading tertiary hospital.

* __Research Intern, Dec. 2023 – Aug. 2024__
  * System Group, Theory Lab (Huawei 2012 Labs), Huawei Hong Kong Research Center.
  * Conducted research on AI-empowered time-series forecasting and multimodal LLM-based information retrieval.

* __Research Assistant, Sept. 2019 – Sept. 2020__
  * Department of Computing, The Hong Kong Polytechnic University; supervised by Prof. Song Guo.
  * Studied deep-reinforcement-learning-based incentive mechanisms and resource optimization for federated learning and mobile edge intelligence.

* __Research Assistant, Nov. 2018 – Jul. 2019__
  * State Key Laboratory of Intelligent Control and Decision of Complex Systems, Beijing Institute of Technology; supervised by Prof. Kun Liu.
  * Developed cooperative UAV–UGV system models, control laws, and tracking algorithms under dynamic visibility constraints.

* __Embedded Systems Software Engineer, Apr. 2018 – Oct. 2018__
  * Zhejiang Dahua Technology Co., Ltd.; worked on debugging, automated testing, and code-coverage analysis for embedded AI camera systems.

Education
======
* __Ph.D. in Computer Science, The Hong Kong Polytechnic University, 2020 – 2024.__
  * Degree conferred Dec. 11, 2024; supervised by [Prof. Song Guo](https://cse.hkust.edu.hk/admin/people/faculty/profile/songguo).
  * Dissertation: *Cooperation & Competition: Mechanism Design for Federated Optimization of Edge Intelligence*.
* __Visiting Ph.D. Student, École Polytechnique Fédérale de Lausanne, May 2023 – Dec. 2023.__
  * School of Computer and Communication Sciences; supervised by [Prof. Anne-Marie Kermarrec](https://people.epfl.ch/anne-marie.kermarrec?lang=en).
  * Research focus: federated unlearning.
* __B.S. in Automation, Beijing Institute of Technology, 2015 – 2019.__
  * Xuteli School; research focus: game theory and control theory.

Research Agenda and Current Pipeline
======
My current research agenda centers on **knowledge- and memory-augmented agentic AI systems**, building on my earlier work in federated learning, privacy-aware optimization, and edge intelligence.

* **Agentic Memory for Personalized and Domain-Specific AI:** Developing a memory harness that enables AI agents to acquire, organize, retrieve, update, and maintain long-term knowledge. A prototype evaluated on LoCoMo outperforms Huawei's open-source Jiuwen-Memory baseline by 29.6 percentage points in Recall@20 and 12.4 percentage points in question-answering accuracy. Ongoing research investigates memory quality, consistency, privacy, and downstream agent performance.
* **Graph-Based Knowledge Construction and Retrieval:** Extending autonomous knowledge construction and Graph-RAG toward continuously updated domain knowledge systems. Current enterprise validation focuses on high-precision question answering in finance, nuclear power, and digital government, with follow-up academic research under development.
* **Graph-Based Code Intelligence:** Constructing graph representations and indexes over large code repositories to support repository-level retrieval, reasoning, and automated repair. On SWE-bench Pro, the current system improves the issue-resolution pass rate by 13.5 percentage points over a Codex baseline.
* **Efficient and Trustworthy Agent Deployment:** Investigating model compression, speculative decoding, hardware-aware optimization, and privacy-preserving learning to deploy agentic AI under practical latency, computing, and data-governance constraints.

Publications
======
<small><sup>*</sup> Equal contribution.</small>

### Peer-Reviewed Journal Articles

<ul>{% assign journal_publications = site.publications | where: "publication_type", "journal" | sort: "date" %}{% for post in journal_publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

### Peer-Reviewed Conference Papers

<ul>{% assign conference_publications = site.publications | where: "publication_type", "conference" | sort: "date" %}{% for post in conference_publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

### Preprints

<ul>{% assign preprint_publications = site.publications | where: "publication_type", "preprint" | sort: "date" %}{% for post in preprint_publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

Teaching Experience
======
* **Teaching Assistant, Department of Computing, The Hong Kong Polytechnic University, 2020 – 2023.**
  * Led English-medium tutorials across all listed courses for classes of approximately 50–100 students, preparing tutorial slides and supporting teaching materials.
  * Managed student-facing teaching responsibilities as a TA, including consultation and learning support, assignments, course projects, examinations, and grading.
  * Courses:
    * [COMP4431: Artificial Intelligence](https://www.polyu.edu.hk/comp/docdrive/ug/subject/COMP4431.pdf), Fall 2020 — Level 4 undergraduate course covering problem solving and search, knowledge representation and reasoning, and machine learning.
    * [COMP4434: Big Data Analytics](https://www.polyu.edu.hk/comp/docdrive/ug/subject/COMP4434.pdf), Fall 2021 — Level 4 undergraduate course covering NoSQL data management, Hadoop and MapReduce, machine learning, graph analytics, recommender systems, and data visualization.
    * [COMP5511: Artificial Intelligence Concepts](https://www.polyu.edu.hk/comp/docdrive/tpg/subject/COMP5511.pdf), Spring and Fall 2022 — Level 5 postgraduate course covering search and game playing, knowledge representation and reasoning, uncertainty management, expert systems, machine learning, and neural networks.
    * [COMP4121: E-Commerce Technology and Applications](https://www.polyu.edu.hk/comp/docdrive/ug/subject/COMP4121.pdf), Spring 2023 — Level 4 undergraduate course covering web technologies, cryptography and internet security, electronic payment systems, and e-commerce system design and implementation.

Research Supervision and Mentoring
======
* **Master's research mentoring:** Mentored at least five master's students on dissertation research. In Fall 2022, provided day-to-day research guidance to Zhaoyang Zhang on his dissertation, *Personalized Federated Prompt Learning*, which received an outstanding dissertation award at PolyU.
* **Undergraduate research mentoring:** Mentored at least 10 undergraduate students. Among them, Yaohong Ding coauthored [QuickDrop](https://dl.acm.org/doi/10.1145/3652892.3700764), published at Middleware 2024, and is now pursuing a Ph.D. at The Education University of Hong Kong under the supervision of [Prof. Yu Yang](https://repository.eduhk.hk/en/persons/yu-yang/).
* **Industry research mentoring:** Mentored at least five Huawei research interns on research development, system implementation, and translation into industrial applications.

Honors and Awards
======
* **Huawei Hong Kong Research Center Star Award (港研之星) – Team Award, Aug. 2026.**
  * Awarded as a member of the Knowledge Engineering and Knowledge Graph Team.

Selected Conference Presentations
======
<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>

Academic Service
======
* **Conference reviewer:** IJCAI, ICML, AAAI, NeurIPS, and IEEE INFOCOM.
* **Journal reviewer:** IEEE Transactions on Mobile Computing, IEEE Transactions on Cloud Computing, IEEE Internet of Things Journal, and IEEE Transactions on Sustainable Computing.

Technical Skills
======
* **Programming:** Python, C, C++, MATLAB.
* **Machine learning and distributed systems:** PyTorch, TensorFlow, Spark, Ray, Docker, and Linux.
* **Languages:** Mandarin (native), Cantonese (fluent), and English (proficient).
