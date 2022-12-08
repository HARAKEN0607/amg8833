from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()
image_path = folderpath + '/original_image.png'
img = Image.open(image_path)
d = ImageDraw.Draw(img)

# 図形縁取り
d.rectangle((200, 100, 300, 200), fill='white', outline='blue')

# 文字列を描写
font_path = 'C:\Windows\Fonts\meiryo.ttc'           # Windowsのフォントファイルへのパス
font_size = 24                                      # フォントサイズ
fnt = ImageFont.truetype(font_path, font_size)     # PILでフォントを定義
d.text((100, 100), 'こんにちは', fill='blue', outline='white', font=fnt)

img.save(folderpath + "/Processing_image.png")

print('finished')


