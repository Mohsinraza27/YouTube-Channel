import qrcode as qr

img = qr.make("https://www.youtube.com/channel/UCPecrhWaA9IauGHI8MqPb0Q")
img.save("Youtube_Channel.png")

