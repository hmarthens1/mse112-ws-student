import cv2
import numpy as np

img = cv2.imread("/home/pi/mse112-ws/OpenCV_tutorials/Geometric_transformations/sfu.png")
rows, cols, ch = img.shape
mapx = np.ones(img.shape[:2], np.float32)
mapy = np.ones(img.shape[:2], np.float32)


# mapx and mapy separately set the x axis and y axis coordinate. map1
# remains unchanged, and map2 = “total number of row - 1 - current row # number”
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)#just modify this line of code. Symmetrical

result_img = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
cv2.imshow("img", img)
cv2.imshow("result_img", result_img)
cv2.waitKey()
cv2.destroyAllWindows()
