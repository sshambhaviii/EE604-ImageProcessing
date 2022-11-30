import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

loc = sys.argv[1]
img = cv2.imread(loc)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.asarray(img)

temp = 0
for i in range(0, 201):
    for j in range(0, 190):
        temp = img[i][j][1]
        img[i][j][1] = img[i][j][2]
        img[i][j][2] = temp
        

img_copy = img.copy()


for i in range(0, 201):
    for j in range(0, 190):
        img_copy[i][j] = img[i+200][j]

for i in range(201, 411):
    for j in range(0, 190):
        img_copy[i][j] = img[i-200][j]


def flip_rows(img, x, y, l1, l2):
    temp = np.ones((l2, 3))
    for i in range(0, int(l1/2)+1):
        temp = img[x+i, y:y+l2, :].copy()
        img[x+i, y:y+l2, :] = img[x+l1-i-1, y:y+l2, :]
        img[x+l1-i-1, y:y+l2, :] = temp
    return img


def flip_cols(img, x, y, l1, l2):
    temp = np.ones((l1, 3))
    for j in range(0, int(l2/2)+1):
        temp = img[x:x+l1, y+j, :].copy()
        img[x:x+l1, y+j, :] = img[x:x+l1, y+l2-j-1, :]
        img[x:x+l1, y+l2-j-1, :] = temp

    return img


img_copy = flip_cols(img_copy, 150, 515, 180, 185)

img_copy = flip_rows(img_copy, 370, 370, 51, 427)
img_copy = flip_rows(img_copy, 0, 0, 201, 190)

for i in range(1, 6):
    img_copy[399+i, 0:190, :] = img_copy[400-i, 0:190, :]
for i in range(1, 6):
    img_copy[411-i, 0:190, :] = img_copy[410+i, 0:190, :]

image2 = Image.fromarray(img_copy)
image2.save('jigsolved.jpg')
