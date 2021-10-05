#!/usr/bin/python
import rospy
import cv2
import random
img = cv2.imread('photos/allCaps.jpeg', cv2.IMREAD_COLOR)

img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
#img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
print(img.shape)
tag = img[50:250, 30:230]
img[100:300, 70:270] = tag
#cv2.imwrite('new_allcaps.jpg', img)
cv2.imshow('ALLCAPS',img)
cv2.waitKey(0)
cv2.destroyAllWindows()