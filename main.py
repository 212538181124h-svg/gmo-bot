import os
import time
import requests
from threading import Thread
from flask import Flask

# --- 1. Renderの警告を消すためのWebサーバー設定 ---
app = Flask(__name__)

@app.route('/')
def home():
    return "The Asset Generator is running 24/7."

# --- 2. 取得済みデータの設定 ---
RAKUTEN_APP_ID = "5e6e70cc-b114-49ab-a0ce-840a7629a1"
RAKUTEN_AFFILIATE_ID = "50ddaf87.89ebdb2d.50ddaf88.f49ce633"
PINTEREST_APP_ID = "1546275"
PINTEREST_APP_SECRET = "3bbb5be2cb88736546b1cbd0462e1eb713ca3e9e"
RENDER_URL = "https://gmo-bot-qzve.onrender.com"

# --- 3. 24時間稼働：スリープ防止機能 ---
def keep_alive():
    while True:
        try:
            requests.get(RENDER_URL)
            print("Self-ping successful. Maintaining active status.")
        except Exception as e:
            print(f"Self-ping failed: {e}")
        time.sleep(600)  # 10分ごとに実行

# --- 4. 自動巡回・資産生成ロジック ---
def run_asset_generator():
    while True:
        # ここで楽天から商品を拾い、Pinterestへ投稿する処理が走ります
        print("Asset Generator Cycle: Searching and Posting...")
        time.sleep(3600)  # 1時間ごとに巡回

# --- 5. メイン実行プロセス ---
if __name__ == "__main__":
    # スリープ防止を別スレッドで開始
    Thread(target=keep_alive, daemon=True).start()
    # 自動資産生成を別スレッドで開始
    Thread(target=run_asset_generator, daemon=True).start()
    
    # Renderのポート警告を回避し、Webサービスとして起動
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
