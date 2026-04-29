# การใช้งาน ✏️
## Create file .env
```
LINE_TOKEN=your_token_here
LINE_SECRET=your_secret_here
```

## Ngrok
```bash
ngrok http 8999
```
จากนั้นนำ https เปลี่ยนที่ Webhook URL > [Line Messaging API](https://developers.line.biz/console/channel/2006800711/messaging-api)  
<br>
## วิธีที่ 1 Build ผ่าน Dockerfile 🐋
### 🖼️ Build image
```bash
docker build -t thongdee-linechat:0.1 .
```
### 📦 Run Container
```bash
docker run --rm -p 8999:8999 --name thongdee --env-file .env thongdee-chatbot:0.1
```

---
<br>

## วิธีที่ 2 สร้าง Environment 🏕️
### 📁 สร้าง folder venv
```bash
python -m venv venv
```
### 📖 ติดตั้ง Packages
```bash
pip install -r requirements.txt
```

### 🟢 Avtivate venv
```bash
.\venv\Scripts\activate
```

### ▶️ Rum app
```bash
python main.py
```
