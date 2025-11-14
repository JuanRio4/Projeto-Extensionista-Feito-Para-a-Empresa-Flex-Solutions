# Relatório 4 - Projeto

**Grupo 2**: Bárbara Melo, Juan Gomes, Leonardo Fila e Rebecca Campos

---

## Contexto e Objetivo

Este relatório apresenta uma análise de viabilidade para a aplicação de **Inteligência Artificial (IA)** na detecção e previsão de quedas em idosos, utilizando dados de dispositivos **wearables**. O objetivo é recomendar uma base de dados e abordar a implementação de modelos de **Machine Learning** para uma empresa de automação em serviços de saúde.

---

## Base de Dados: cStick.csv (Elderly Fall Prediction and Detection)

**Link da base**: [cStick.csv - Kaggle](https://www.kaggle.com/datasets/laavanya/elderly-fall-prediction-and-detection?resource=download&select=cStick.csv)

A base de dados **cStick.csv**, originada de um projeto de pesquisa sobre um protótipo de bengala (*cStick*) feito para prever quedas de idosos, foi utilizada para esta análise. Ela contém dados de sensores como **distância**, **pressão**, **Variabilidade da Frequência Cardíaca (HRV)**, **níveis de açúcar**, **SpO2** e **leituras de acelerômetro**.

A variável alvo (**Decision**) classifica os eventos em três categorias:

- **0:** Sem queda
- **1:** Escorregão/tropeço/previsão de queda
- **2:** Queda definitiva

O dataset possui **2039 entradas** e **não apresenta valores ausentes**, o que o torna ideal para o desenvolvimento de modelos de **Machine Learning**.

---

## Modelos de Machine Learning Aplicados

Para avaliar a capacidade de classificação do dataset, foram implementados e testados os seguintes algoritmos de **Machine Learning**, com pré-processamento de padronização das features e avaliação robusta via **K-Fold Cross-Validation** (5 folds):

1. **Support Vector Machine (SVM)**: Um classificador poderoso que busca o hiperplano ótimo para separar as classes.
2. **k-Nearest Neighbors (k-NN)**: Um classificador não-paramétrico que classifica instâncias com base na proximidade de seus vizinhos.
3. **Regressão Logística**: Um modelo linear generalizado que estima a probabilidade de uma instância pertencer a uma classe.

---

## Desempenho dos Modelos

Todos os modelos testados demonstraram um desempenho excepcional no dataset **cStick.csv**:

- **SVM (K-Fold):** Acurácia média de **1.0000** (+/- **0.0000**)
- **k-NN (K-Fold):** Acurácia média de **1.0000** (+/- **0.0000**)
- **Regressão Logística (K-Fold):** Acurácia média de **1.0000** (+/- **0.0000**)

Os resultados de **100% de acurácia**, tanto na divisão treino/teste quanto na validação cruzada, indicam que as classes no dataset **cStick.csv** são altamente separáveis. Isso sugere um forte potencial para a detecção e previsão de quedas com **alta confiabilidade** neste contexto específico.

---

## Aprendizagem por Regras (Rule-Based Learning)

A **Aprendizagem por Regras** é uma abordagem de **Machine Learning** que se baseia na extração de regras **"SE-ENTÃO"** (IF-THEN) a partir dos dados para realizar classificações ou previsões. Diferente dos modelos paramétricos como **SVM** ou **Regressão Logística**, os modelos baseados em regras são altamente **interpretáveis**, o que pode ser uma vantagem significativa em aplicações de saúde, onde a explicabilidade das decisões é crucial.

- **Conceito**: Um exemplo de regra poderia ser:  
  *SE Distance < 10 E Pressure == 2 ENTÃO Decision = 2 (Queda Definitiva).*

### Implementação e Resultados (CN2 Rule Induction)

Para explorar esta abordagem, foi utilizado o algoritmo **CN2 Rule Induction** na ferramenta **Orange**. Os resultados obtidos com o CN2 reforçam a alta separabilidade do dataset **cStick.csv** e a eficácia da **Aprendizagem por Regras**:

- **Acurácia (CA):** **0.998**
- **F1-Score:** **0.998**
- **Recall:** **0.998**

Esses resultados demonstram que, mesmo com um modelo baseado em regras, que oferece maior interpretabilidade, é possível alcançar uma performance de classificação extremamente alta. Isso valida ainda mais o potencial do dataset para a construção de sistemas de **detecção e previsão de quedas** com **alta confiabilidade** e **transparência** nas decisões.


---

## Conclusão

O dataset **cStick.csv** é uma base de dados altamente adequada para o desenvolvimento de soluções de IA para **detecção de quedas em idosos**. Os modelos de **Machine Learning** avaliados (SVM, k-NN, Regressão Logística e Aprendizagem por Regras com CN2) demonstraram excelente desempenho, validado por **K-Fold Cross-Validation**.

Esta abordagem integrada oferece um caminho promissor para automação em serviços de saúde no desenvolvimento de soluções de **monitoramento de idosos com wearables**, combinando **alta performance preditiva** com a possibilidade de **interpretabilidade** para decisões clínicas.

---
