 # -*- coding: utf-8 -*-
import cv2
import numpy as np
import time

img_origin = cv2.imread('3315437f-8cd9-4741-acc7-19c550e92bde.jpg', 1)
img = cv2.bitwise_not(img_origin)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 150, 255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
img_contour = cv2.drawContours(img_origin, contours, -1, (0, 255, 0), 5)
cv2.imshow("img_edge",img_contour)
cv2.waitKey(10000)
cv2.destroyAllWindows()