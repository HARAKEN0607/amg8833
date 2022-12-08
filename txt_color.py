from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/original_image.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

d.text((200, 200), '45', fill='white', outline='blue', spacing=10, align='right')
d.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))

img.save(folderpath + "/Processing_image.png")

print('finished')
