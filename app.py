from flask import Flask, render_template, send_from_directory, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/qr")
def show_qr():
    # Get the current URL (your local IP)
    host_url = request.host_url
    
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(host_url)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64 for display in HTML
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
    
    return render_template("qr_display.html", qr_image=img_base64, url=host_url)

@app.route("/download")
def download_vn():
    # Serve the .vnt file
    return send_from_directory(
        directory="static",
        path="naal nachna by peaches._.ncream.vnt",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run()