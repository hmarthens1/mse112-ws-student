import cv2
img=cv2.imread('test2.jpg')
img = cv2.GaussianBlur(img, (5, 5), 0) #gaussian blur
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img3 = cv2.drawContours(img, contours, -1, (0,255,255), 3)
cv2.imshow("BINARY", img3)
cv2.waitKey(0)    
cv2.destroyAllWindows()