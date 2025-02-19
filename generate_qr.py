import qrcode

# Function to generate QR code
def generate_qr_code(url, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  # Size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of each box
        border=4  # Border size
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    
    print(f"✅ QR code generated and saved as {filename}")

# Ask user for the website URL
if __name__ == "__main__":
    website_url = input("Enter the website URL: ").strip()
    generate_qr_code(website_url)
