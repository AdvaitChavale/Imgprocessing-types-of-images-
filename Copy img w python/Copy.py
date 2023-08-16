import cv2

img = cv2.imread("kunai.jfif")

cv2.imwrite("copy.jpg",img)

cv2.imshow("Oi",img)
cv2.waitKey()

cv2.destroyAllWindows()

                 
