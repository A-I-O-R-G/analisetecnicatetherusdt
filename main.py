import requests
import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Função para coletar dados históricos da Tether (USDT)
def coletar_dados_historicos(symbol: str, interval: str = '1d', limit: int = 100) -> pd.DataFrame:
    try:
        # Usando a API da Binance para coletar dados de preços
        url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
        response = requests.get(url)
        response.raise_for_status()  # Verificar se a requisição foi bem-sucedida
        data = response.json()
    except requests.RequestException as e:
        print(f'Erro ao fazer a requisição: {e}')
        return pd.DataFrame()

    # Estruturando os dados em um DataFrame
    df = pd.DataFrame(data, columns=['open_time', 'open', 'high', 'low', 'close', 'volume', 
                                      'close_time', 'quote_asset_volume', 'number_of_trades', 
                                      'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['close'] = df['close'].astype(float)
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    return df[['open_time', 'close']]

# Função para calcular a média móvel
def media_movel(df: pd.DataFrame, period: int) -> pd.Series:
    return df['close'].rolling(window=period).mean()

# Função para calcular o Índice de Força Relativa (RSI)
def calcular_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    delta = df['close'].diff(1)
    ganho = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    perda = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = ganho / perda
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Função para plotar os dados em um gráfico
def plotar_graficos(df: pd.DataFrame, symbol: str) -> None:
    fig = go.Figure()
    
    # Preço de fechamento
    fig.add_trace(go.Scatter(x=df['open_time'], y=df['close'], mode='lines', name='Preço de Fechamento'))
    
    # Média Móvel de 20 períodos
    fig.add_trace(go.Scatter(x=df['open_time'], y=media_movel(df, 20), mode='lines', name='Média Móvel 20'))
    
    # RSI
    rsi_series = calcular_rsi(df)
    fig.add_trace(go.Scatter(x=df['open_time'], y=rsi_series, mode='lines', name='RSI'))
    
    # Configurações do gráfico
    fig.update_layout(title=f'Análise Técnica da {symbol}',
                      xaxis_title='Data',
                      yaxis_title='Preço (USD)')
    
    # Salvar gráfico como imagem
    fig.write_image(f'{symbol}_grafico.png')
    fig.show()

# Função para exibir estatísticas resumidas
def exibir_estatisticas(df: pd.DataFrame) -> None:
    print('Estatísticas Resumidas:')
    print(f'Média: {df["close"].mean():.2f}')
    print(f'Mediana: {df["close"].median():.2f}')
    print(f'Desvio Padrão: {df["close"].std():.2f}')

# Execução do script
if __name__ == '__main__':
    symbol = 'USDTBUSD'  # Par Tether para o Binance USD
    df = coletar_dados_historicos(symbol)
    if not df.empty:
        exibir_estatisticas(df)
        plotar_graficos(df, symbol)