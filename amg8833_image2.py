import time
import busio
import board

import adafruit_amg88xx

import matplotlib.pyplot as plt

# I2Cバスの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)

# センサーの初期化
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)

# センサーの初期化待ち
time.sleep(.1)

# imshowでsensor.pixelsの２次元配列データを表示させる
fig = plt.imshow(sensor.pixels, cmap="inferno", interpolation="bicubic")
plt.colorbar()

plt.savefig("img.png")