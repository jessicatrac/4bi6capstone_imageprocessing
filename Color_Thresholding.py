def red_detection (img,teeth_mask):
    import numpy
    import cv2
    import sys
    from matplotlib import pyplot as plt

    nzCount_teeth = cv2.countNonZero(teeth_mask)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, (320,50,20), (360,255,255)) # 320 is "red magenta" on colour wheel
    mask2 = cv2.inRange(hsv, (0,50,20), (39,255,255)) # validated 39 - "warm yellow" on colour wheel
    mask = cv2.bitwise_or(mask1, mask2)
    res = cv2.bitwise_and(img,img,mask= mask)

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

    percentage = (float(nzCount_plaque)/float(nzCount_teeth))*100


    bin_detect="false"
    if nzCount_plaque > 1000:
        bin_detect="true" #output true if plaque is detected

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    percentage = round(percentage,2)

    return bin_detect, percentage;

def blue_detection (img,teeth_mask):
    import numpy
    import cv2
    import sys
    from matplotlib import pyplot as plt

    nzCount_teeth = cv2.countNonZero(teeth_mask)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (80,85,85), (102,255,255)) # validated 39 - "cyan" on colour wheel
   
    res = cv2.bitwise_and(img,img,mask= mask)

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

    percentage = (float(nzCount_plaque)/float(nzCount_teeth))*100


    bin_detect="false"
    if nzCount_plaque > 1000:
        bin_detect="true" #output true if plaque is detected

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    percentage = round(percentage,2)

    return bin_detect, percentage;
