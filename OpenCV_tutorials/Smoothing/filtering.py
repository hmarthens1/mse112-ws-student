import cv2
import numpy as np
# import matplotlib.pyplot as plt   # not used - display uses cv2 below

# image reading
img = cv2.imread('noise.jpg')

# image smoothing
blur1 = cv2.blur(img, (5, 5))   # mean filtering
blur2 = cv2.GaussianBlur(img, (5, 5), 1)    # Gauss filtering
blur3 = cv2.medianBlur(img, 5)  # Median filtering

# image display
# All four are the same size, so stack them side by side in one window:
# Original | Mean | Gauss | Median
comparison = np.hstack((img, blur1, blur2, blur3))
cv2.imshow("Original | Mean | Gauss | Median", comparison)

cv2.waitKey(0)            # press any key (with a window focused) to close
cv2.destroyAllWindows()