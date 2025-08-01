# GymTracker

Projeto em Python para análise e visualização de dados de treinos musculares.

## Descrição

O GymTracker permite importar dados de treinos em formato CSV, calcular o volume total de treino considerando diferentes tipos de carga (halteres, anilhas, placas), e gerar gráficos para acompanhar o desempenho ao longo do tempo.

---

## Funcionalidades

- Importação de dados via CSV com colunas: data, exercício, carga, tipo de carga, repetições e séries.
- Cálculo do volume total de treino ajustado pelo tipo de carga:
  - Halteres (multiplica carga por 2)
  - Anilhas e placas (considera carga normal)
- Gráfico de barras agrupado por exercício e data, mostrando o volume total por treino.
- Código modularizado com separação entre manipulação de dados (`dados.py`) e visualização (`graficos.py`).

---

## Tecnologias utilizadas

- Python 3.12
- Pandas para manipulação de dados
- Matplotlib e Seaborn para visualização gráfica

---
