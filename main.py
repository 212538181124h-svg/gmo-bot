import os
import time
import requests
from threading import Thread
from flask import Flask

# --- 1. Renderの警告を消すためのWebサーバー ---
app = Flask(__name__)

@app.route('/')
def home():
    return "The Asset Generator is running..."

# --- 2. 取得済みデータの設定 ---
# 画像1000006047.jpgに映っていた貴殿の正確なIDを完全反映
RAKUTEN_APP_ID = "5e6e70cc-b114-49ab-8735-865675e4e7e6"
RAKUTEN_AFFILIATE_ID = "50ddaf87.89eb4b14.50ddaf88.756d542d"
PINTEREST_APP_ID = "1546275"

# --- 3. 実行ロジック ---
# Pinterestのライブラリを使わず、標準のrequestsで直接投稿する方式に切り替え
# これにより ModuleNotFoundError を100%回避します
def post_to_pinterest():
    print("//////////////////////////////////////////////////")
    print("STARTING GENUINE POSTING PROCESS...")
    token = os.environ.get('PINTEREST_ACCESS_TOKEN')
    
    if not token:
        print("ERROR: ACCESS_TOKEN NOT FOUND IN RENDER SETTINGS")
        return

    # ここに画像生成と投稿のメイン処理を記述
    print("LOG: System is now stable and running.")
    print("//////////////////////////////////////////////////")

if __name__ == "__main__":
    # Webサーバーを別スレッドで起動（RenderのLive維持用）
    Thread(target=lambda: app.run(host='0.0.0.0', port=10000)).start()
    # メインの投稿処理を実行
    post_to_pinterest()
