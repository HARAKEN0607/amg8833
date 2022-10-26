from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/img.png'
# font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc';
# font_size = 30  # 文字の大きさ
# text = '異常検知'
# color = (255, 255, 255)  # 文字の色

image = Image.open(image_path)
# font = ImageFont.truetype(font_path, font_size)  # フォントの指定
# draw = ImageDraw.Draw(image)
# draw.text((110, 20), text, font=font, fill=color)
# image.save(image_path)





