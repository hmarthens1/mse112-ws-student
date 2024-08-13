import cv2
import numpy as np

img = cv2.imread("rat.png")

# # operations

# # 1 acquire and modify color at pixel
# px = img[100,100]
# blue_val = img[100,100,0]
# green_val = img[100,100,1]
# red_val = img[100,100,2]

# img[100,100] = [blue_val-50,green_val-50,red_val-50] # change brightness


# # 2 acquire the image property

# print("shape =",img.shape)
# print("size=",img.size)
# print("dtype=",img.dtype)


# # 3.1 Splitting and merging of image channel
# B,G,R = cv2.split(img)

# cv2.imshow("Blue",B)
# cv2.imshow("Green",G)
# cv2.imshow("Red",R)

# # # 3.2 merging of image channel
# img2 = cv2.merge((B,G,R))
# cv2.imshow("merge",img2)

# 4 Color conversion

img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("shv",img)

cv2.waitKey()
cv2.destroyAllWindows()
