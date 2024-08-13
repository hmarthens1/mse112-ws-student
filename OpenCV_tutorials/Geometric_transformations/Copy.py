import cv2
import numpy as np

img = cv2.imread('/home/pi/mse112-ws-student/OpenCV_tutorials/Geometric_transformations/sfu.png')
rows, cols, ch = img.shape

# mapx and mapy separately set the x and y axis coorinate
# Map all the pixels on the target image to the pixels on 100th row, 200th column of the original image.
mapx = np.ones(img.shape[:2], np.float32) * 200
mapy = np.ones(img.shape[:2], np.float32) * 100
result_img = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

cv2.imshow("img", img)
cv2.imshow("result_img", result_img)
cv2.waitKey()
cv2.destroyAllWindows()
