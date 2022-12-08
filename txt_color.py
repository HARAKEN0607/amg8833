from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/original_image.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

d.text((50, 50), '45', fill='blue', outline='white', spacing=10, align='right')

img.save(folderpath + "/Processing_image.png")