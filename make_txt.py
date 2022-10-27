from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/img.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

d.text((200, 200), 'Test Message\nExample', fill='blue', spacing=10, align='right')

# d.line([(0, 50), (200, 50), (0, 150), (200, 150)], fill='blue', width=2)

img.save(folderpath + "/Processing_image.png")





