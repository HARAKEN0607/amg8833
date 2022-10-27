from PIL import Image, ImageFont, ImageDraw
import os
import time
import busio
import board

import adafruit_amg88xx

folderpath = os.getcwd()


def get_temp_data():
    # I2Cの初期化
    i2c = busio.I2C(board.SCL, board.SDA)
    # サーモセンサーの初期化
    sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)

    # 初期化のために待つ
    time.sleep(1)

    # 8x8の温度配列
    print(sensor.pixels)

def trimming(left, upper, right, lower):  # trimming photo
    image_path = folderpath + '/img.png'
    img = Image.open(image_path)

    im_crop = img.crop((left, upper, right, lower))
    im_crop.save(folderpath + "/Trimming_image.png", quality=95)

trimming(108, 58, 478, 428)

get_temp_data()
