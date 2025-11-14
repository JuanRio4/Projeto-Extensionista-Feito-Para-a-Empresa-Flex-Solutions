# Relatório de Projeto: Implementação de Wearables Voltados ao Público Geriátrico

## 1. Introdução
O projeto tem como objetivo a implementação de **wearables** voltados ao público geriátrico, focando na detecção precoce de emergências médicas, como quedas e problemas cardíacos, e no despacho eficiente de resgates para hospitais. O uso de algoritmos de busca permite otimizar o caminho de resgate, considerando diferentes bases, pacientes e hospitais.

## 2. Cenário do Projeto
O cenário envolve um sistema de despacho em que **ambulâncias** partem de diferentes bases, atendem pacientes que usam wearables e os transportam até hospitais. O projeto explora duas abordagens de algoritmos de busca:

- **Busca Gulosa (Greedy Best-First Search)**: Expande nós com base somente na heurística (estimativa de tempo restante), sem considerar o custo já percorrido.
- **A* (A Star)**: Expande nós considerando tanto o custo acumulado quanto a heurística, permitindo encontrar o caminho mais eficiente.

## 3. Representação do Grafo e Heurística

### Código 1 (Fictício)
- Coordenadas em sistema cartesiano (x, y) em **km**.
- Grafo com várias **bases**, **bairros**, **paciente** e **hospitais**.
- **Heurística**: Distância em linha reta convertida em tempo (km/min).

### Código 2 (Realista)
- Coordenadas em **latitude e longitude** reais.
- Grafo simplificado com **Base → Paciente → Hospital**.
- **Heurística**: Fórmula de **Haversine** convertida em tempo estimado, considerando velocidade média urbana.

## 4. Algoritmos de Busca
Ambos os códigos implementam os algoritmos de busca **Gulosa** e **A\***.

- **Busca Gulosa**: `f(n) = h(n)`, prioriza a expansão de nós com menor estimativa de tempo até o objetivo.
- **A\***: `f(n) = g(n) + h(n)`, considera custo acumulado (`g`) e heurística (`h`) para encontrar o caminho ótimo.

### Diferenças de Implementação
- **Código 1**: Permite passar a função heurística como parâmetro, contabiliza nós expandidos, reconstrói caminhos detalhando o custo de cada aresta e calcula todas as combinações possíveis de rotas.
- **Código 2**: Fixa a heurística internamente, reconstrói o caminho de forma mais enxuta e foca na visualização da rota em um grafo usando **networkx** e **matplotlib**.

## 5. Saídas e Análise
- **Código 1**: Gera **CSVs** com todas as combinações de rotas e as melhores rotas por algoritmo, além de prints resumidos com tempo total estimado e nós expandidos.
- **Código 2**: Exibe no console uma **rota de exemplo** e plota graficamente a rota do **A\*** no mapa.

## 6. Comparação entre os Códigos

| **Aspecto**                       | **Código 1**                               | **Código 2**                               |
|------------------------------------|--------------------------------------------|--------------------------------------------|
| **Coordenadas**                    | Cartesianas fictícias                      | Latitude/Longitude reais                   |
| **Heurística**                     | Distância euclidiana                       | Fórmula de Haversine                       |
| **Grafo**                          | Complexo, múltiplas rotas                  | Simples, rota única                        |
| **Foco**                           | Comparação de algoritmos, análise de performance | Visualização e teste de rota única         |
| **Saídas**                         | CSVs e prints                              | Print e gráfico visual                     |
| **Algoritmo**                      | Passagem de heurística como parâmetro, contagem de nós expandidos | Heurística fixa, reconstrução enxuta, foco visual |

## 7. Conclusão
- **Código 1** é mais adequado para estudos de desempenho e análise comparativa entre algoritmos em cenários complexos.
- **Código 2** é mais adequado para implementação prática com dados reais, permitindo visualização do caminho de resgaste e validação rápida.

Aliamos os **algoritmos de busca eficientes** à implementação de **wearables para idosos**, visando otimizar significativamente o tempo de resposta em emergências, aumentando a **segurança** e a **qualidade de vida** do público-alvo.
