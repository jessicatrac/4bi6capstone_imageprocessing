'''
Determine different regions in extracted image. 
Jessica Trac.
November 2018.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
import random as rng

def localization(sharpened_image):

	# # Load image
	# img_raw = cv2.imread('plaquefinder.png',0)
	# img_raw = cv2.imread('anotha_tooth.jpg',0)
	# img_raw = cv2.imread('circle.png',0)
	# img_raw = cv2.imread('oneteethjessfilr33.jpg',0)

	# print('gums:',img_raw[80,150]) # gums
	# print('top teeth:',img_raw[102,171]) # teeth
	# print('bottom teeth:',img_raw[290,254]) # teeth
	# print('space:',img_raw[312,312]) # teeth

	## Threshold image - this primes the image for edge detection
	img_raw = cv2.cvtColor(sharpened_image,cv2.COLOR_BGR2GRAY)
	img_raw = cv2.GaussianBlur(img_raw,(5,5),11) # Add Gaussian blur 
	img_raw = cv2.equalizeHist(img_raw) # Equalize histogram = improve contrast

	img_invert = cv2.bitwise_not(img_raw) # Invert image
	img_blur = cv2.GaussianBlur(img_invert,(5,5),0) # Add Gaussian blur 
	otsu_threshold, img_threshold = cv2.threshold(img_blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) # Otsu's Thresholding (determines a suitable threshold)
	ret,img_threshold = cv2.threshold(img_raw,otsu_threshold*1.3,255,cv2.THRESH_BINARY)

	## Edge Detection using Canny Algorithm

	max_threshold = otsu_threshold*0.9
	min_threshold = otsu_threshold*0.2 # lower threshold is half of otsu's adaptive threshold

	# print('max thresh:',max_threshold)
	# print('otsu:',otsu_threshold)
	# print('min thresh:',min_threshold)

	edges_raw = cv2.Canny(img_raw,min_threshold,max_threshold) # Need to automate the threshold finding for edge detection
	# edges_raw = cv2.Laplacian(img_raw,cv2.CV_64F)
	edges_threshold = cv2.Canny(img_threshold,min_threshold,max_threshold)

	kernel = np.ones((5,5),np.uint8)
	edges_dilated = cv2.dilate(edges_threshold,kernel,iterations = 1) # Dilate edges (accounting for tiny edges; 'noise')
	edges_blur = cv2.GaussianBlur(edges_dilated,(5,5),0) # Add Gaussian blur 


	## Plotting images vs. detected edges
	plt.subplot(211),plt.imshow(img_raw,cmap = 'gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(212),plt.imshow(img_threshold,cmap = 'gray')
	plt.title('Threshold Image / Mask'), plt.xticks([]), plt.yticks([])

	# plt.subplot(223),plt.imshow(edges_raw,cmap = 'gray')
	# plt.title('Original Edge Image'), plt.xticks([]), plt.yticks([])
	# plt.subplot(224),plt.imshow(edges_blur,cmap = 'gray')
	# plt.title('Equalized Edge Image'), plt.xticks([]), plt.yticks([])

	# '''contours is a Python list of all the contours in the image. 
	# Each individual contour is a Numpy array of (x,y) coordinates of boundary points 
	# of the object.'''

	# ## Contour Detection from Edges
	# _, contours, hierarchy = cv2.findContours(edges_blur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	# contours_drawing = np.zeros((edges_blur.shape[0], edges_blur.shape[1], 3), dtype=np.uint8)

	# for i in range(len(contours)):
	#   color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
	#   cv2.drawContours(contours_drawing, contours, i, color, -1, cv2.LINE_8, hierarchy, 0)

	# contours_drawing = cv2.resize(contours_drawing, (300, 300)) # Plot contour drawing in smaller window
	# cv2.imshow("output", contours_drawing)  
	plt.show()

	return img_threshold
