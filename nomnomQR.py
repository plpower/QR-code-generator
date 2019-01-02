# Python script to create qrcode

import qrcode

qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 20,
    border = 2,
)

# THE INPUT TO qr.add_data IS WHAT WILL SIT INSIDE THE QR CODE
# CHANGING THE URL BELOW WILL ALTER WHERE THIS QR CODE TAKES YOU
qr.add_data("https://eatvietnomnom.com/")
qr.make(fit = True)
img = qr.make_image(fill_color="green", back_color= "white")
img.show()