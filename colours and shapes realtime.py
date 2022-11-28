#importing modules

import cv2   
import numpy as np
import math

#capturing video through webcam
cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
while(1):
    _, frame = cap.read()   
    #converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #definig the range of red color
    red_lower=np.array([136,87,111],np.uint8)
    red_upper=np.array([180,255,255],np.uint8)

    #defining the Range of Blue color
    blue_lower=np.array([99,115,150],np.uint8)
    blue_upper=np.array([110,255,255],np.uint8)
    
    #defining the Range of yellow color
    yellow_lower=np.array([22,60,200],np.uint8)
    yellow_upper=np.array([60,255,255],np.uint8)

    green_lower = np.array([50, 52, 72],np.uint8) 
    green_upper= np.array([102, 255, 255],np.uint8)

    #finding the range of red,blue and yellow color in the image
    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
    green=cv2.inRange(hsv,green_lower,green_upper)
    
    #Morphological transformation, Dilation  	
    kernal = np.ones((5 ,5), "uint8")

    red=cv2.dilate(red, kernal)
    res=cv2.bitwise_and(frame, frame, mask = red)

    blue=cv2.dilate(blue,kernal)
    res1=cv2.bitwise_and(frame, frame, mask = blue)

    yellow=cv2.dilate(yellow,kernal)
    res2=cv2.bitwise_and(frame,frame, mask = yellow)

    green=cv2.dilate(green,kernal)
    res2=cv2.bitwise_and(frame, frame, mask = green)


    #Tracking the Red Color
    contours, _ =cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
            if(area>800):
                    
                    x,y,w,h = cv2.boundingRect(contour)	
                    frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(frame,"Red",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
                    cv2.drawContours(frame, contours, 1, (0, 255,0))
                    if len(approx) == 3:
                        cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 4:
                        cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                    elif  len(approx)>100:
                        cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 6:
                        cv2.putText(frame, "Hexagon", (x, y), font, 0.5, (1))
                    elif len(approx) == 5:
                        cv2.putText(frame, "Pentagon", (x, y), font, 0.5, (1))
                
                    
    #Tracking the Blue Color
    contours, _ =cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
            if(area>800):
                    x,y,w,h = cv2.boundingRect(contour)	
                    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(frame,"Blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
                    cv2.drawContours(frame, contours, 1, (0, 255,0))
                    if len(approx) == 3:
                        cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 4:
                        cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                    elif 10 < len(approx) < 20:
                        cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 6:
                        cv2.putText(frame, "Hexagon", (x, y), font, 0.5, (1))
                    elif len(approx) == 5:
                        cv2.putText(frame, "Pentagon", (x, y), font, 0.5, (1))

    #Tracking the yellow Color
    contours, _ =cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
            if(area>800):
                    x,y,w,h = cv2.boundingRect(contour)	
                    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.putText(frame,"yellow",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))
                    cv2.drawContours(frame, contours, 1, (0, 255,0))
                    if len(approx) == 3:
                        cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 4:
                        cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                    elif 10 < len(approx) < 20:
                        cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 6:
                        cv2.putText(frame, "Hexagon", (x, y), font, 0.5, (1))
                    elif len(approx) == 5:
                        cv2.putText(frame, "Pentagon", (x, y), font, 0.5, (1))

    contours, _ =cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
            if(area>800):
                    x,y,w,h = cv2.boundingRect(contour)	
                    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.putText(frame,"green",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255))
                    cv2.drawContours(frame, contours, 1, (0, 255,0))
                    if len(approx) == 3:
                        cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 4:
                        cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                    elif 10 < len(approx) < 20:
                        cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
                    elif len(approx) == 6:
                        cv2.putText(frame, "Hexagon", (x, y), font, 0.5, (1))
                    elif len(approx) == 5:
                        cv2.putText(frame, "Pentagon", (x, y), font, 0.5, (1))
                
     
  
    cv2.imshow("Color Tracking",frame)
    #cv2.imshow("red",res) 	
    if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break  
      
