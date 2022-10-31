from PIL import Image, ImageDraw
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
abn_temp = 40

if not os.path.exists(folderpath):
    os.mkdir(folderpath)


def get_original_data(abn_temp):
    # I2Cの初期化
    i2c = busio.I2C(board.SCL, board.SDA)
    # サーモセンサーの初期化
    sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)

    # 初期化のために待つ
    time.sleep(1)

    # datalist = 8x8の温度配列
    datalist = sensor.pixels

    # get max_temp min_temp
    temp_max_arrange = []
    temp_min_arrange = []

    for n in range(0, 8, 1):
        temp_arrange = datalist[n]
        temp_max_arrange.append(max(temp_arrange))
        temp_min_arrange.append(min(temp_arrange))

        for m in range(0, 8, 1):
            temp_max = max(temp_max_arrange)
            temp_min = min(temp_min_arrange)

    # imshowでsensor.pixelsの２次元配列データを表示させる
    plt.axis("off")
    plt.imshow(sensor.pixels, cmap="inferno", interpolation="bicubic", vmin=temp_min, vmax=temp_max)

    # set color bar
    plt.colorbar()

    # original_photo saving
    if temp_max > abn_temp:
        plt.savefig(folderpath + '/' + dt_now_name + '_original.png')

    return datalist


def trimming(left, upper, right, lower):  # trimming photo
    image_path = folderpath + '/original_image.png'
    img = Image.open(image_path)

    im_crop = img.crop((left, upper, right, lower))
    im_crop.save(folderpath + "/Trimming_image.png", quality=95)


def draw_txt(abn_temp):  # drawing circle and temp data
    if os.path.exists(folderpath + '/' + dt_now_name + '_original.png'):

        image_path = folderpath + '/' + dt_now_name + '_original.png'

        # reading original data
        img = Image.open(image_path)

        d = ImageDraw.Draw(img)

        x = []
        y = []
        temp_list = []

        # get temp original data
        for n in range(0, 8, 1):
            temp_arrange = list[n]

            for m in range(0, 8, 1):
                temp = temp_arrange[m]
                if temp > abn_temp:
                    x.append(m + 1)
                    y.append(n + 1)
                    temp_list.append(temp) # abnormal temp data

        # writing temp data
        for n in range(0, len(y), 1):
            x_point = 106 + 23 * (2 * x[n] - 1)
            y_point = 45 + 23 * (2 * y[n] - 1)

            d.text((x_point, y_point), str(temp_list[n]), fill='blue', spacing=10, align='right')

        # drawing circle
        for n in range(0, len(y), 1):
            x1_point = 106 + 46 * (x[n] - 1)
            y1_point = 45 + 46 * (y[n] - 1)
            x2_point = 106 + 46 * x[n]
            y2_point = 45 + 46 * y[n]

            d.ellipse((x1_point, y1_point, x2_point, y2_point), outline=(0, 0, 0))

        # saving processing photo
        img.save(folderpath + '/' + dt_now_name + "_Processing_image.png")

    else:
        print("異常温度検知なし")


list = get_original_data(abn_temp)

draw_txt(abn_temp)

print("finish")




