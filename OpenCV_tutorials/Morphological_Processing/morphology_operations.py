import cv2
import numpy as np
# import matplotlib.pyplot as plt   # not used - display uses cv2 below

# read the image
img_org = cv2.imread('example_org.jpg')
img_noise = cv2.imread('example_noise.jpg')
img_cave = cv2.imread('example_cave.jpg')

# build nuclear structure
kernel = np.ones((10, 10), np.uint8)  # 10*10 all-one matrix

# Morphological processing
erosion_img = cv2.erode(img_org, kernel)  # erosion
dilate_img = cv2.dilate(img_org, kernel)  # dilation
open_img = cv2.morphologyEx(img_noise, cv2.MORPH_OPEN, kernel)  # open operation
close_img = cv2.morphologyEx(img_cave, cv2.MORPH_CLOSE, kernel)  # close operation
top_hat_img = cv2.morphologyEx(img_noise, cv2.MORPH_TOPHAT, kernel)  # top hat operation
black_hat_img = cv2.morphologyEx(img_cave, cv2.MORPH_BLACKHAT, kernel)  # bottom hat operation

# image display
# Each row shares a source image, so the three results can be stacked side by
# side. Rows come from different source images and may differ in size, so they
# are shown as three separate windows rather than one 3x3 grid.
row1 = np.hstack((img_org,   erosion_img, dilate_img))
row2 = np.hstack((img_noise, open_img,    top_hat_img))
row3 = np.hstack((img_cave,  close_img,   black_hat_img))

cv2.imshow("Original | Erosion | Dilation", row1)
cv2.imshow("Original2 | Open | TopHat", row2)
cv2.imshow("Original3 | Close | BlackHat", row3)

cv2.waitKey(0)            # press any key (with a window focused) to close
cv2.destroyAllWindows()
