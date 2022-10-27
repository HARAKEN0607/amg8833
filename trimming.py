from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/img.png'

img = Image.open(image_path)

im_crop = img.crop((108, 58, 478, 428))
im_crop.save(folderpath + "/Trimming_image.png", quality=95)

