import localization
import cv2

def main():

	sharpened_image = cv2.imread('plaque.jpg',0)
	localization.localization(sharpened_image)

main()