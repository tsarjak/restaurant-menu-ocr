import cv2
import numpy as np
from cv2 import boundingRect, countNonZero, cvtColor, drawContours, findContours, getStructuringElement, imread, morphologyEx, pyrDown, rectangle, threshold
from PIL import Image

hist = []
large = imread("84.jpg")
# downsample and use it for processing
rgb = large

# apply grayscale
small = cvtColor(rgb, cv2.COLOR_BGR2GRAY)

# binarize
_, bw = threshold(src=small, thresh=0, maxval=255, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)


#Inverting the image
bw = 255 - bw

#Making the image from array so as to process it using PIL
im = Image.fromarray(bw)


#Loading the imag
photo=im.load()

x= im.size[0]
y=im.size[1]

print(x,y)

#Preparing histogram
for i in range(0,x):
    count=0
    for j in range(0,y):
        if(photo[i,j] == 255):
            count+=1
    hist.append(count)

print(hist)

count = 0
length = 0
for idx, val in enumerate(hist):
    if val != 0 and hist[idx-1] < 2:
        count+=1
    elif val != 0:
        length+=1


avg = length/count
print(avg)

length=0
for idx, val in enumerate(hist):
    if val>1 and hist[idx-1] > 1:
        length+=1
    elif val==0:
        hist[idx] = 50
        length=0
    elif val<2 and length > avg-1:
        hist[idx] = 50
        length=0

print(hist)
#Image.fromarray(bw).show()