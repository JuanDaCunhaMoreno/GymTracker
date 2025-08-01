import matplotlib.pyplot as plt
import seaborn as sns

def grafico_barras_agrupado_por_exercicio(df):
    """
    Plota gráfico de barras agrupando volume por exercício e data,
    com barras lado a lado (hue = exercício).
    """
    # Agrupa por exercício e data somando o volume
    df_agrupado = df.groupby(['exercicio', 'data'])['volume'].sum().reset_index()

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Gráfico de barras com hue para exercícios
    sns.barplot(x='data', y='volume', hue='exercicio', data=df_agrupado, palette='Set2')

    plt.title('Volume de Treino por Exercício e Data')
    plt.xlabel('Data')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)
    plt.legend(title='Exercício')
    plt.tight_layout()
    plt.show()
