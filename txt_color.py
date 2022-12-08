from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/original_image.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

# d.text((200, 200), '45', fill='white', outline='blue', spacing=10, align='right')
# d.rectangle((200, 100, 300, 200), fill='white', outline='blue')

draw = ImageDraw.Draw(img)

# フォント TakaoExMincho を指定
font = ImageFont.truetype('TakaoExMincho', 50)
draw.text((100, 100), 'こんにちは', fill=(255, 0, 0), font=font)

img.save(folderpath + "/Processing_image.png")

print('finished')
