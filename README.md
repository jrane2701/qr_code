# qr_code
# QR Code Generator 📱🔗

A simple Python project that generates a QR code for any website or text using the `qrcode` library. The generated QR code is saved as an image file. The script currently creates a QR code for a YouTube playlist link. 

---

## 📌 Features

* Generate QR codes from URLs or text.
* Customize QR code size and border.
* Save the generated QR code as an image.
* Lightweight and beginner-friendly project.

---

## 🛠️ Technologies Used

* Python 3
* `qrcode` library
* PIL (Pillow)

---

## 📂 Project Structure

```text
QR-Code-Generator/
│
├── qr.py          # Main Python script
├── yt_qr.png      # Generated QR code image
└── README.md
```

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/QR-Code-Generator.git
cd QR-Code-Generator
```

2. Install dependencies:

```bash
pip install qrcode[pil]
```

---

## ▶️ Usage

Run the script:

```bash
python qr.py
```

After execution, a file named:

```text
yt_qr.png
```

will be created in the project directory.

---

## 📝 Code Overview

```python
import qrcode

website_link = "YOUR_URL"

qr = qrcode.QRCode(version=1, box_size=5, border=2)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')
img.save('yt_qr.png')
```

---

## 📸 Example Output

The program generates a QR code image that can be scanned with any smartphone camera to open the corresponding link.

---

## 🔧 Customization

You can modify:

| Parameter    | Description                 |
| ------------ | --------------------------- |
| `version`    | Controls QR code complexity |
| `box_size`   | Size of each QR box         |
| `border`     | Thickness of border         |
| `fill_color` | QR code color               |
| `back_color` | Background color            |

Example:

```python
img = qr.make_image(
    fill_color='blue',
    back_color='yellow'
)
```

---

## 🎯 Future Improvements

* Accept user input for URLs.
* Generate QR codes for text, Wi-Fi credentials, or contact information.
* Add a graphical user interface (GUI).
* Allow color and style customization.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

⭐ If you found this project useful, consider giving the repository a star!
