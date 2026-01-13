# Flask Demo - Python Web Application

這是一個簡易的 Python Flask 網站，可以部署到 Render。

## 專案結構

```
FlaskDemo/
├── app.py              # Flask 主程式
├── requirements.txt    # Python 套件清單
└── README.md          # 說明文件
```

## 本地執行

1. 安裝套件：
```bash
pip install -r requirements.txt
```

2. 執行應用：
```bash
python app.py
```

3. 開啟瀏覽器訪問：`http://localhost:5000`

## 部署到 Render

1. 將專案推送到 GitHub
2. 在 Render 建立新的 Web Service
3. 連結 GitHub Repository
4. Render 會自動偵測並部署

## 功能

- ✅ 簡易的 Flask Web Server
- ✅ 美觀的 HTML 介面
- ✅ 健康檢查端點 (`/health`)
- ✅ 自動讀取 Render 的 PORT 環境變數

https://flaskdemoflaskdemo-python-124.onrender.com/
