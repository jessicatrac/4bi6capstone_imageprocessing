def ambient_subtraction(img1, img2):
    import numpy
    import cv2
    import sys
    from matplotlib import pyplot as plt

    img3 = cv2.subtract(img1,img2)
    cv2.namedWindow("Subtracted Image", cv2.WINDOW_NORMAL)
    cv2.imshow('Subtracted Image', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return img3
