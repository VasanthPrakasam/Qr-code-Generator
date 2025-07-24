import qrcode

qr = qrcode.QRCode(
    version=5,  # Reduced from 15 to a more reasonable version
    box_size=10,  # size of the box where QR code will be displayed
    border=5  # white border around the QR code
)

data = "https://www.youtube.com/feed/playlists"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')  # Fixed back_color parameter
img.save('test.png')