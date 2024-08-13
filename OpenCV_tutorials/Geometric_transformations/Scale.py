import numpy as np
import cv2 as cv

src = cv.imread('/home/pi/mse112-ws-student/OpenCV_tutorials/Geometric_transformations/sfu.png')
# method  output the dimension directly
height, width = src.shape[:2]  # acquire the original dimension

# increase size by 50%, interpolation cubic spline
res1 = cv.resize(src, (int(1.5*width), int(1.5*height)),interpolation=cv.INTER_CUBIC)

# decrease size by 50%, interpolation cubic spline
res2 = cv.resize(src, (int(0.5*width), int(0.5*height)),interpolation=cv.INTER_CUBIC)

# displat images
cv.imshow("src", src)
cv.imshow("res1", res1)
cv.imshow("res2", res2)
print("src.shape=", src.shape)
print("res1.shape=", res1.shape)
print("res2.shape=", res2.shape)

# close windows when any key is pressed
cv.waitKey()
cv.destroyAllWindows()
