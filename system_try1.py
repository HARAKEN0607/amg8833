from PIL import Image, ImageFont, ImageDraw
import os
import matplotlib.pyplot as plt

folderpath = os.getcwd()

image_path = folderpath + '/img.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

d.text((10, 10), '異常温度検知', fill='red')

img.save("Processing_image.png")





