import cv2
import numpy
import time
import np
img02=cv2.imread('circles.png')
img3 = cv2.resize(img02,(250,250))
background03=cv2.imread('circles.png')
background3 = cv2.resize(background03,(250,250))
hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
lower_blue = np.array([100,150,0]) 
upper_blue = np.array([140,255, 255])
mask6 = cv2.inRange(hsv3, lower_blue, upper_blue) 
mask5 = mask6
mask5 = cv2.morphologyEx(mask5, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask5 = cv2.dilate(mask5, np.ones((3, 3), np.uint8), iterations = 1) 
mask6 = cv2.bitwise_not(mask5)
res5 = cv2.bitwise_and(background3, background3, mask = mask5)    
res6= cv2.bitwise_and(img3, img3, mask = mask6) 
cv2.imshow('res5',res5)
cv2.waitKey(0)
cv2.destroyAllWindows()
