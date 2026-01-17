from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os
import asyncio
from telethon import TelegramClient

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# ==================== Telegram 配置區域 ====================
API_ID = 31340109
API_HASH = "d8c89a5a75a37dea30d7dec64dbe4e1b"
PHONE_NUMBER = "+886937604266"

# 要發送訊息的目標列表（目標、訊息）
TARGETS = [
    ("@auto_sheerid_bot", "/qd"),
    ("@sheeridverifier_bot", "/checkin"),
]
# =========================================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vip')
def vip():
    return render_template('vip.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash('感謝您的訊息！我們會盡快回覆您 😊', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/send-telegram')
def trigger_telegram():
    """
    透過網頁或 Cron-job.org 觸發發送訊息
    """
    # 這裡加入簡單的安全性檢查 (選用)
    auth_key = request.args.get('key')
    # if auth_key != "your_custom_secure_key":
    #     return jsonify({"status": "error", "message": "Unauthorized"}), 401

    try:
        # 在 Flask 中執行非同步任務
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(send_telegram_messages())
        return jsonify({"status": "success", "results": results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

async def send_telegram_messages():
    """發送訊息給所有目標的核心邏輯"""
    # 使用與 Kiro1 相同的 session 檔案名稱
    client = TelegramClient('session_name', API_ID, API_HASH)
    results = []
    
    try:
        await client.start(phone=PHONE_NUMBER)
        
        for target, message in TARGETS:
            try:
                await client.send_message(target, message)
                results.append(f"✓ 已發送給 {target}")
            except Exception as e:
                results.append(f"✗ 發送給 {target} 失敗: {str(e)}")
        
    except Exception as e:
        results.append(f"!! 連接失敗: {str(e)}")
    finally:
        await client.disconnect()
    
    return results

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
