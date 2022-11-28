import cv2
import numpy
import time
import np
img03=cv2.imread('circles.png')
img4 = cv2.resize(img03,(250,250))
background04=cv2.imread('circles.png')
background4 = cv2.resize(background04,(250,250))
hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20,100,100]) 
upper_yellow = np.array([30,255, 255])
mask8= cv2.inRange(hsv4, lower_yellow, upper_yellow) 
mask7 = mask8
mask7 = cv2.morphologyEx(mask7, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask7 = cv2.dilate(mask7, np.ones((3, 3), np.uint8), iterations = 1) 
mask8 = cv2.bitwise_not(mask7)
res7 = cv2.bitwise_and(background4, background4, mask = mask7)    
res8= cv2.bitwise_and(img4, img4, mask = mask8) 
cv2.imshow('res7',res7)

cv2.waitKey(0)
cv2.destroyAllWindows()
