from time import time
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os


def save_file(user_input, user_input_formatted, program_path):
        qr = qrcode.QRCode(version=1, box_size=5, border=3)
        qr.add_data(user_input)

        qr.make(fit=True)
        img = qr.make_image(fill_color='white', back_color='black')
        print(user_input_formatted)
        img.save(program_path + user_input_formatted + '.png')

        
        print('💾 QR Code saved to path: ', program_path + user_input_formatted)
