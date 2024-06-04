---
title: "On Knowledge Editing in Federated Learning: Perspectives, Challenges, and Future Directions"
collection: publications
permalink: /publication/2023-06-02-On-Knowledge-Editing-in-Federated-Learning-Perspectives-Challenges-and-Future-Directions
excerpt: 'This paper is about knowledge editing in federated learning.'
date: 2023-06-02
venue: 'ArXiv'
paperurl: 'https://arxiv.org/abs/2306.01431' 
citation: '<b>Leijie Wu</b>, Song Guo, Junxiao Wang, Zicong Hong, Jie Zhang, and Jingren Zhou. &quot;On Knowledge Editing in Federated Learning: Perspectives, Challenges, and Future Directions.&quot; <i>ArXiv</i>. 2023.'
---


Federated Learning (FL) has gained considerable attention recently, as it allows clients to cooperatively train a global machine learning model without sharing raw data. However, its performance can be compromised due to the high heterogeneity in clients' local data distributions, commonly known as Non-IID (non-independent and identically distributed). Moreover, collaboration among highly dissimilar clients exacerbates this performance degradation. Personalized FL seeks to mitigate this by enabling clients to collaborate primarily with others who have similar data characteristics, thereby producing personalized models. We noticed that existing methods for assessing model similarity often do not capture the genuine relevance of client domains. In response, our paper enhances personalized client collaboration in FL by introducing a metric for domain relevance between clients. Specifically, to facilitate optimal coalition formation, we measure the marginal contributions of client models using coalition game theory, providing a more accurate representation of potential client domain relevance within the FL privacy-preserving framework. Based on this metric, we then adjust each client's coalition membership and implement a personalized FL aggregation algorithm that is robust to Non-IID data domain. We provide a theoretical analysis of the algorithm's convergence and generalization capabilities. Our extensive evaluations on multiple datasets, including MNIST, Fashion-MNIST, CIFAR-10, and CIFAR-100, and under varying Non-IID data distributions (Pathological and Dirichlet), demonstrate that our personalized collaboration approach consistently outperforms contemporary benchmarks in terms of accuracy for individual clients.
