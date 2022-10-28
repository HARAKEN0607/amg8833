from PIL import Image, ImageDraw
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
    datalist = sensor.pixels

    # imshowでsensor.pixelsの２次元配列データを表示させる
    plt.axis("off")
    plt.imshow(sensor.pixels, cmap="inferno", interpolation="bicubic")
    plt.colorbar()

    # original_photo saving
    plt.savefig("original_image.png")

    return datalist


def trimming(left, upper, right, lower):  # trimming photo
    image_path = folderpath + '/original_image.png'
    img = Image.open(image_path)

    im_crop = img.crop((left, upper, right, lower))
    im_crop.save(folderpath + "/Trimming_image.png", quality=95)


def draw_txt():
    image_path = folderpath + '/original_image.png'

    img = Image.open(image_path)

    d = ImageDraw.Draw(img)

    x = []
    y = []

    for n in range(0, 8, 1):
        temp_arrange = list[n]

        for m in range(0, 8, 1):
            temp = temp_arrange[m]
            if temp > 24:
                x.append(m + 1)
                y.append(n + 1)

    for n in range(0, len(y), 1):
        x_point = 106 + 23 * (2 * x[n] - 1)
        y_point = 45 + 23 * (2 * y[n] - 1)
        print(x_point)
        print(y_point)
        d.text((x_point, y_point), '45', fill='blue', spacing=10, align='right')

    for n in range(0, len(y), 1):
        x1_point = 106 + 46 * (x[n] - 1)
        y1_point = 45 + 46 * (y[n] - 1)
        x2_point = 106 + 46 * x[n]
        y2_point = 45 + 46 * y[n]

        d.ellipse((x1_point, y1_point, x2_point, y2_point), outline=(0, 0, 0))

    img.save(folderpath + "/Processing_image.png")

list = get_original_data()

draw_txt()




