import localization
import cv2
import sharpening
import Color_Histogram

def main():
        
    # Testing image with plaque      
	raw_image = cv2.imread('plaque.jpg',1)
	sharpened_image = sharpening.sharpen(raw_image)
	thresholding_image = localization.localization(sharpened_image)
	Color_Histogram.fluorescence_hist(sharpened_image, thresholding_image)

	# # Testing image with no plaque
	# raw_image = cv2.imread('no_plaque.jpg',1) 
	# sharpened_image = sharpening.sharpen(raw_image)
	# thresholding_image = localization.localization(sharpened_image)
	# Color_Histogram.fluorescence_hist(sharpened_image)

main()
