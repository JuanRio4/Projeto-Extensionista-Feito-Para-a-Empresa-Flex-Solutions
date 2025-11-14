# Aplicação de Redes Neurais (LSTM) para Consultoria de IA

### Grupo 2: Bárbara Melo, Juan Gomes, Leonardo Fila e Rebecca Campos

## 1. Contexto e Objetivo Técnico
Este relatório detalha a aplicação de uma **Rede Neural Recorrente (LSTM)** para a **classificação de atividades** e **detecção de inatividade prolongada** em idosos, utilizando o dataset público e real **HAR70+** (Human Activity Recognition 70+). O objetivo técnico do código (`analise_har70.py`) é demonstrar o fluxo de trabalho completo de **Machine Learning** para séries temporais, incluindo:
- Carregamento de dados brutos
- Pré-processamento
- Janelamento
- Treinamento
- Avaliação do modelo

## 2. Análise do Dataset HAR70+
O dataset **HAR70+** é composto por dados de **acelerômetros triaxiais** (6 eixos) coletados de 18 idosos (faixa etária de 70-95 anos).

### Características
- **Features (Entrada):**  
  6 eixos de aceleração:
  - `back_x`, `back_y`, `back_z` (costas)
  - `thigh_x`, `thigh_y`, `thigh_z` (coxa)
- **Rótulos (Saída):**  
  Atividades anotadas, como:
  - Caminhando
  - Sentado
  - Deitado
- **Taxa de Amostragem:**  
  50 Hz (amostras por segundo)

## 3. Fluxo de Trabalho do Código (`analise_har70.py`)

O código implementa as seguintes etapas cruciais para o processamento de séries temporais:

### 3.1. Carregamento e Pré-processamento (`carregar_dataset` e `criar_janelas_e_features`)
1. **Carregamento:**  
   A função `carregar_dataset` itera sobre os 18 arquivos CSV do **HAR70+** e concatena os dados de aceleração e os rótulos de atividade em um único **DataFrame**.
   
2. **Normalização:**  
   Os dados brutos de aceleração são normalizados utilizando **MinMaxScaler** para garantir que todas as features contribuam igualmente para o treinamento da rede neural.
   
3. **Janelamento (Windowing):**  
   O código aplica o janelamento, transformando a série temporal contínua em sequências discretas de tempo.
   - **Tamanho da Janela:** 250 amostras (equivalente a 5 segundos a 50 Hz).
   - **Passo (Step):** 100 amostras (equivalente a 2 segundos, resultando em 60% de sobreposição).

4. **Classificação Binária:**  
   Para a detecção de risco, os rótulos de atividade são mapeados para uma classificação binária:
   - **Classe 0 (Atividade Normal):** Caminhando, Subindo/Descendo Escadas, Sentado, Em Pé.
   - **Classe 1 (Repouso/Risco):** Deitado (Lying), utilizado como proxy para inatividade prolongada ou risco.

### 3.2. Arquitetura da Rede Neural (`treinar_modelo_lstm`)
A arquitetura escolhida é a **Long Short-Term Memory (LSTM)**, ideal para capturar dependências temporais em dados de séries.

| **Camada**   | **Tipo**                     | **Unidades/Função**                   | **Propósito**                        |
|--------------|------------------------------|---------------------------------------|--------------------------------------|
| 1            | LSTM                         | 64 unidades, `return_sequences=True`  | Extrai características sequenciais e mantém a saída para a próxima camada LSTM. |
| 2            | Dropout                      | 0.2                                   | Previne overfitting.                |
| 3            | LSTM                         | 32 unidades                           | Extrai características sequenciais finais. |
| 4            | Dropout                      | 0.2                                   | Previne overfitting.                |
| 5            | Densa                        | 1 unidade, `sigmoid`                  | Classificação binária final (0 ou 1). |

## 4. Resultados e Avaliação do Modelo

O modelo foi treinado por **5 épocas** e avaliado em um conjunto de teste (20% dos dados).

| **Métrica**           | **Valor**  | **Interpretação**                                                    |
|-----------------------|------------|----------------------------------------------------------------------|
| **Acurácia no Conjunto de Teste** | 0.9102     | O modelo classificou corretamente 91.02% das janelas de tempo como **Atividade Normal** ou **Repouso/Risco**. |
| **Dados de Entrada**  | 22.594 janelas de tempo (cada uma com 250 timesteps e 6 features de aceleração) |                                          |
| **Janelas de Amostras de Risco (Classe 1)** | 2.031  | O modelo foi treinado com 2.031 janelas de risco (Deitado).             |

## 5. Conclusão Técnica

O código `analise_har70.py` e os resultados obtidos com o dataset **HAR70+** validam a escolha da arquitetura **LSTM** para o monitoramento de idosos. A acurácia de **91.02%** demonstra a alta capacidade do modelo em distinguir padrões de movimento e inatividade prolongada a partir de dados reais de acelerômetros, fornecendo uma base sólida para o desenvolvimento de um **sistema de alerta de risco**.

Este relatório é estritamente técnico e focado na análise do código e dos resultados obtidos com o dataset **HAR70+**.
