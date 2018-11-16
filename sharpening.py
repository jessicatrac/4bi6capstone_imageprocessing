import cv2
import numpy as np
from scipy.ndimage.filters import median_filter
import matplotlib as mp


def sharpen(raw_image):
    #image = cv2.imread(raw_image)
    rimage = cv2.resize(raw_image,(460,460))
    #cv2.imshow('Orginial', rimage)
    kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    sharpened = cv2.filter2D(rimage,-1,kernel_sharpening)
    #cv2.imshow('Sharpening Kernel', sharpened)
    return sharpened










#Median Filter to Remove Noise
#mimage=(rimage,1)

#Laplacian Filtering
#limage =cv2.Laplacian(mimage,cv2.CV_64F)
#sharpened2 = rimage - 0.7*limage
#cv2.imshow('Sharpening Laplace', sharpened)


#boxFilter = np.ones((3,3),np.float32)/81.0
#kernel_sharpening =kernel_sharpening - boxFilter
#cv2.imshow('Orginial', rimage)
#Resizing the Image
#Reading in Image so that it works with Median Filter






