---
title: "CIIA"
author: "x"
date: "Julho/2025"
subject: "Evasão Escolar"
keywords: [CIIA]
subtitle: "Dados de Entrada"
...

# Introdução

A evasão escolar é um desafio crítico que afeta a qualidade da educação e o futuro dos alunos. O governo federal brasileiro, por meio do Ministério da Educação (MEC), tem como política pública a prevenção da evasão escolar, propondo a implementação de Sistema de Alerta Preventivo (SAP) como uma ferramenta diagnóstica para identificar precocemente estudantes em situação de risco. A estratégia proposta é identificar alunos com risco de evasão escolar precocemente, permitindo intervenções direcionadas e eficazes.

Este documento contém informações sobre os dados de entrada utilizados no projeto de prevenção de evasão escolar. Os dados são fundamentais para treinar modelos preditivos.

Devido à dificuldade de acesso a dados reais, foi elaborado um conjunto de dados sintéticos utilizando uma metodologia própria, detalhada neste documento. Esses dados simulados possibilitam o desenvolvimento e a validação dos modelos de Machine Learning, permitindo testar cenários próximos à realidade e avaliar a eficácia das soluções propostas.


# Referencial teórico

A evasão escolar é um fenômeno complexo que envolve múltiplos fatores, incluindo aspectos socioeconômicos, acadêmicos e emocionais. A literatura aponta que a identificação precoce de alunos em risco é crucial para implementar intervenções eficazes. Estudos recentes têm utilizado técnicas de Machine Learning para prever a evasão escolar, analisando dados históricos e comportamentais dos alunos.

O Manual do Sistema de Alerta Preventivo (SAP), publicado pelo Ministério da Educação no âmbito do Programa Brasil na Escola, apresenta um conjunto de estratégias para prevenção da evasão e abandono escolar. O SAP é uma ferramenta diagnóstica que visa identificar precocemente estudantes em situação de risco, combinando dados individuais (como situação socioeconômica, histórico escolar, absenteísmo) com informações da escola. A metodologia propõe um modelo de intervenção em quatro etapas:
i) Mapeamento de riscos, por meio de questionários aplicados periodicamente;
ii) Interpretação das devolutivas, permitindo análise qualitativa dos fatores de risco;
iii) Escuta ativa, em que profissionais capacitados realizam entrevistas estruturadas para aprofundar o entendimento sobre os riscos identificados;
iv) Ações preventivas, implementadas de forma universal, seletiva ou indicativa, conforme o perfil de risco de cada estudante.

O SAP adota práticas baseadas em evidências internacionais, respeitando as especificidades de cada rede de ensino, e busca não apenas mitigar fatores associados à evasão, mas também promover um acompanhamento contínuo e personalizado. O manual ainda reforça a necessidade de revisão periódica das práticas adotadas, prevenção da estigmatização dos alunos e integração de ações escolares com políticas sociais mais amplas (@mec2022sap).


**A FAZER**: revisão dos trabalhos indicados abaixo

@pereira2025machine

@pereira2024early

@vaarma2024predicting

@psyridou2024machine



# Estrutura dos Dados Proposta

A partir das propostas encontradas na literatura, foi proposto a arquitetura de dados a seguir, que contempla as principais variáveis identificadas como relevantes para a previsão de evasão escolar. A estrutura é dividida em quatro categorias principais: dados demográficos, desempenho acadêmico, fatores socioeconômicos e histórico escolar.

**A FAZER**: definir a estrutura de dados a partir da proposta feita pelo Lucas Costa.


# Metodologia de Geração de Dados Sintéticos


A metodologia de geração de dados sintéticos foi desenvolvida para simular cenários realistas de evasão escolar, permitindo o treinamento e validação dos modelos preditivos. A seguir, são apresentados os passos principais da metodologia.

## 1. Criação do DataFrame

 com as colunas identificadas na seção anterior


## 2. Rotulação dos dados

Rotulação de dados aleatória seguindo a proporção de evasão escolar observada no Brasil, que é de aproximadamente XXX dos alunos. A rotulação é feita de forma aleatória, garantindo que XXX dos dados sejam marcados como "evasão" e os demais como "não evasão".

## 3. Geração de Atributos Sintéticos

Para cada coluna do DataFrame, são gerados valores sintéticos com base em distribuições estatísticas adequadas.
Os parâmetros das distribuições são, preferencialmente, definidos com base em dados reais disponíveis na literatura e em estatísticas educacionais do Brasil. Não sendo possível, são utilizados parâmetros fictícios, mas plausíveis, para simular a realidade educacional brasileira. Destaca-se que os parâmetros, no geral, são distintos para o caso de evasão e não evasão, refletindo as diferenças esperadas entre os grupos. Caso contrário, a respectiva coluna não tem correlação com a evasão escolar.

### Sexo do aluno

Para o caso de "não evasão", a coluna "sexo" é gerada com base na proporção de alunos do sexo masculino e feminino no Brasil, que é de aproximadamente XXX.

Para o caso de "evasão", utiliza-se a fórmula de Bayes para calcular a probabilidade de ser do sexo masculino ou feminino, considerando a proporção de evasão escolar por sexo. 

**A FAZER**: ver estatísticas e calcular a distribuição para o caso de "evasão".





