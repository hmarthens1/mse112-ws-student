import cv2
import numpy as np
import matplotlib.pyplot as plt

# image reading
img = cv2.imread('noise.jpg')

# image smoothing
blur1 = cv2.blur(img, (5, 5))   # mean filtering
blur2 = cv2.GaussianBlur(img, (5, 5), 1)    # Gauss filtering
blur3 = cv2.medianBlur(img, 5)  # Median filtering

# image display
plt.figure(figsize=(10, 5), dpi=100)
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(141), plt.imshow(img), plt.title("Original")
plt.xticks([]), plt.yticks([]) #remove xgrid and ygrid
plt.subplot(142), plt.imshow(blur1), plt.title("Mean Filtering")
plt.xticks([]), plt.yticks([]) #remove xgrid and ygrid
plt.subplot(143), plt.imshow(blur2), plt.title("Gauss Filtering")
plt.xticks([]), plt.yticks([]) #remove xgrid and ygrid
plt.subplot(144), plt.imshow(blur3), plt.title("Median Filtering")
plt.xticks([]), plt.yticks([])
plt.show()