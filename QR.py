import qrcode
from IPython import display

qr = qrcode.QRCode()
qr.add_data("359443095688916") #imei

img = qr.make_image().get_image().show()

display(img())

img.save(r"_GITHUB\unTrash\SamsungNote9Kevin.png")

img.get_image().show()