# VN QR Share

Share VN video editing templates via QR codes that auto-download on mobile devices.

## How it works
1. QR Code → Your web page (Python server)
2. Auto-download .vn file
3. VN opens → Import Project

## Compatibility
✅ Android  
✅ iPhone (Safari / Chrome)  
❌ Desktop (downloads file normally)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your .vn template file to the `static/` folder

3. Update the filename in `app.py` if needed (currently set to `my_template.vn`)

4. Run the server:
```bash
python app.py
```

5. Generate QR code:
```bash
python generate_qr.py
```

## Deployment

For public sharing, host on:
- Render
- Railway  
- PythonAnywhere
- VPS (DigitalOcean)

⚠️ Localhost QR will NOT work publicly

## Usage

1. Update the URL in `generate_qr.py` with your deployed domain
2. Generate and share the QR code
3. Users scan → template opens directly in VN

## Instagram Caption Template

```
Scan the QR 📲 Template opens directly in VN 🎬
(Just tap download if prompted)
```