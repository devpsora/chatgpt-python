import qrcode

QR = qrcode.make("https://www.naver.com/")
QR.save("imgs/naver.png")