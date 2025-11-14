# Relatório 6 - Projeto

**Grupo 2:** Bárbara Melo, Juan Gomes, Leonardo Fila e Rebecca Campos

## Relatório de Funcionalidade: Sistema de Simulação para Monitoramento do Bem-Estar de Idosos

### Propósito e Funcionalidade: Entendendo o Humor Semanal do Idoso

O sistema de simulação opera em três etapas principais, que juntas criam um ciclo de monitoramento semanal focado nas variações emocionais do idoso simulado:

### 1. Geração de Dados de Simulação (O Diário de Sentimentos)
Esta seção cria o "material bruto" para a análise, simulando o registro diário de pensamentos e eventos que refletem diferentes estados emocionais (positivos, neutros e negativos) que um idoso pode vivenciar.

- **Simulação de Variação Semanal:** O código atribui pesos de probabilidade diferentes para cada dia da semana, simulando uma rotina com altos e baixos emocionais típicos. Por exemplo, a simulação inclui dias programados para serem predominantemente positivos (como o Sábado) e dias predominantemente negativos (como a Segunda-feira), refletindo a variação extrema solicitada para um acompanhamento mais sensível.

### 2. Análise de Sentimento Aprimorada com spaCy
O coração da simulação é o módulo de análise de sentimento, que foi aprimorado com a implementação da biblioteca **spaCy**, uma ferramenta de Processamento de Linguagem Natural (PLN) de nível profissional.

- **Melhoria na Análise:** A substituição do classificador simples (dummy) pelo **spaCy** garante um pré-processamento de texto mais sofisticado, que respeita as regras da língua portuguesa. Isso inclui uma tokenização mais precisa (separação correta das palavras), o que é fundamental para qualquer análise de texto.
  
- **Classificação Baseada em Léxico:** Embora a lógica de classificação ainda utilize um léxico simplificado (lista de palavras-chave), o **spaCy** fornece a infraestrutura para uma análise mais robusta. Isso significa que, no futuro, o sistema pode ser facilmente expandido para incluir técnicas avançadas como a identificação de negação ou o uso de modelos de aprendizado de máquina pré-treinados, tornando a análise de humor muito mais precisa e contextual.

- **Quantificação do Humor:** A cada classificação de sentimento é atribuído um valor numérico (1 para positivo, 0.5 para neutro e 0 para negativo), permitindo que o humor do idoso seja medido de forma objetiva.

### 3. Agregação e Visualização de Resultados (A Nota de Qualidade do Dia)
A etapa final transforma os dados brutos e classificados em um resultado compreensível e visual, crucial para o acompanhamento do idoso.

- **Cálculo da Qualidade do Dia:** A média dos valores de sentimento de todas as frases de um dia é calculada para gerar uma Pontuação Diária, normalizada para uma escala de 0 a 10, representando a Nota de Qualidade do Dia do Idoso.

- **Visualização Gráfica:** Um gráfico de barras é criado para apresentar visualmente a variação da Nota de Qualidade do Dia ao longo da semana. Isso permite que cuidadores e familiares identifiquem rapidamente padrões de bem-estar, dias de maior fragilidade ou períodos de humor elevado com base em uma análise de texto mais confiável.

### Conclusão: Um Indicador de Bem-Estar Mais Confiável
Em resumo, o código funciona como um protótipo conceitual focado no monitoramento do idoso. A implementação do **spaCy** move o sistema de uma simulação muito básica para um protótipo com base técnica sólida, que traduz dados textuais em uma métrica de bem-estar diário. O resultado é uma visualização clara do monitoramento de humor semanal, demonstrando como a tecnologia de PLN pode oferecer insights objetivos e mais confiáveis para apoiar o cuidado e a qualidade de vida da pessoa idosa.
