def red_detection (img):
    import numpy
    import cv2
    import sys
    from matplotlib import pyplot as plt

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, (320,50,50), (360,255,255))
    mask2 = cv2.inRange(hsv, (0,50,50), (28,255,255))
    mask = cv2.bitwise_or(mask1, mask2)
    res = cv2.bitwise_and(img,img,mask= mask)

    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.imshow('Original Image', img)
    cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
    cv2.imshow('Mask', mask)
    cv2.namedWindow("Red", cv2.WINDOW_NORMAL)
    cv2.imshow('Red', res)

    nzCount = cv2.countNonZero(mask)
    #print nzCount
    bin_detect="false"
    if nzCount > 10000:
        bin_detect="true" #output true if plaque is detected

    cv2.waitKey()
    cv2.destroyAllWindows()

    return bin_detect
