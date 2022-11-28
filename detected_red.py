import cv2
import numpy
import time
import np

img00=cv2.imread('circles.png')
img1 = cv2.resize(img00,(250,250))
background01=cv2.imread('circles.png')
background1 = cv2.resize(background01,(250,250))
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
lower_red = np.array([170,10,110])
upper_red = np.array([180, 255, 255]) 
mask2 = cv2.inRange(hsv1, lower_red, upper_red) 
mask1 = mask2
mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
mask2 = cv2.bitwise_not(mask1)
res1 = cv2.bitwise_and(background1, background1, mask = mask1)    
res2 = cv2.bitwise_and(img1, img1, mask = mask2) 
cv2.imshow('res1',res1)
cv2.waitKey(0)
cv2.destroyAllWindows()
