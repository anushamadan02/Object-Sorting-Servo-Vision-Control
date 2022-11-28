import cv2
import numpy
import time
import np
img00=cv2.imread('circles.png')
img1 = cv2.resize(img00,(250,250))
background01=cv2.imread('circles.png')
background1 = cv2.resize(background01,(250,250))
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
lower_red = np.array([170,10, 110])
upper_red = np.array([180, 255, 255]) 
mask2 = cv2.inRange(hsv1, lower_red, upper_red) 
mask1 = mask2
mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
mask2 = cv2.bitwise_not(mask1)
res1 = cv2.bitwise_and(background1, background1, mask = mask1)    
res2 = cv2.bitwise_and(img1, img1, mask = mask2) 
cv2.imshow('res1',res1)

lower_green = np.array([50, 52, 72]) 
upper_green = np.array([102, 255, 255])
mask4 = cv2.inRange(hsv1, lower_green, upper_green) 
mask3 = mask4
mask3 = cv2.morphologyEx(mask3, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask3 = cv2.dilate(mask3, np.ones((3, 3), np.uint8), iterations = 1) 
mask4 = cv2.bitwise_not(mask3)
res3 = cv2.bitwise_and(background1, background1, mask = mask3)    
res4 = cv2.bitwise_and(img1, img1, mask = mask4) 
cv2.imshow('res3',res3)

lower_blue = np.array([100,150,0]) 
upper_blue = np.array([140,255, 255])
mask6 = cv2.inRange(hsv1, lower_blue, upper_blue) 
mask5 = mask6
mask5 = cv2.morphologyEx(mask5, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask5 = cv2.dilate(mask5, np.ones((3, 3), np.uint8), iterations = 1) 
mask6 = cv2.bitwise_not(mask5)
res5 = cv2.bitwise_and(background1, background1, mask = mask5)    
res6= cv2.bitwise_and(img1, img1, mask = mask6) 
cv2.imshow('res5',res5)

lower_yellow = np.array([20,100,100]) 
upper_yellow = np.array([30,255, 255])
mask8= cv2.inRange(hsv1, lower_yellow, upper_yellow) 
mask7 = mask8
mask7 = cv2.morphologyEx(mask7, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask7 = cv2.dilate(mask7, np.ones((3, 3), np.uint8), iterations = 1) 
mask8 = cv2.bitwise_not(mask7)
res7 = cv2.bitwise_and(background1, background1, mask = mask7)    
res8= cv2.bitwise_and(img1, img1, mask = mask8) 
cv2.imshow('res7',res7)

cv2.waitKey(0)
cv2.destroyAllWindows()

