from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/img.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

# d.text((200, 200), '異常温度検知', fill='blue')
d.point([(50, 50), (150, 150)], fill='blue')

img.save(folderpath + "/Processing_image.png")





