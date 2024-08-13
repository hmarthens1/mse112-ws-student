import cv2
import numpy as np
import sys

img = cv2.imread("/home/pi/mse112-ws-student/OpenCV_tutorials/Geometric_transformations/sfu.png")
rows, cols, ch = img.shape
mapx = np.ones(img.shape[:2], np.float32)
mapy = np.ones(img.shape[:2], np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)#set X-axis coordinate of each point mapped on the original picture 
        mapy.itemset((i,j),i)#set Y-axis coordinate of each point mapped on the original picture
result_img = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

cv2.imshow("img", img)
cv2.imshow("result_img", result_img)
cv2.waitKey()
cv2.destroyAllWindows()
