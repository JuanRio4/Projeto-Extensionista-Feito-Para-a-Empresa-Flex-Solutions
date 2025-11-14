# Relatório 5 - Projeto

**Grupo 2**: Bárbara Melo, Juan Gomes, Leonardo Fila e Rebecca Campos

---

## Introdução

Este relatório apresenta os resultados de uma simulação de **consultoria de Inteligência Artificial** focada na **previsão de pontuações de questionários clínicos em idosos**, utilizando dados de **wearables** do dataset **MAISON-LLF**. O objetivo é demonstrar o potencial da IA para automatizar e aprimorar os serviços de saúde, permitindo o monitoramento proativo e a intervenção personalizada.

---

## Metodologia

Para esta análise, foram utilizados os arquivos **all-features-imputed.csv** e **demographic-coded.csv** do dataset **MAISON-LLF**. As variáveis-alvo para regressão foram as pontuações dos questionários clínicos:

- **SIS** (Social Isolation Scale)
- **OHS** (Oxford Hip Score)
- **OKS** (Oxford Knee Score)

Foram empregados três modelos de regressão:

1. **Regressão Linear**
2. **Random Forest Regressor**
3. **Gradient Boosting Regressor**

Os dados foram divididos em conjuntos de treino e teste (**80/20**), e um pipeline de pré-processamento foi aplicado, incluindo escalonamento de features numéricas.

As métricas de avaliação utilizadas foram:

- **Erro Quadrático Médio (MSE)**
- **Raiz do Erro Quadrático Médio (RMSE)**
- **Coeficiente de Determinação (R²)**

---

## Explicação das Variáveis

### Variáveis-Alvo (o que o modelo prevê)

- **SIS (Social Isolation Scale):** Pontuação que indica o nível de isolamento social do indivíduo. Valores mais altos geralmente significam menor isolamento (melhor).
- **OHS (Oxford Hip Score):** Pontuação que avalia a dor e a função da articulação do quadril. Valores mais altos indicam melhor função e menos dor.
- **OKS (Oxford Knee Score):** Pontuação que avalia a dor e a função da articulação do joelho. Valores mais altos indicam melhor função e menos dor.

### Variáveis Preditivas (o que o modelo usa para prever)

- **Características Demográficas:** Incluem informações como idade, gênero e nível de escolaridade dos participantes, que ajudam a contextualizar os dados.
- **Características dos Sensores:** Derivadas dos wearables, estas são estatísticas diárias de diferentes sensores, como:
  - **Aceleração:** Mede o movimento do corpo, indicando atividade física e intensidade.
  - **Batimentos Cardíacos:** Mede a frequência cardíaca, relevante para saúde cardiovascular e estresse.
  - **Movimento e Passos:** Quantificam a mobilidade e o nível de atividade física.
  - **Posição:** Indica a postura (em pé, sentado, deitado) e padrões de comportamento.
  - **Sono:** Detalha a duração e qualidade do sono, um indicador de saúde geral.

---

## Resultados

Os modelos demonstraram um desempenho notavelmente alto na previsão das pontuações clínicas. Abaixo, um sumário dos resultados:

| Modelo                      | Variável-Alvo | MSE     | RMSE    | R²     |
|-----------------------------|---------------|---------|---------|--------|
| **Linear Regression**        | **SIS**       | 0.0000  | 0.0000  | 1.0000 |
|                             | **OHS**       | 0.0000  | 0.0000  | 1.0000 |
|                             | **OKS**       | 0.0000  | 0.0000  | 1.0000 |
| **Random Forest Regressor**  | **SIS**       | 0.0332  | 0.1823  | 0.9971 |
|                             | **OHS**       | 0.0393  | 0.1981  | 0.9995 |
|                             | **OKS**       | 0.0087  | 0.0934  | 0.9999 |
| **Gradient Boosting Regressor** | **SIS**    | 0.0013  | 0.0364  | 0.9999 |
|                             | **OHS**       | 0.0009  | 0.0301  | 1.0000 |
|                             | **OKS**       | 0.0322  | 0.1795  | 0.9997 |



## Discussão e Recomendações

Os resultados demonstram que os **dados de wearables** e **informações demográficas** do dataset **MAISON-LLF** são extremamente eficazes na previsão das pontuações clínicas. O desempenho quase perfeito da **Regressão Linear** (R² = 1.0000, MSE = 0.0000) para todas as variáveis-alvo é notável, e os modelos **Random Forest** e **Gradient Boosting** também apresentaram R² muito próximos de 1, o que é um forte indicativo da capacidade preditiva dos dados.

Isso valida o potencial do uso de **wearables** para:

- **Monitoramento Contínuo:** Prever o estado de saúde e bem-estar de idosos de forma não invasiva.
- **Intervenção Proativa:** Identificar tendências ou mudanças nas pontuações clínicas que possam indicar a necessidade de intervenção médica ou social.
- **Personalização do Cuidado:** Adaptar planos de cuidado e suporte com base em previsões individualizadas.

As próximas etapas seriam realizar **engenharia de features** mais complexa e otimizar os modelos para **implantação em um ambiente real**.

---
