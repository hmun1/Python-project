#Simple Qr Code generator

import qrcode
img = qrcode.make("Another Message!")
img.save("black_white.png")