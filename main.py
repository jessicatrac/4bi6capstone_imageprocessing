import localization
import cv2
import sharpening
import Color_Histogram
import Color_Thresholding
# import ambient_subtraction

def main():

    # Testing image with plaque
	image = cv2.imread('test2jess3cl2.jpg',1)
	mask = localization.localization(image)
	localized_image = cv2.bitwise_and(image,image,mask= mask)
	detect_value = Color_Thresholding.red_detection(localized_image)

	print(detect_value)

main()
