import cv2
import numpy as np

img = cv2.imread('/home/pi/mse112-ws/OpenCV_tutorials/Geometric_transformations/sfu.png')
rows, cols, ch = img.shape
# rotate the image counterclockwise by 45 degrees, and zoom out the original image by factor 0.5
M = cv2.getRotationMatrix2D((cols/ 2.0,rows/2.0), 45,0.5)
# original picture  convert matrix  output the image center
dst = cv2.warpAffine(img, M, (cols, rows))

print("Matrix M: \n",M)
cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
