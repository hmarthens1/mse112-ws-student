import cv2
import numpy as np

img = cv2.imread("pele.png")
# drawing a line
# cv2.line(img,(100,100),(100,200),(255,0,0),5)

# drawing a rectangle
# cv2.rectangle(img,(100,100),(200,200),(255,0,0),5)

# drawing a circle
# cv2.circle(img,(240,60),100,(255,0,0),5)

# drawing a polygon
# pts = np.array([[100,100],[400,100],[100,300],[400,300]],np.int32)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],0,(255,0,0),5)

# put text
cv2.putText(img,"Champions!!",(100,100),cv2.FONT_ITALIC,3,(0,255,0),5)

cv2.imshow("pele",img)
cv2.waitKey()
cv2.destroyAllWindows()