import os
import time
import busio
import board
import matplotlib.pyplot as plt
import datetime

import adafruit_amg88xx

dt_now = datetime.datetime.now()
dt_now_name = dt_now.strftime('%Y%m%d%H%M%S')
folderpath = os.getcwd() + '/' + dt_now_name

if not os.path.exists(folderpath):
    os.mkdir(folderpath)


# I2Cの初期化
i2c = busio.I2C(board.SCL, board.SDA)
# サーモセンサーの初期化
sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)

# 初期化のために待つ
time.sleep(1)

# imshowでsensor.pixelsの２次元配列データを表示させる
plt.axis("off")
plt.imshow(sensor.pixels, cmap="inferno", interpolation="bicubic")

# set color bar
plt.colorbar()

plt.savefig(folderpath + '/' + dt_now_name + '_original.png')