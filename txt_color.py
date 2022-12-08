from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/original_image.png'

img = Image.open(image_path)

d = ImageDraw.Draw(img)

# d.text((200, 200), '45', fill='white', outline='blue', spacing=10, align='right')
# d.rectangle((200, 100, 300, 200), fill='white', outline='blue')

text = "あいうえお"
font = ImageFont.truetype(font="C:/WINDOWS/Fonts/Corbel", size=70)
fill_color = (255, 0, 0)
stroke_color = (0, 0, 255)

d.text((50, 10), text, font=font, fill=fill_color, stroke_width=1, stroke_fill=stroke_color)
d.text((50, 80), text, font=font, fill=fill_color, stroke_width=3, stroke_fill=stroke_color)
d.text((50, 150), text, font=font, fill=fill_color, stroke_width=5, stroke_fill=stroke_color)
d.text((50, 220), text, font=font, fill=fill_color, stroke_width=7, stroke_fill=stroke_color)

img.save(folderpath + "/Processing_image.png")

print('finished')
