from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML 模板
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Demo - Python Web App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            background: white;
            padding: 3rem;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 500px;
        }
        h1 {
            color: #667eea;
            margin-top: 0;
            font-size: 2.5rem;
        }
        .success {
            color: #28a745;
            font-size: 1.2rem;
            margin: 1rem 0;
        }
        .info {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        .badge {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.5rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐍 Flask Demo</h1>
        <p class="success">✅ Python Flask 運行成功！</p>
        <div class="info">
            <p><strong>這是一個簡易的 Flask 網站</strong></p>
            <p>部署在 Render 上</p>
        </div>
        <div>
            <span class="badge">Python</span>
            <span class="badge">Flask</span>
            <span class="badge">Render</span>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {"status": "ok", "message": "Flask app is running!"}

if __name__ == '__main__':
    # Render 會自動設定 PORT 環境變數
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
