from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/img.png'

image = Image.open(image_path)

width = img.width
height = img.height

print("画像の高さは ",height)
print("画像の幅は ",width)





