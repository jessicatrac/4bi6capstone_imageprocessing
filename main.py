import localization
import cv2
import sharpening
import Color_Histogram
import Color_Thresholding

def main():
        
    # Testing image with plaque      
	raw_image = cv2.imread('test2jess3cl.jpg',1)
	#sharpened_image = sharpening.sharpen(raw_image)
	mask = localization.localization(raw_image)
	localized_image = cv2.bitwise_and(raw_image,raw_image,mask= mask)
	#Color_Histogram.fluorescence_hist(raw_image,thresholding_image)
	detect_value = Color_Thresholding.red_detection(localized_image)
	

main()
