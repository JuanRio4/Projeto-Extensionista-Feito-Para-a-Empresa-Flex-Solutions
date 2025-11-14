# Plano de Ação para Detecção de Emergências Cardíacas

## 1. Revisar e Expandir o Léxico Médico
Focar na curadoria de um vocabulário robusto para emergências cardíacas, indo além do corpus inicial. É crucial revisar a literatura médica para incluir:
- Sinônimos
- Termos técnicos
- Descrições de sintomas

Esses termos podem não estar presentes no texto original, mas sua inclusão garante uma cobertura mais ampla para o algoritmo de detecção.

## 2. Definir um Dicionário de Termos-Chave para Implementação
Criar uma base de dados ou um dicionário estruturado (e.g., JSON, CSV) que mapeie os termos médicos identificados para categorias de risco ou ações específicas. Exemplos:
- **Dor torácica** e **irradiação para o braço** podem ser associados a um **nível de alerta alto**, servindo de base para os thresholds do sistema de wearables.

## 3. Ampliar o Corpus de Análise
Expandir a coleta de dados para incluir:
- Artigos científicos
- Diretrizes médicas
- Prontuários anonimizados

Isso aumentará a variabilidade e a riqueza do vocabulário, permitindo que o modelo de Processamento de Linguagem Natural (PLN) seja treinado com um material mais diversificado e representativo de cenários clínicos reais.

## 4. Avançar para Análise Semântica de Contexto
Evoluir da simples contagem de frequência e busca de palavras para técnicas mais avançadas, como:
- **Análise de sentimento**
- **Modelagem de tópicos (topic modeling)**

O objetivo é capacitar o sistema a não apenas identificar um termo, mas também a compreender o **contexto** em que ele aparece. Isso permitirá, por exemplo, distinguir uma menção histórica de um sintoma ativo.

## 5. Desenvolver um Protótipo de Integração
Planejar a integração da análise de PLN com dados simulados de sensores de wearables (como frequência cardíaca e SpO₂). O objetivo é criar um protótipo que demonstre como:
- Um pico na **frequência cardíaca**, correlacionado com a detecção de termos como **palpitação** ou **desconforto**, poderia acionar um protocolo de emergência de forma mais precisa.
