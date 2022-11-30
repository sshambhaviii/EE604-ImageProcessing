import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from PIL import Image
# For the purpose of displaying our numbers, a map table has been created. All 15 lights for a digit have been numbered from 0 to 14 and for every digit and light, the matrix shows 0 or 1
# 0--> Light not activated
# 1--> Light activated
act = np.ones((10, 15))
lst_y = [4, 7, 10, 0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 3, 4, 10, 11, 3, 4, 9, 10, 1, 4,
         9, 10, 12, 13, 4, 5, 9, 10, 4, 5, 10, 3, 4, 6, 7, 9, 10, 12, 13, 4, 10, 4, 9, 10]
lst_x = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4,
         4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 9]
for i in range(len(lst_x)):
    act[lst_x[i], lst_y[i]] = 0

#Code to show white circle at given centres
def circle(x, y, img):
    for i in range(x-25, x+26):
        for j in range(y-25, y+26):
            # print((i-x)*(i-x)+(j-y)*(j-y))
            if (((i-x)*(i-x)+(j-y)*(j-y)) <= 625):
                img[i][j] = 255

#Display Number
img = np.zeros([300, 500], dtype=np.uint8)
dig1 = np.empty([15, 2], dtype=int)
dig1[0][0] = 34
dig1[0][1] = 81
j = 0
gap = 58
for i in range(len(dig1)):
    dig1[i][0] = dig1[0][0]+j*gap
    if ((i+1) % 3 == 0):
        j = j+1
    dig1[i][1] = dig1[0][1]+(i % 3)*gap
dig2 = np.empty([15, 2], dtype=int)
for i in range(len(dig2)):
    dig2[i][1] = dig1[i][1]+222
    dig2[i][0] = dig1[i][0]

number = int(sys.argv[1])

num_1 = number/10
num_2 = number % 10

for i in range(act.shape[1]):
    if (act[int(num_1)][i] == 1):
        circle(dig1[i][0], dig1[i][1], img)

for i in range(act.shape[1]):
    if (act[int(num_2)][i] == 1):
        circle(dig2[i][0], dig2[i][1], img)


imag = Image.fromarray(img)
imag = imag.convert("L")
imag.save("dotmatrix.png")
