import localization
import cv2
import sharpening

def main():
              
	raw_image = cv2.imread('plaque.jpg',0)
	sharpened_image = sharpening.sharpen(raw_image)
	localization.localization(sharpened_image)

main()
