# Qr-Generator
QR Code Generator - Setup & Execution Guide
-------------------------------------------

1. PREREQUISITES
   - Python 3.6+ installed (https://www.python.org/downloads/)
   - VS Code (or any Python IDE)

2. SETUP
   a. Open Terminal (VS Code: Ctrl+~)
   b. Navigate to project folder:
      cd "P:/1. Vaguppu/0. MDTE22 Vaguppu/QrCodeGenerator"
   c. Install dependencies:
      pip install qrcode[pil]

3. RUN THE SCRIPT
   a. Method 1: VS Code
      - Open Qr_Code_Generator.py
      - Click the ▶️ Run button (or press F5)
   b. Method 2: Terminal
      python Qr_Code_Generator.py

4. OUTPUT
   - QR code saved as test.png in the same folder.

5. CUSTOMIZE
   - Change the URL in `data` to generate different QR codes.
   - Adjust `version`, `box_size`, or `border` for sizing.

6. TROUBLESHOOTING
   - "Module not found": Run `pip install qrcode[pil]`
   - Path errors: Use forward slashes (/) in paths
   - Virtual Environment: Activate with `.venv/Scripts/activate` (Windows)
