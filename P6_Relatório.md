# Relatório 6 – Projeto  
**Grupo 2:** Bárbara Melo, Juan Gomes, Leonardo Fila e Rebecca Campos  

# Relatório de Funcionalidade: Sistema de Simulação para Monitoramento do Bem-Estar de Idosos

## Propósito do Sistema
O sistema de simulação tem como objetivo monitorar a Qualidade de Vida Diária de um idoso, baseando-se na análise de sentimento de suas falas. Para garantir a precisão do monitoramento, o sistema incorpora uma simulação de **Distinção de Voz (Speaker Diarization)** usando o conceito de tensores de aprendizado de máquina.

O processo é dividido em quatro etapas principais:  
1. Simulação de Dados  
2. Simulação de Distinção de Voz  
3. Análise de Sentimento  
4. Agregação Ponderada  

---

## 1. Simulação de Dados (O Diário de Sentimentos)
Esta etapa gera o conjunto de dados brutos para a análise, simulando as falas registradas ao longo de uma semana.

- **Simulação de Locutores:** As frases são geradas e atribuídas a dois locutores: *Idoso* e *Outra Pessoa* (cuidadores, familiares etc.).  
- **Variação Semanal:** Pesos de probabilidade são atribuídos para sentimentos (positivo, neutro, negativo) em cada dia da semana, simulando oscilações emocionais típicas.

---

## 2. Simulação de Distinção de Voz com Tensores
- **Função de Simulação:** Emula a saída de um modelo de verificação de locutor, retornando um tensor PyTorch representando a probabilidade de ser o idoso.  
- **Frases do Idoso:** Probabilidade entre **0.7 e 0.9**.  
- **Frases de Outra Pessoa:** Probabilidade entre **0.1 e 0.3**.  
- **Uso de Tensor:** Demonstra como modelos de Deep Learning representam e manipulam informações numéricas.

---

## 3. Análise de Sentimento
- **Pré-processamento:** O spaCy é usado para tokenização e análise linguística em português.  
- **Classificação:** Léxico simples classifica frases como **POSITIVE**, **NEUTRAL** ou **NEGATIVE**, com pontuação de confiança.  
- **Quantificação:**  
  - Positivo: **1.0**  
  - Neutro: **0.5**  
  - Negativo: **0.0**

---

## 4. Agregação Ponderada e Visualização (A Nota de Qualidade do Dia)
- **Ponderação por Voz:** O valor numérico do sentimento é multiplicado pela probabilidade de ser o idoso.  
- **Cálculo por Dia:** A média ponderada é calculada para cada dia da semana.  
- **Normalização:** A média diária é normalizada para uma escala de **0 a 10**, gerando a *Nota de Qualidade do Dia*.  
- **Visualização:** Um gráfico de barras exibe a variação semanal.

---

## Conclusão
O sistema apresenta um protótipo conceitual que integra técnicas de PLN e simulação com tensores para gerar um indicador mais confiável de bem-estar, focado exclusivamente nas falas do idoso, isolando interferências de terceiros.
