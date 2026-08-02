"""
Genererar QR-koderna som länkar till filmklippen (via GitHub Pages).
Kör om (python3 build_qr.py) om filmerna flyttas eller döps om.
"""

import qrcode

BASE = "https://willeeklund.github.io/shs26/workshops/spelforstaelse/Filmer/"

urls = {
    "roller": BASE + "de%204%20rollerna.mp4",
    "skugga": BASE + "passningsskugga.mp4",
    "hall": BASE + "h%C3%A5ll%20pucken%20inom%20laget.mp4",
    "givego": BASE + "bli%20spelbar%20-%20give%20and%20go.mp4",
}

for name, url in urls.items():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#111111", back_color="white")
    img.save(f"{name}.png")
    print(name, "->", url)
