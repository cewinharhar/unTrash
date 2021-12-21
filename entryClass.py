from  typing import BinaryIO, List, Tuple, Dict
import qrcode
import hashlib

#hi

class entry:

    """
    The input class for each device. Following can be done:
        - initialize with imei nr
        - get information from scarping imei.info
        - Get device life history
            - first/second user
            - repairments
        - retrieve information from sustainability databank
            - calculate unTrash score
            - saved CO2
    """

    def __init__(self, imei: str):

        #input check
        if not isinstance(imei, str):
            return print("imei is no string")

        binImei         = imei.encode('UTF-8') #transfom string to binary for hashing
        self.hashImei   =  hashlib.sha256(binImei).hexdigest() #hash binary imei with sha256 algorithm


    #qr code generator
    def QRGenerator(self):
        """
        Generate the Qr code with the hashed imei binary
        """
        qr              = qrcode.QRCode()
        self.QRhash     = qr.add_data(self.hashImei) #imei
        self.QRImg      = qr.make_image().get_image()

    def QR(self):
        """
        Save / print QR code
        """
        self.QRImg.show()


### Test

mine = entry("84739560303030395969302")
mine.QRGenerator()
mine.QR()
