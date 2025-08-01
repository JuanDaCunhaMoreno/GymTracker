import pandas as pd

def carregar_dados(caminho_arquivo):
    #Lê o arquivo csv
    df = pd.read_csv(caminho_arquivo)
    #Converter a coluna "data" para datetime
    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    return df


def calcular_volume_total(df):
    #Cria nova coluna "Volume" = carga * reps * séries e adiciona ao DataFrame.
    df['volume'] = df['carga'] * df['reps'] * df['series']
    return df


def agrupar_por_exercicio(df):
    #Agrupa por exercício e data, somando o volume total
    agrupado = df.groupby(['exercicio', 'data'])['volume'].sum().reset_index()
    return agrupado