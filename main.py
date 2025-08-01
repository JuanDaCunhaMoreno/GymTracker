from dados import calcular_volume_total, carregar_dados, agrupar_por_exercicio
from graficos import grafico_linha_volume, grafico_barras_total, grafico_pizzas_exerciocios

def main():
    #Caminho do arquivo CSV
    caminho = 'Treino.csv'
    #Carregar dados
    df = carregar_dados(caminho)
    df = calcular_volume_total(df)
    df_agrupado = agrupar_por_exercicio(df)
    #Gerar gráfico
    grafico_linha_volume(df_agrupado)
    grafico_barras_total(df)
    grafico_pizzas_exerciocios(df)
    #Encerrar o programa
    print("Programa finalizado com sucesso.")

if __name__ == "__main__":
    main()