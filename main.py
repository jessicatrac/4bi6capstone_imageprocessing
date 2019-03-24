import localization
import cv2
import sharpening
import Color_Histogram
import Color_Thresholding
# import ambient_subtraction

def main():

    # Testing image with plaque
	image = cv2.imread('AKOF1.jpg',1)
	mask = localization.localization(image)
	localized_image = cv2.bitwise_and(image,image,mask= mask)
	detect_value, percentage = Color_Thresholding.red_detection(localized_image,mask)
	print(detect_value)
	print(percentage)

main()
