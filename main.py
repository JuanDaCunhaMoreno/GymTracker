from dados import carregar_dados, calcular_volume_total
from graficos import grafico_barras_total

def main():
    caminho = 'treino.csv'

    # Carrega e processa os dados
    df = carregar_dados(caminho)
    df = calcular_volume_total(df)

    # Mostra apenas o gráfico de barras
    grafico_barras_total(df)

    print("Gráfico de barras exibido com sucesso.")

if __name__ == "__main__":
    main()
