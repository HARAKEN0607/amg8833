from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()

image_path = folderpath + '/img.png'

img = Image.open(image_path)

im_crop = img.crop((108, 47, 468, 422))
im_crop.save(folderpath + "/Trimming_image.png", quality=95)