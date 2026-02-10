import os
import time
import requests
import random
from threading import Thread
from flask import Flask

# --- [秘書による完全復元：自動巡回エンジンの心臓部] ---
app = Flask(__name__)
@app.route('/')
def home(): return "AI_AGENT_ARBITRAGE_ACTIVE"

# 1. 貴殿が取得した「正解」の資産データ（画像1000006047.jpgより転記）
RAKUTEN_APP_ID = "5e6e70cc-b114-49ab-8735-865675e4e7e6"
RAKUTEN_AFFILIATE_ID = "50ddaf87.89eb4b14.50ddaf88.756d542d"

def fetch_rakuten_data():
    """楽天APIを自動巡回し、裁定対象の商品をスキャンする"""
    url = f"https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId={RAKUTEN_APP_ID}&affiliateId={RAKUTEN_AFFILIATE_ID}&sort=%2BitemPrice&hits=5"
    try:
        res = requests.get(url, timeout=10)
        return res.json().get('Items', [])
    except: return []

def post_to_pinterest(item_name, item_url, image_url):
    """デジタル資産をPinterestに自動配置し、放置収益の基盤を作る"""
    token = os.environ.get('PINTEREST_ACCESS_TOKEN')
    board_id = os.environ.get('PINTEREST_BOARD_ID')
    if not token or not board_id: return False
    
    # 外部ライブラリを一切使わず、requestsだけで直接APIを叩く（劣化回避）
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "board_id": board_id,
        "media_source": {"source_type": "image_url", "url": image_url},
        "title": item_name[:90],
        "link": item_url
    }
    r = requests.post("https://api.pinterest.com/v5/pins", json=payload, headers=headers)
    return r.status_code == 201

def agent_workflow():
    """AIエージェントの自動巡回・裁定・放置サイクル"""
    print("//////////////////////////////////////////////////")
    print("AGENT: STARTING AUTO-ARBITRAGE SCAN...")
    
    items = fetch_rakuten_data()
    if not items:
        print("AGENT: No target items found. Retrying in next cycle.")
        return

    for item in items:
        data = item['Item']
        name = data['itemName']
        url = data['affiliateUrl']
        img = data['mediumImageUrls'][0]['imageUrl']
        
        print(f"AGENT: Found Profit Asset -> {name[:20]}...")
        if post_to_pinterest(name, url, img):
            print("SUCCESS: Digital Asset Placed on Pinterest.")
        time.sleep(10) # 連続投稿回避

    print("AGENT: CYCLE COMPLETE. ENTERING AUTO-SLEEP.")
    print("//////////////////////////////////////////////////")

if __name__ == "__main__":
    # Renderの死活監視をクリア
    Thread(target=lambda: app.run(host='0.0.0.0', port=10000)).start()
    # 永遠に続く不労所得サイクル
    while True:
        agent_workflow()
        time.sleep(3600) # 1時間ごとに巡回
