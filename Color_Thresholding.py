def red_detection (img,teeth_mask):
    import numpy
    import cv2
    import sys
    from matplotlib import pyplot as plt

    nzCount_teeth = cv2.countNonZero(teeth_mask)
    print(nzCount_teeth)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, (320,50,20), (360,255,255)) # 320 is "red magenta" on colour wheel
    mask2 = cv2.inRange(hsv, (0,50,20), (39,255,255)) # 45 is "warm yellow" on colour wheel
    mask = cv2.bitwise_or(mask1, mask2)
    res = cv2.bitwise_and(img,img,mask= mask)

    # cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    # cv2.imshow('Original Image', img)
    # cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
    # cv2.imshow('Mask', mask)
    # cv2.namedWindow("Red", cv2.WINDOW_NORMAL)
    # cv2.imshow('Red', res)

	# examples for poster
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
    plt.imshow(mask,cmap = 'gray')
    plt.xticks([]), plt.yticks([])
    plt.show()
    plt.imshow(res)
    plt.xticks([]), plt.yticks([])
    plt.show()

    nzCount_plaque = cv2.countNonZero(mask)
    print(nzCount_plaque)
    percentage = (float(nzCount_plaque)/float(nzCount_teeth))*100
    print(percentage)

    bin_detect="false"
    if nzCount_plaque > 1000:
        bin_detect="true" #output true if plaque is detected

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return bin_detect
