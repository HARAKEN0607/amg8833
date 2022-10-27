from PIL import Image, ImageFont, ImageDraw
import os
import time
import busio
import board
import matplotlib.pyplot as plt

import adafruit_amg88xx

folderpath = os.getcwd()


def get_original_data():
    # I2Cの初期化
    i2c = busio.I2C(board.SCL, board.SDA)
    # サーモセンサーの初期化
    sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)

    # 初期化のために待つ
    time.sleep(1)

    # 8x8の温度配列
    print(sensor.pixels)

    # imshowでsensor.pixelsの２次元配列データを表示させる
    plt.imshow(sensor.pixels, cmap="inferno", interpolation="bicubic")
    plt.colorbar()

    plt.savefig("original_image.png")


def trimming(left, upper, right, lower):  # trimming photo
    image_path = folderpath + '/original_image.png'
    img = Image.open(image_path)

    im_crop = img.crop((left, upper, right, lower))
    im_crop.save(folderpath + "/Trimming_image.png", quality=95)


get_original_data()

trimming(108, 58, 478, 428)
