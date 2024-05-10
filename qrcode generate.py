import qrcode


def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_Q,
        box_size=7,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg007.png")


url = input("Enter your Url: ")
generate_qrcode(url)