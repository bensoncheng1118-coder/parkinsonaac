from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # 需要 pip install flask-cors
import datetime

app = Flask(__name__)
CORS(app) # 允許跨來源資源共用，讓 HTML 能存取 API

# 模擬資料庫
usage_logs = []

@app.route('/')
def index():
    # Flask 會自動到 templates/ 目錄下找 index.html
    return render_template('index.html')
    
@app.route('/api/log', methods=['POST'])
def log_message():
    data = request.json
    content = data.get('message')
    time = data.get('timestamp')
    
    # 這裡可以將資料寫入資料庫 (SQLite/MongoDB)
    print(f"[紀錄] 使用者選擇了: {content} (時間: {time})")
    
    usage_logs.append(data)
    return jsonify({"status": "success", "received": content}), 200

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify(usage_logs), 200

if __name__ == '__main__':
    # 啟動伺服器在 5000 端口
    print("AAC 後端伺服器啟動中...")
    app.run(port=5000, debug=True)
