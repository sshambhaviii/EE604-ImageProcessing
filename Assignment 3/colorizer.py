#Shambhavi Sabharwal
#Roll No 200914
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
#Read Image
path1 = sys.argv[1]
img1 = cv2.imread(path1,0)
path2 = sys.argv[2]
img2 = cv2.imread(path2,0)
path3 = sys.argv[3]
img3 = cv2.imread(path3,0)
#Create Arrays for computation
chan_1=np.asarray(img1)
#print(chan_1.shape)
height,width=chan_1.shape
chan_2=np.asarray(img2)
chan_3=np.asarray(img3)
#Initialising Empty Arrays for storage after upsampling
new_c2=np.zeros(chan_1.shape)
new_c3=np.zeros(chan_1.shape)
#Code with Loops to construct Image
i=0
j=0
print(height)
print(width)
for row in range(height):
    #i=row
    j=0
    for coloumn in range(width):
        new_c2[row][coloumn]=chan_2[int(row/4)][int(coloumn/4)]
        new_c3[row][coloumn]=chan_3[int(row/4)][int(coloumn/4)]
        if (coloumn%4==0):
            j=j+1
    if (row%4==0):
            i=i+1
     
#Combining Image channels
YCrCb=np.dstack((chan_1,new_c2,new_c3))
YCrCb = YCrCb.astype('uint8')
print(YCrCb.shape)
#Converting to RGB
final_image=cv2.cvtColor(YCrCb,39)
#Writing to file
cv2.imwrite("flyingelephant.jpg",final_image)
        

