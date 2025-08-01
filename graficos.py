import matplotlib.pyplot as plt
import seaborn as sns

#Visual seaborn
sns.set(style="whitegrid")


def grafico_linha_volume(df_agrupado):
    #Plota um gráfico de linha mostrando evolução no exercício
    plt.figure(figsize=(10, 6)) #Tamanho da figura
    #Plota uma linha para cada exercício
    for exercicio in df_agrupado['exercicio'].unique():
        dados = df_agrupado[df_agrupado['exercicio'] == exercicio]
        plt.plot(dados['data'], dados['volume'], marker = 'o', label = exercicio)

    plt.title("Volume de Treino por Exercício")
    plt.xlabel('Data')
    plt.ylabel('Volume Total')
    plt.legend(title= 'Exercicio')
    plt.xticks(rotation = 45) #Rotaciona datas
    plt.tight_layout()
    plt.show() #Exibe o gráfico

    
def grafico_barras_total(df):
        #Plota um gráfico de barras com o volume total
        #Agrupa dados por data e soma o volume total
        volume_diario = df.groupby('data')['volume'].sum().reset_indnex()

        plt.figure(figsize=(10, 6)) #Tamanho da figura
        sns.barplot(x= 'data', y= 'volume', data= volume_diario, color= 'skyblue') #Plota as barras

        plt.title('Volume Total de Treino por Dia')
        plt.xlabel('data')
        plt.ylabel('Volume Total')
        plt.xticks(rotation= 45)
        plt.tight_layout()
        plt.show


 def grafico_pizzas_exerciocios(df):
        #Plota gráfico de pizza
        #Agrupa um gráfico de pizza e mostra a proporção de volume por exercício
        volume_por_exercicio = df.groupby('exercicio')['volume'].sum()
        plt.figure(figsize=( 8, 8))
        plt.pie(volume_por_exercicio, labels= volume_por_exercicio.index, autopct= '%1.1f%%', startangle= 140) 
        plt.axis('equal')
        plt.show
