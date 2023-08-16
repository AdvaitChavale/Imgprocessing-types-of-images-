import cv2
import imutils

img=cv2.imread("copy.jpg")
resizeImg=imutils.resize(img,width=50)
cv2.imwrite("resize.jpg",resizeImg)
