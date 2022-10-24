import time
import busio
import board

import adafruit_amg88xx

# I2Cの初期化
i2c = busio.I2C(board.SCL, board.SDA)
# サーモセンサーの初期化
sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)

# 初期化のために待つ
time.sleep(0.2)

# 8x8の温度配列
print(sensor.pixels)