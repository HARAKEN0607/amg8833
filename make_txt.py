from PIL import Image, ImageFont, ImageDraw
import os

folderpath = os.getcwd()
image_path = folderpath + '/data.png'
img = Image.open(image_path)
d = ImageDraw.Draw(img)

font = ImageFont.truetype('arial.ttf', 26)

x = []
y = []

list = []
list_matrix = []

for n in range(0, 8, 1):
    list.append(40)

for n in range(0, 8, 1):
    list_matrix.append(list)

# print(list_matrix)

for n in range(0, 8, 1):
    temp_arrange = list_matrix[n]

    for m in range(0, 8, 1):
        temp = temp_arrange[m]
        if temp > 24:
            x.append(m+1)
            y.append(n+1)

# print(x)
#
# print(y)

for n in range(0, len(y), 1):
    x_point = 95+23*(2*x[n]-1)
    y_point = 45+23*(2*y[n]-1)
    # print(x_point)
    # print(y_point)
    d.text((x_point, y_point), '45', fill='blue', spacing=10, align='right', font=font)

for n in range(0, len(y), 1):
    x1_point = 108+46*(x[n]-1)
    y1_point = 58+46*(y[n]-1)
    x2_point = 108+46*x[n]
    y2_point = 58+46*y[n]

    # d.ellipse((x1_point, y1_point, x2_point, y2_point), outline='white')
    d.rectangle((x1_point, y1_point, x2_point, y2_point), outline='white')

img.save(folderpath + "/Processing_data.png")





