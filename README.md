# qr-studio
Simple CLI app for generating and decoding QR codes.

This command line tool steps you through creating or decoding a QR code. The application saves .png files in a dedicated directory for every qr code you create.

# Installation

Application uses a few libraries that can be installed using the requirements.txt. 
Simply navigate to the repo and run:

pip install -r requirements.txt

If you are on a Linux system, you may get a pyzbar error. In whitch case you install the shared libzbar0 library with:

sudo apt-get install libzbar0
