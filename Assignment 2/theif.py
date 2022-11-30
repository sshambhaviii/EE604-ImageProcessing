#Roll No-200914
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys

#Read Image
path = sys.argv[1]
image = cv2.imread(path)

#convert image to grayscale for processing
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_img=np.asarray(gray_img)

#Histogram Equalization to Enhance Image

flatten_array=gray_img.flatten()
histogram=np.zeros(256)
#Calculate Histogram Values
for i in flatten_array:
    histogram[i]+=1
#Normalise Histogram
sum=np.sum(histogram)
normalised_histogram=histogram/sum
#Cumulative Histogram
cumulative=np.cumsum(histogram)
#Apply to Image
newimage=cumulative[flatten_array]
newimage=np.reshape(newimage, gray_img.shape)
#Rescaling values from 0 to 255
max=newimage.max()
newimage=newimage/max*255

#Write Image
num = path[-5]
cv2.imwrite("enhanced-cctv"+num+".jpg",newimage)
