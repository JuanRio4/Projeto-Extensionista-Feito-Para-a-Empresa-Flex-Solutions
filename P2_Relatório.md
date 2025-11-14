# Relatório 2 - Projeto

**Grupo 2**: Bárbara Melo, Juan Gomes, Leonardo Fila e Rebecca Campos

## Primeiro notebook - Hta_predict.ipynb

O notebook realiza uma análise de risco de ataque cardíaco usando um sistema de lógica fuzzy. O processo se inicia com a importação de bibliotecas essenciais para a manipulação de dados, como `pandas` e `numpy`, além da biblioteca `skfuzzy` para a implementação da lógica fuzzy. Em seguida, ele carrega ou simula um conjunto de dados sobre diabetes, garantindo que o código possa ser executado e testado mesmo sem os dados reais.

O sistema de lógica fuzzy é então construído. Para isso, são definidas as variáveis de entrada, que são a pressão arterial, a idade e a glicose. A variável de saída é o risco de ataque cardíaco. O próximo passo é criar as funções de pertinência, que são representadas por conjuntos fuzzy. Essas funções classificam os valores de entrada em categorias como "baixa", "normal" ou "alta" para as variáveis de entrada, e "baixo", "médio" ou "alto" para a variável de saída.

A lógica central do sistema é definida por quatro regras fuzzy, que estabelecem a relação entre as variáveis de entrada e a saída. Por exemplo, uma das regras determina que se a pressão arterial for alta ou a glicose for alta, o risco de ataque cardíaco é alto. Finalmente, o sistema de controle fuzzy é construído e simulado com um ponto de dados de exemplo do conjunto de dados de diabetes, e o resultado do cálculo do risco de ataque cardíaco é exibido.

### Exemplo de Cálculo do Risco

Com base nos dados de entrada:

- Pressão arterial: **92.00 mmHg**
- Idade: **30.00 anos**
- Glicose: **110.00 mg/dL**

O sistema de lógica fuzzy calculou um risco de ataque cardíaco de **78.31%**.

### Análise dos Resultados

- **Pressão arterial de 92 mmHg**: Considerada alta, enquadrando-se no Estágio 2 de Hipertensão, o que pode ser um fator de risco.
- **Idade de 30 anos**: Classificada como jovem no sistema fuzzy, sem grande impacto no risco.
- **Glicose de 110 mg/dL**: Considerada normal.

Apesar da idade e da glicose não serem fatores de alto risco neste exemplo, a pressão arterial elevada é um fator de peso no sistema de lógica fuzzy. No código, uma das regras determina que "se a pressão arterial for alta ou a glicose for alta, o risco de ataque cardíaco é alto". Como a pressão arterial de 92 mmHg é categorizada como "alta", isso aciona a regra, resultando em um alto risco.

A combinação desses fatores leva a um resultado final de **78.31%** de risco de ataque cardíaco, demonstrando como o sistema de lógica fuzzy pode pesar a importância de cada variável para chegar a uma conclusão final.

---

## Segundo notebook - Health_Monitoring.ipynb

O notebook realiza uma análise de desempenho de modelos de aprendizado de máquina para detecção de diabetes e estresse, com foco na otimização de hiperparâmetros usando um algoritmo genético.

### Modelo de Diabetes

O modelo de diabetes, um classificador `Random Forest`, já demonstrava um desempenho robusto com **99% de acurácia**, apresentando alta precisão e recall para as duas classes.

### Modelo de Estresse

O modelo de estresse, uma **máquina de vetores de suporte (SVM)**, teve uma acurácia de **90%**, mas mostrou uma fraqueza no recall da classe "estresse", que foi de apenas **0.62**, apesar de uma alta precisão de **0.99** para a mesma classe.

### Otimização de Hiperparâmetros com Algoritmo Genético

Para aprimorar esses resultados, o notebook utilizou um **algoritmo genético** para otimizar os hiperparâmetros dos modelos.

- **Modelo de Diabetes**: A otimização resultou nos melhores hiperparâmetros: 
  - `n_estimators = 161`
  - `max_depth = 5`

  Isso elevou a precisão de validação cruzada para **0.9896**. O desempenho final do modelo otimizado foi perfeito, atingindo **100%** de acurácia, precisão, recall e f1-score.

- **Modelo de Estresse**: Os melhores hiperparâmetros encontrados foram:
  - `C = 2.0031`
  - `gamma = 0.0151`

  Com esses parâmetros, a precisão de validação cruzada foi **0.9860**. Após a otimização, o modelo de estresse alcançou **99% de acurácia**, e o recall para a classe "estresse" melhorou significativamente para **0.97**, resolvendo o principal problema do modelo inicial.

---
