import cv2
import numpy as np
# import matplotlib.pyplot as plt   # not used - display uses cv2 below

# read the image
img = cv2.imread('luna.jpg')

# Canny edge detection
lowThreshold = 1
max_lowThreshold = 80
canny = cv2.Canny(img, lowThreshold, max_lowThreshold)

# image display
cv2.imshow("Original", img)
cv2.imshow("Edge Detection", canny)

cv2.waitKey(0)            # press any key (with a window focused) to close
cv2.destroyAllWindows()