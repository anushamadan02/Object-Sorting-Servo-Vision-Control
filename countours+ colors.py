import cv2
import imutils
import numpy as np
import time

cap=cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue_object = 0
    red_object = 0

#HSV range of colors
    low_red = np.array([70, 40, 160]) 
    high_red = np.array([180, 255, 255])
    low_blue = np.array([81, 69, 28])
    high_blue = np.array([128, 255, 255])

#masking of detected colors
    maskr = cv2.inRange(hsv_frame, low_red, high_red)
    maskb = cv2.inRange(hsv_frame, low_blue, high_blue)
    
    red = cv2.bitwise_and(frame, frame, mask = maskr)
    blue = cv2.bitwise_and(frame, frame, mask = maskb)
    Result = red + blue
#drawing contours around detected colors
    cntsr = cv2.findContours(maskr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntsr = imutils.grab_contours(cntsr)
    cntsb = cv2.findContours(maskb, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntsb = imutils.grab_contours(cntsb)
    
    
    for c in cntsr:
        arear = cv2.contourArea(c)
        if arear > 5000:
            cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m10"]/M["m00"])
            #cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            cv2.putText(frame, "Red", (cx-5, cy-5), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 3)
            red_object = 1
            
                
    for c in cntsb:
        areab = cv2.contourArea(c)
        if areab > 5000:
            cv2.drawContours(frame, [c], -1, (0,255,0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m10"]/M["m00"])
            #cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            cv2.putText(frame, "Blue", (cx-5, cy-5), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255,255,255), 3)
            
            blue_object = 1
            
#display of frames            
    cv2.imshow("Frame",frame)
    cv2.imshow("Final_result", Result)
    if blue_object == 1:
        print("Object in front of camera is blue")
    if red_object == 1:
        print("Object in front of camera is red")
    if blue_object == 1 & red_object == 1:
        print("both red and blue")
        
    
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()



