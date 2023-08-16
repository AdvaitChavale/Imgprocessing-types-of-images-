import cv2
img=cv2.imread("copy.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayImage.png",grayImg)
cv2.imshow("Orig",img)
cv2.imshow("Gray",grayImg)
cv2.waitKey()
cv2.destroyAllWindows()
