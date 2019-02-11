import localization
import cv2
import sharpening
import Color_Histogram
import Color_Thresholding
import ambient_subtraction

def main():

    # Testing image with plaque
	raw_image1 = cv2.imread('al_test4_back_LED.jpg',1)
	raw_image2 = cv2.imread('al_test4_back_noLED.jpg',1)
	ambient_filtered = ambient_subtraction.ambient_subtraction(raw_image1,raw_image2)
	#sharpened_image = sharpening.sharpen(raw_image)
	mask = localization.localization(ambient_filtered)
	localized_image = cv2.bitwise_and(ambient_filtered,ambient_filtered,mask= mask)
	#Color_Histogram.fluorescence_hist(raw_image,thresholding_image)
	detect_value = Color_Thresholding.red_detection(ambient_filtered)

	print(detect_value)

main()
