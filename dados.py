import pandas as pd

def carregar_dados(caminho_arquivo):
    #Lê o arquivo csv
    df = pd.read_csv(caminho_arquivo)
    #Converter a coluna "data" para datetime
    df['data'] = pd.to_datetime(df['data'], errors='coerce')
    return df


def calcular_volume_total(df):
    #Calcula volumet total de acordo com a carga conforme tipo_carga:
    # - 'Halter' multiplica por 2
    # - 'anilha' e 'placa' mantêm carga normal
    def ajustar_carga(row):
        if row['tipo_carga'] == 'halter':
            return row['carga'] * 2
        elif row['tipo_carga'] in ['anilha', 'placa']:
            return row['carga']
        else:
            return row['carga']
        
    df['carga_ajustada'] = df.apply(ajustar_carga, axis= 1)
    df['volume'] = df['carga_ajustada'] * df['reps'] * df['series']
    return df


def agrupar_por_exercicio(df):
    #Agrupa por exercício e data, somando o volume total
    agrupado = df.groupby(['exercicio', 'data'])['volume'].sum().reset_index()
    return agrupado
