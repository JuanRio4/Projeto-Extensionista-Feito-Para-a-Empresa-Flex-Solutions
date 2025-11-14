# Relatório 3 - Projeto

**Grupo 2:** Bárbara Melo, Juan Gomes, Leonardo Fila e Rebecca Campos

---

## Relatório sobre o Dataset MHEALTH e Resultados da Árvore de Decisão

### 📌 Dataset MHEALTH

O dataset **MHEALTH (UCI Machine Learning)** contém dados de **10 voluntários** realizando **12 atividades**, capturados por sensores de aceleração, giroscópio e ECG posicionados no peito, pulso e tornozelo.  
Ele possui aproximadamente **1,2 milhão de amostras**, com **23 atributos** e uma coluna **label**, que indica a atividade realizada.

### **Significado dos Rótulos (label):**

- **0:** Nulo (sem atividade ou baseline)  
- **1:** Em pé  
- **2:** Sentado  
- **3:** Deitado  
- **4:** Andando  
- **5:** Subindo escadas  
- **6:** Descendo escadas  
- **7:** Elevação do braço com peso (3kg)  
- **8:** Rotação do braço com peso (3kg)  
- **9:** Correndo  
- **10:** Ciclismo  
- **11:** Saltando  
- **12:** Jogando bola (atividades dinâmicas)

---

## 📊 Resultados da Árvore de Decisão

A Árvore de Decisão foi treinada no **Orange**, utilizando a coluna *label* como alvo. Os resultados obtidos foram:

- **Acurácia (CA):** 0,943 (94,3%)  
- **F1 Score:** 0,942  
- **Precisão:** 0,943  
- **Recall:** 0,943  
- **MCC:** 0,882  

---

## 🧠 Interpretação

Os resultados demonstram um **excelente desempenho** na classificação das atividades, estando alinhados com benchmarks típicos para o dataset **MHEALTH**, que variam entre **90% e 95% de acurácia**.

Isso indica que o modelo conseguiu capturar bem os padrões presentes nos sinais dos sensores, diferenciando adequadamente as atividades realizadas pelos voluntários.

---
