{% include base_path %}

Academic Profile
======
Research scientist at Huawei Hong Kong Research Center working on **efficient, knowledge-enhanced, and trustworthy AI systems**. My research connects federated and edge intelligence with foundation-model inference and memory-augmented agents. I bring experience in algorithm research, industrial system integration, English-medium university teaching, and student research mentoring.

Research Interests
======
Efficient LLM inference; agentic retrieval and memory; knowledge graphs; federated learning, unlearning, and edge intelligence.

Education
======
* __Ph.D. in Computer Science, The Hong Kong Polytechnic University, 2020 – 2024.__
  * Degree conferred Dec. 11, 2024; supervised by [Prof. Song Guo](https://cse.hkust.edu.hk/admin/people/faculty/profile/songguo).
  * Dissertation: *Cooperation & Competition: Mechanism Design for Federated Optimization of Edge Intelligence*.
* __Visiting Ph.D. Student, École Polytechnique Fédérale de Lausanne, May 2023 – Dec. 2023.__
  * School of Computer and Communication Sciences; federated unlearning with [Prof. Anne-Marie Kermarrec](https://people.epfl.ch/anne-marie.kermarrec?lang=en).
* __B.S. in Automation, Beijing Institute of Technology, 2015 – 2019.__
  * Xuteli School; research focus: game theory and control theory.

Research Appointments and Experience
======
* __Research Scientist, Dec. 2024 – Present__
  * System Group, Theory Lab (Huawei 2012 Labs), Huawei Hong Kong Research Center.
  * **Efficient AI systems:** Developed sparse-attention and KV-cache methods, including a GQA approach integrated into Huawei's Unified Cache Management (UCM). Internal Qwen3-32B-BF16 tests on Ascend 910B2 (64 GB) showed 46% higher output throughput than full attention at 60K input / 4K output tokens. Additional work includes W4A8 deployment, speculative decoding, and vision-model optimization for a hospital application.
  * **Knowledge-enhanced AI:** Collaborated with Prof. Yangqiu Song's team at HKUST on [AutoSchemaKG](https://aclanthology.org/2026.acl-long.942/). Developed hybrid vector/graph retrieval and knowledge-graph maintenance for applications in financial services, energy, and digital government.
  * **Agentic retrieval and memory:** Developed query decomposition and adaptive retrieval chains, improving MuSiQue retrieval recall from 35.9% to 64.2% over the internally evaluated baseline. Current work extends to long-term agent memory and graph-based code intelligence.
  * Detailed methods, evaluation conditions, and project status: [Research Portfolio](https://leijiewu.github.io/research/).

* __Research Intern, Huawei Hong Kong Research Center, Dec. 2023 – Aug. 2024.__ Theory Lab; time-series forecasting and multimodal LLM-based retrieval.

* __Research Assistant, The Hong Kong Polytechnic University, Sept. 2019 – Sept. 2020.__ Department of Computing; federated-learning incentives and edge resource optimization with Prof. Song Guo.

* __Research Assistant, Beijing Institute of Technology, Nov. 2018 – Jul. 2019.__ Cooperative UAV–UGV modeling, control, and tracking under visibility constraints with Prof. Kun Liu.

* __Embedded Systems Software Engineer, Zhejiang Dahua Technology Co., Ltd., Apr. – Oct. 2018.__ Debugging, automated testing, and code-coverage analysis for embedded AI camera systems.

Research Agenda
======
**Knowledge- and memory-augmented agentic AI:** reliable evolving knowledge, adaptive retrieval, repository-level reasoning, and efficient, privacy-aware deployment. Detailed directions and prototype results: [Research Portfolio](https://leijiewu.github.io/research/).

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
