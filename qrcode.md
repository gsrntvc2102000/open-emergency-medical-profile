A simple Python script to generate QR codes for any website using the `qrcode` module. This script will take a **website URL** as input and generate a **QR code image**.  

### **Steps:**  
1. Install the required module:  
   ```bash
   pip install qrcode[pil]
   ```  
2. Run the script and enter your website URL.  
3. The script will generate a **QR code image** and save it as `qrcode.png`.  

---

### **QR Code Generator Script (`generate_qr.py`)**
```python
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
```

---

### **How to Use:**  
1. Save this script as `generate_qr.py`.  
2. Open a terminal or command prompt.  
3. Run:  
   ```bash
   python generate_qr.py
   ```  
4. Enter the website URL (e.g., `https://add_yourwebsite_link_here/`).  
5. The script will generate `qrcode.png` in the same directory.  

Let me know if you need improvements! 🚀