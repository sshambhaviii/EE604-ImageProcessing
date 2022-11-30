#Roll No - 200914
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
#Read Image
path = sys.argv[1]
image = cv2.imread(path)
num = path[-5]
if((path[-6]).isdigit()):
	num = path[-6] + num
#Gaussian Blur
kernelsize = 5
sigma = 0.9
height,width = image.shape[0:2]
gaussian_blur=np.zeros((kernelsize,kernelsize))
half_size= int(kernelsize / 2)
for x in range(-half_size,half_size+1):
	for y in range(-half_size,half_size+1):
		gaussian_blur[x+half_size,y+half_size]=np.exp(-(x**2 + y**2)/(2* sigma**2))/(2*np.pi*(sigma**2))
blurredimg=np.zeros_like(image)
for c in range(3):
	paddedimg=np.pad(image[:,:,c],pad_width=((half_size,half_size),(half_size,half_size)),constant_values=0)
	temp_image=np.zeros_like(paddedimg)
	for i in range(half_size, paddedimg.shape[0]-half_size):
		for j in range(half_size, paddedimg.shape[1]-half_size):
			x = paddedimg[i-half_size:i-half_size+kernelsize, j-half_size:j-half_size+kernelsize]
			x = x.flatten()*gaussian_blur.flatten()
			temp_image[i][j] = x.sum()  	
	blurredimg[:,:,c]=temp_image[half_size:-half_size, half_size:-half_size]
gray = cv2.cvtColor(blurredimg, cv2.COLOR_BGR2GRAY)
#Canny Edge Detection
edges = cv2.Canny(gray, 50, 200)
#Hough Transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=250)
for line in lines:
  x1, y1, x2, y2 = line[0]
  cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)

#Write Image
cv2.imwrite("robolin-tiles" + num +".jpg",image)