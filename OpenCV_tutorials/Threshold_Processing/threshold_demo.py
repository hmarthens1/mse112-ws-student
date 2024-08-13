import cv2
img=cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
#the threshold is 127
#set maxval as 255. And the output image after processing is black-and-white image
cv2.imshow("BINARY", img2)
cv2.waitKey(0)    
cv2.destroyAllWindows()