# Predicting student dropouts with machine learning: An empirical study in Finnish higher education

## Resumo
O presente artigo tem como objetivo investigar de forma precoce e precisa quais estudantes de uma determinada universidade finlandesa possuem maior probabilidade de abandonar o curso. Para essa pesquisa, foram utilizados alguns modelos de Machine Learning, a fim de analisar padrões nos dados de histórico acadêmico, demográficos e do sistema de gestão de aprendizagem (LMS - Moodle).

## Descrição dos Dados
Para o estudo, foi utilizada uma amostra de 8.813 alunos durante o período de 2015 a 2020. Aproximadamente 76% dos estudantes, ou seja, 6.664 alunos se formaram durante esse intervalo, enquanto 2.149 (24%) evadiram. Quanto à divisão dos dados, os registros do ano de 2025, foram utilizados como conjunto de dados de testes, em contrapartida, os dados dos demais anos compuseram o conjunto de treinamento.

- Dados demográficos: gênero, nível de instrução anterior, prioridade de inscrição, curso, língua materna, semestre de início e a idade na matrícula.
- Histórico acadêmico: créditos acumulados, GPA (coeficiente de rendimento), quantidade de disciplinas reprovadas e de dias de intercâmbio.
- LMS - Moodle: frequência de login, abertura de links, entrega de trabalhos, comentários e participação em discussões.

Vale citar que todas as variáveis foram separadas como categóricas e numéricas, além de serem classicadas como variantes ou invariantes no tempo.

| Tipo           | Feature                        | Tipo de Dado / Valores                                      |
|----------------|--------------------------------|-------------------------------------------------------------|
| **Invariante no Tempo** |  Gênero                       | Categórico: male (51%), female (49%)                        |
|                | Nível de Instrução          | Categórico: high school (55%), vocational (31%), other (14%) |
|                | Prioridade           | Categórico: top priority (69%), not top priority (31%)      |
|                | Curso                   | Categórico: engineering (33%), nursing (17%), business (15%), hospitality (5%), data processing (5%), other 210 ETCS programs (14%), other 240 ETCS programs (12%) |
|                | Língua Materna                 | Categórico: Finnish (94%), not Finnish (6%)                 |
|                | Semestre de início                  | Categórico: autumn (89%), spring (11%)                      |
|                | Idade na matrícula               | Numérico, decimal: anos                                     |
|                | Saída                          | Categórico: graduation (76%), dropout (24%)                 |
| **Variante no Tempo**   | Números de meses presente        | Numérico, inteiro: meses (1–60)                              |
|                | Números de meses ausente        | Numérico, inteiro: meses (1–60)                              |
|                | Créditos acumulados     | Numérico, inteiro                                            |
|                | GPA (grade point average)       | Numérico, decimal: 1–5                                      |
|                | Número de reprovações        | Numérico, inteiro                                            |
|                | Número de dias de intercâmbio        | Numérico, inteiro                                            |
|                | Quantidade de atividades no Moodle          | Numérico, inteiro                                            |
|                | Tendência no Moodle       | Categórico: decreasing (43%), increasing (37%), stagnating (20%) |


_Tabela 1: Separação dos Dados_

## Modelos de Machine Learning
Foram utilizados 10 modelos de classificação, onde cada um passou por 60 treinamentos. No entanto, apenas três mostraram maior desempenho:
- CATBoost (CAT);
- Redes Neurais (NN);
- Regressão Logística (LR).

### Pré-processamento dos Dados
Para as variáveis de tipo categórica, foi realizado o "One-Hot Encoding", a fim de transformar cada variável desse tipo em uma coluna binária, o que proporciona maior robustez aos modelos. Ademais, as variáveis numéricas passaram por Z-Score, o que as colocou na mesma escala, isso permite que as variáveis sejam consideradas de forma igualitária, sem que uma sobressaia a outra.

## Resultados

|    Modelo     |    AUC   |     AP    |   F1-score   |   Precisão   |   Recall  |
|---------------|----------|-----------|--------------|--------------|-----------|
|   CatBoost    |   0.853  |   0.721   |      59%     |      81%     |     47%   |
| Redes Neurais |   0,844  |   0.698   |      58%     |      76%     |     47%   |
| Regressão Logística |   0,842  |   0.696   |      58%     |      82%     |     42%   |

_Tabela 2: Métricas dos principais modelos_

Obs.: Além das métricas utilizadas, também foi feita uma matriz de correlação, a fim de identificar a multicolinearidade entre as variáveis.

![resultados1](https://github.com/user-attachments/assets/a63f76f0-28a3-48c7-a1ed-5234b8e3ef65)
_Figura 1: Análise de desempenho ao longo do tempo_

## Conclusão 
Por fim, o estudo trata principalmente dos aspectos relacionados ao desempenho e engajamento dos estudantes. É importante ressaltar que, o sistema possui suas contribuições focadas em comparar as fontes dos dados, a fim de entender quais features são mais relevantes, além de realizar uma análise mensal e medir o desempenho dos modelos de maneira contínua. Essa análise mensal contribui para a tentativa de diminuir as taxas de evasão de forma precoce, visto que o modelo tem a capacidade de realizar a predição da possível evasão antes mesmo do final do semestre letivo.

Com isso, pode-se concluir que analisar o engajamento, motivação e comprometimento dos estudantes em suas atividades pode auxiliar no enfrentamento ao problema de evasão escolar. No entanto, cabe citar ainda, que devido às diferenças culturais, é importante considerar outras variáveis relevantes ao caso, quando visto dentro do cenário brasileiro. Desse modo, é necessário dar importância à inclusão de dados que também englobem as diversidades socioeconômicas, regionais e culturais.
