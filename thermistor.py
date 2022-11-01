import numpy as np
import smbus
import time


i2c = smbus.SMBus(1)
addr = 0x68
config = 0b10011000
Vref = 2.048

i2c.write_byte(addr, config)  # 16bit
time.sleep(0.2)


def swap16(x):
    return (((x << 8) & 0xFF00) | ((x >> 8) & 0x00FF))


def sign16(x):
    return (-(x & 0b1000000000000000) | (x & 0b0111111111111111))


def cal_temp_103JT(res):
    return 247.9 * res ** (-0.1546) - 148.7


def cal_res_103JT(temp):
    return 7.66 * np.exp(-0.07066 * temp) + 20.21 * np.exp(-0.03303 * temp)


while True:

    data = i2c.read_word_data(addr, config)
    raw = swap16(int(hex(data), 16))
    raw_s = sign16(raw)

    voltage = round((Vref * raw_s / 32767), 4)
    current = (3.3-voltage)/9.84e3


    temp = cal_temp_103JT(voltage/current/1000)

    print(temp)

    time.sleep(1)