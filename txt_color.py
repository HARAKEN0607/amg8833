from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/original_image.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

d.text((200, 200), '45', fill='white', outline='blue', spacing=10, align='right')

img.save(folderpath + "/Processing_image.png")

print('finished')
