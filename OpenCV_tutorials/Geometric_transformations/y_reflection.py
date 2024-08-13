import cv2
import numpy as np

img = cv2.imread("/home/pi/mse112-ws-student/OpenCV_tutorials/Geometric_transformations/sfu.png")
rows, cols, ch = img.shape
mapx = np.ones(img.shape[:2], np.float32)
mapy = np.ones(img.shape[:2], np.float32)

# mapx and mapy separately set the x axis and y axis coordinate. map2
# remains unchanged, and map1 = “total number of cols - 1 - current col # number”
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)#just modify this line of code. 
        mapy.itemset((i,j),i)#
result_img = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
cv2.imshow("img", img)
cv2.imshow("result_img", result_img)
cv2.waitKey()
cv2.destroyAllWindows()