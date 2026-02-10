import ccxt
import time
import os

# GitHub Secretsから安全に鍵を読み込みます
api_key = os.getenv('GMO_API_KEY')
secret_key = os.getenv('GMO_API_SECRET')

gmo = ccxt.gmocoin({
    'apiKey': api_key,
    'secret': secret_key,
})

def trade_logic():
    print("24時間監視プログラム起動。利益を狙い続けます。")
    while True:
        try:
            ticker = gmo.fetch_ticker('BTC/JPY')
            print(f"現在価格: {ticker['last']}円 - 監視中...")
            # ここに他取引所との差額判定ロジックを自動注入します
            time.sleep(1) # 1秒ごとにチェック
        except Exception as e:
            print(f"待機中: {e}")
            time.sleep(10)

if __name__ == "__main__":
    trade_logic()
