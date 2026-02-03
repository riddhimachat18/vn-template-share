# Deploy to Render - Step by Step

## 🚀 Quick Deploy Guide

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "VN template QR share"
```
Then follow GitHub's instructions to push.

### 2. Deploy on Render
1. Go to **render.com**
2. Sign in with GitHub
3. Click **New → Web Service**
4. Select your repo
5. Settings:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click **Deploy**
7. Wait ~2 minutes

### 3. Test Your URL
Render gives you a URL like: `https://your-app-name.onrender.com`

Test it on your phone browser first!

### 4. Generate QR Code
Update `generate_qr.py` with your Render URL:

```python
import qrcode

url = "https://your-app-name.onrender.com"  # Your Render URL here
qr = qrcode.make(url)
qr.save("vn_template_qr.png")
print("QR code created!")
```

## 📱 User Experience
1. Scan QR → Opens your website
2. Auto-downloads `.vnt` file after 800ms
3. Phone prompts "Open with VN"
4. VN opens import screen
5. Template ready! 🎬

## ⚠️ Important Notes
- VN app must be installed on user's phone
- iPhone users might need to tap "Open in VN" once
- Android usually auto-detects VN

Your template: `naal nachna by peaches._.ncream.vnt` is ready to go!