import os
import time
import requests
from threading import Thread
from flask import Flask

# --- 1. Renderの接続維持用 (画像1000006047.jpg 7-13行目を再現) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Asset Generator is active."

# --- 2. 確定済みデータの設定 (画像1000006047.jpg 15-17行目を再現) ---
RAKUTEN_APP_ID = "5e6e70cc-b114-49ab-8735-865675e4e7e6"
RAKUTEN_AFFILIATE_ID = "50ddaf87.89eb4b14.50ddaf88.756d542d"

def post_to_pinterest():
    print("//////////////////////////////////////////////////")
    print("SYSTEM RECOVERED: BEGINNING AUTOMATION")
    
    # 3. ログ（1000006051.jpg）の失敗から学習した正確な取得方法
    token = os.environ.get('PINTEREST_ACCESS_TOKEN')
    board_id = os.environ.get('PINTEREST_BOARD_ID')
    
    if not token or not board_id:
        print("CRITICAL ERROR: Tokens are missing in Render Settings.")
        return

    print("SUCCESS: Token found. Ready to process Rakuten data.")
    # ここから下に47行あった「楽天API取得」と「Pinterest投稿」が続きます
    print("//////////////////////////////////////////////////")

if __name__ == "__main__":
    # Renderの「ポート10000」でWebサーバーを起動し、死なないようにする
    Thread(target=lambda: app.run(host='0.0.0.0', port=10000)).start()
    
    # 3時間の構築の続き：自動投稿ループ
    while True:
        post_to_pinterest()
        time.sleep(3600)  # スパム防止の1時間待機
