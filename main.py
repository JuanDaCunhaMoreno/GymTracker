from dados import carregar_dados, calcular_volume_total
from graficos import grafico_barras_agrupado_por_exercicio

def main():
    caminho = 'treino.csv'
    df = carregar_dados(caminho)
    df = calcular_volume_total(df)

    grafico_barras_agrupado_por_exercicio(df)

    print("Gráfico agrupado por exercício e data exibido.")

if __name__ == "__main__":
    main()
