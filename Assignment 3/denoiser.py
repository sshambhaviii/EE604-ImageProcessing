#Shambhavi 200914
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
#Read Image
loc = sys.argv[1]
img = cv2.imread(loc)
height = img.shape[0]
width = img.shape[1]
# print(height)
# print(width)
flag = 0
#ROI for larger image
Height = height
if (height > 650):
    flag = 1
    height = int(height/2.28)
else:
    height = int(height/1.4)

#Bilateral Filter
def bilat_fil(image, kernel, sigi, sigs):
    # image=np.asarray(image)
    image = image.astype(np.float32)
    result = np.zeros_like(image, dtype=np.float32)
    for channel in range(3):
        print(channel)
        for r in range(height):
            for c in range(width):
                W = np.zeros(3)
                pix_val = np.zeros(3)
                dist = int(kernel/2)
                for x in range(-dist, dist):
                    for y in range(-dist, dist):
                        dx = r+x
                        dy = c+y
                        if (dx < 0):
                            dx = 0
                        if (dx >= height):
                            dx = height-1
                        if (dy < 0):
                            dy = 0
                        if (dy >= width):
                            dy = width-1
                        gausss = (np.exp(-(x**2 + y**2)/(2*sigs**2))) / \
                            (2*np.pi*(sigs**2))
                        intdiff = abs(image[r][c][channel] -
                                      image[dx][dy][channel])
                        # print(type(intdiff))
                        gaussi = (np.exp(-(intdiff**2)/(2*sigi**2))) / \
                            (2*np.pi*(sigi**2))
                        w = gaussi*gausss
                        W[channel] = W[channel]+w
                        w = w*image[dx][dy][channel]
                        pix_val[channel] = pix_val[channel]+w
                pix_val[channel] = pix_val[channel]/W[channel]
                result[r][c][channel] = pix_val[channel]
            # print(result)
    # if (flag==1):
        for channel in range(3):
            for r in range(height, Height):
                for c in range(width):
                    result[r][c][channel] = image[r][c][channel]
    return result


filtered_result = cv2.bilateralFilter(img, 15, 90, 90)
cv2.imwrite("denoised.jpg", filtered_result)
