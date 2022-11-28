import cv2
import numpy
import time
import np
img01=cv2.imread('circles.png')
img2 = cv2.resize(img01,(250,250))
background02=cv2.imread('circles.png')
background2 = cv2.resize(background02,(250,250))
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
lower_green = np.array([50, 52, 72]) 
upper_green = np.array([102, 255, 255])
mask4 = cv2.inRange(hsv2, lower_green, upper_green) 
mask3 = mask4
mask3 = cv2.morphologyEx(mask3, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
mask3 = cv2.dilate(mask3, np.ones((3, 3), np.uint8), iterations = 1) 
mask4 = cv2.bitwise_not(mask3)
res3 = cv2.bitwise_and(background2, background2, mask = mask3)    
res4 = cv2.bitwise_and(img2, img2, mask = mask4) 
cv2.imshow('res3',res3)
cv2.waitKey(0)
cv2.destroyAllWindows()
