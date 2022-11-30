#Shambhavi Sabharwal 200914
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
#Read Image
path = sys.argv[1]
img = cv2.imread(path)
#print(type(img))
#Get Image Parameters
height=img.shape[0]
width=img.shape[1]
#Initialise values for voting
Grass=0
Road=0
Building=0
diff1=0
diff2=0
#Iterate over image to vote
for i in range(0,height):
    for j in range(0,width):
        diff1=0
        diff2=0
        g=0
        b=0
        r=0
        diff1=abs(img[i][j][1]-img[i][j][2])
        diff2=abs(2*img[i][j][1]-img[i][j][0]-img[i][j][2])
        if (diff1>=0 and diff1<=80):
          g=g+1
        if (diff1>=0 and diff1<=6):
          b=b+1
        if (diff1>6 and diff1<=20):
          r=r+1
        if (diff2>=12 and diff2<=85):
          g=g+1
        if (diff2>=1 and diff2<=8):
          b=b+1
        if (diff2>=0 and diff2<=12):
          r=r+1
        if (g>r and g>b):
          Grass=Grass+1
        if (r>g and r>b): 
          Road=Road+1
        if (b>r and b>g):
          Building=Building+1
#building=1, grass=2 and road=3 
if (Building>Grass and Building>Road):
  print("1")
if (Road>Grass and Road>Building):
  print("3")
if (Grass>Building and Grass>Road):
  print ("2")



