import matplotlib.pyplot as plt
import seaborn as sns

def grafico_barras_total(df):
    # Agrupa o volume total por data
    df_total = df.groupby('data')['volume'].sum().reset_index()

    # Estilo visual
    sns.set(style="whitegrid")

    # Criação do gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x='data', y='volume', data=df_total, palette='Blues_d')

    # Títulos e rótulos
    plt.title('Volume Total de Treino por Dia')
    plt.xlabel('Data')
    plt.ylabel('Volume Total')
    plt.xticks(rotation=45)

    # Exibe o gráfico
    plt.tight_layout()
    plt.show()
