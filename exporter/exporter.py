# ライブラリインポート
import yfinance
import prometheus_client
import time
from prometheus_client import Gauge, start_http_server

# 監視する銘柄リスト
TICKERS = ["RKLB","SOFI","7974.T"]

# Gaugeを定義
stock_price = Gauge("stock_price","Stock_price",["ticker"])

def collect_prices():
    # TICKERSをループして
    # yfinanceで株価を取得して
    # Gaugeに値をセットする
    for ticker in TICKERS:
        stock = yfinance.Ticker(ticker)
        price = stock.info["currentPrice"]
        stock_price.labels(ticker=ticker).set(price)


if __name__ == "__main__":
    start_http_server(8080) #HTTPサーバ起動
    while True:
        collect_prices()
        time.sleep(60)      #60秒待つ
