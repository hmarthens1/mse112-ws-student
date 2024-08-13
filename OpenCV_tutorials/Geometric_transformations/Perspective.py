import cv2
import numpy as np

img=cv2.imread('/home/pi/mse112-ws-student/OpenCV_tutorials/Geometric_transformations/sfu.png')
rows, cols = img.shape[:2]
print(rows,cols)

# four vertices pts1 of parallelogram in the original image
pts1 = np.float32([[150,50],[400,50],[60,450],[310,450]])
# four vertices pts2 of parallelogram in target image
pts2 = np.float32([[150-200,50],[400,50],[60,450],[310+200,450]])
# transformation matrix
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols,rows))

cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()
