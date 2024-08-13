import numpy as np
import cv2

src = cv2.imread('/home/pi/mse112-ws-student/OpenCV_tutorials/Geometric_transformations/sfu.png')
rows, cols, ch = src.shape

# Matrix with translation in x; x - 300; and translation in y; y + 50
M = np.float32([[1, 0, -300], [0, 1, 50]])

dst = cv2.warpAffine(src, M, (cols, rows))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
