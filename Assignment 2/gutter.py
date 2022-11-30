#Roll No- 200914
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys

#Read Image
path = sys.argv[1]
image = cv2.imread(path)

#Shadow correction by removal of blurred image (Gaussian Blur)

kernelsize = 49
sigma = 8
height,width = image.shape[0:2]
channels=image.shape[2]
#Gaussian Blur
gaussian_blur=np.zeros((kernelsize,kernelsize))
half_size= int(kernelsize / 2)
for x in range(-half_size,half_size+1):
	for y in range(-half_size,half_size+1):
		gaussian_blur[x+half_size,y+half_size]=np.exp(-(x**2 + y**2)/(2* sigma**2))/(2*np.pi*(sigma**2))
blurredimg=np.zeros_like(image)
for c in range(channels):
	paddedimg=np.pad(image[:,:,c],pad_width=((half_size,half_size),(half_size,half_size)),constant_values=0)	#Padding Image for Gauss filter 
	temp_image=np.zeros_like(paddedimg)
	for i in range(half_size, paddedimg.shape[0]-half_size):						#Convoluting Gauss Filter
		for j in range(half_size, paddedimg.shape[1]-half_size):
			x = paddedimg[i-half_size:i-half_size+kernelsize, j-half_size:j-half_size+kernelsize]
			x = x.flatten()*gaussian_blur.flatten()
			temp_image[i][j] = x.sum()  	
	blurredimg[:,:,c]=temp_image[half_size:-half_size, half_size:-half_size]   

cleanedimage = np.zeros_like(blurredimg.shape, dtype=np.uint8) #Removing Blurred Image to get Cleaned Image
cleanedimage = image / blurredimg * 255
#Write Image
cv2.imwrite("cleaned-gutter.jpg",cleanedimage)