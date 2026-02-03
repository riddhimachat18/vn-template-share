import qrcode

url = "https://your-domain.com"  # or http://<your-ip>:5000

qr = qrcode.make(url)
qr.save("vn_template_qr.png")

print("QR code created!")