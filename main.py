import ccxt
import time
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

def trade_logic():
    api_key = os.getenv('GMO_API_KEY')
    secret_key = os.getenv('GMO_API_SECRET')
    gmo = ccxt.gmocoin({'apiKey': api_key, 'secret': secret_key})
    print("24時間監視プログラム起動。利益を狙い続けます。")
    while True:
        try:
            ticker = gmo.fetch_ticker('BTC/JPY')
            print(f"現在価格: {ticker['last']}円 - 監視中...")
            time.sleep(30)
        except Exception as e:
            print(f"待機中: {e}")
            time.sleep(10)

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_health_check_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=trade_logic, daemon=True).start()
    run_health_check_server()
