#importing modules

import cv2   
import numpy as np
import math
import imutils
import sklearn
from sklearn.metrics import pairwise

bg = None
font = cv2.FONT_HERSHEY_COMPLEX
x,y,w,h = 40,40,40,40


def run_avg(image, accumWeight):#larger accumweight good when lot of motion happens
    global bg
    # initialize the background
    if bg is None:
        bg = image.copy().astype("float")#converted to float
        return
    cv2.accumulateWeighted(image, bg, accumWeight)#updates a running average

def segment(image, threshold=25):
    global bg
    # find the absolute difference between background and current frame
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # threshold the diff image so that we get the foreground
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]#binary (basically seperated from the background)
    # get the contours in the thresholded image
    (cnts, _) = cv2.findContours(thresholded.copy(),
    cv2.RETR_EXTERNAL,#external contours are observed
    cv2.CHAIN_APPROX_SIMPLE)#the inside contours are submerged

    # return None, if no contours detected
    if len(cnts) == 0:
        return
    else:
        # based on contour area, get the maximum contour which is the hand
        segmented = max(cnts, key=cv2.contourArea)   #area
        return (thresholded, segmented)
if __name__ == "__main__":
    # initialize accumulated weight
    accumWeight = 0.5
    camera = cv2.VideoCapture(0)
    top, right, bottom, left = 10, 350, 225, 590
    num_frames = 0
    calibrated = False
    argument=input('Enter the colour to be detected')
    while(True):
        (grabbed, frame) = camera.read()#getting current frame
        frame = imutils.resize(frame, width=700)#resize the frame
        frame = cv2.flip(frame, 1)#flipping
        clone = frame.copy()#clone the frame
        (height, width) = frame.shape[:2]#getting height and width o frame
        roi = frame[top:bottom, right:left]#getting region of interest
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        
        hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
        

        #definig the range of red color
        red_lower=np.array([136,87,111],np.uint8)
        red_upper=np.array([180,255,255],np.uint8)

        #defining the Range of Blue color
        blue_lower=np.array([99,115,150],np.uint8)
        blue_upper=np.array([110,255,255],np.uint8)

        #defining the Range of yellow color
        yellow_lower=np.array([22,60,200],np.uint8)
        yellow_upper=np.array([60,255,255],np.uint8)

        #defining the Range of green color
        green_lower = np.array([50, 52, 72]) 
        green_upper = np.array([102, 255, 255])
                
  

        #finding the range of red,blue and yellow color in the image
        red=cv2.inRange(hsv, red_lower, red_upper)
        blue=cv2.inRange(hsv,blue_lower,blue_upper)
        yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
        green=cv2.inRange(hsv,green_lower,green_upper)

        #Morphological transformation, Dilation  	
        kernal = np.ones((5 ,5), "uint8")
        red=cv2.dilate(red, kernal)
        blue=cv2.dilate(blue,kernal)
        yellow=cv2.dilate(yellow,kernal)
        green=cv2.dilate(green,kernal)
        

        if num_frames < 30:
            run_avg(gray, accumWeight)
            if num_frames == 1:
                print("[STATUS] please wait! calibrating...")
            elif num_frames == 29:
                print("[STATUS] calibration successfull...")
                
        else:
            # segment the hand region
            hand = segment(gray)

            # check whether hand region is segmented
            if hand is not None:
                (thresholded, segmented) = hand
                if (argument =='red'):
                    contours, _ =cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    for pic, contour in enumerate(contours):
                            area = cv2.contourArea(contour)
                            approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
                            a = approx.ravel()[0]
                            b= approx.ravel()[1]
                            if(area>300):	
                                    clone = cv2.rectangle(clone,(x,y),(x+w,y+h),(0,0,255),2)
                                    cv2.putText(clone,"RED color",(50,50),font,1,(0,255,0),2)
                                    if len(approx) == 3:
                                        cv2.putText(clone, "Triangle", (a, b), font, 1, (0, 0, 0))
                                    elif len(approx) == 4:
                                        cv2.putText(clone, "Rectangle", (a, b), font, 1, (0, 0, 0))
                                    elif 10 < len(approx) < 20:
                                        cv2.putText(clone, "Circle", (a, b), font, 1, (0, 0, 0))
                                    elif len(approx) == 6:
                                        cv2.putText(clone, "Hexagon", (a, b), font, 0.5, (1))
                                    elif len(approx) == 5:
                                        cv2.putText(clone, "Pentagon", (a, b), font, 0.5, (1))
                if (argument=='blue'):
                    contours, _ =cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    for pic, contour in enumerate(contours):
                        approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
                        a = approx.ravel()[0]
                        b= approx.ravel()[1]
                        area = cv2.contourArea(contour)
                        if(area>300):	
                                clone = cv2.rectangle(clone,(x,y),(x+w,y+h),(255,0,0),2)
                                cv2.putText(clone,"Blue color",(50,50),font,1,(0,255,0),2)
                                if len(approx) == 3:
                                    cv2.putText(clone, "Triangle", (a, b), font, 1, (0, 0, 0))
                                elif len(approx) == 4:
                                    cv2.putText(clone, "Rectangle", (a, b), font, 1, (0, 0, 0))
                                elif 10 < len(approx) < 20:
                                    cv2.putText(clone, "Circle", (a, b), font, 1, (0, 0, 0))
                                elif len(approx) == 6:
                                    cv2.putText(clone, "Hexagon", (a, b), font, 0.5, (1))
                                elif len(approx) == 5:
                                    cv2.putText(clone, "Pentagon", (a, b), font, 0.5, (1))
                                    
                if (argument=='yellow'):
                    contours, _ =cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    for pic, contour in enumerate(contours):
                            area = cv2.contourArea(contour)
                            approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
                            a = approx.ravel()[0]
                            b= approx.ravel()[1]
                            if(area>300):	
                                    clone = cv2.rectangle(clone,(x,y),(x+w,y+h),(0,255,0),2)
                                    cv2.putText(clone,"yellow  color",(50,50),font,1,(0,255,0),2)
                                    if len(approx) == 3:
                                        cv2.putText(clone, "Triangle", (a, b), font, 1, (0, 0, 0))
                                    elif len(approx) == 4:
                                        cv2.putText(clone, "Rectangle", (a, b), font, 1, (0, 0, 0))
                                    elif 10 < len(approx) < 20:
                                        cv2.putText(clone, "Circle", (a, b), font, 1, (0, 0, 0))
                                    elif len(approx) == 6:
                                        cv2.putText(clone, "Hexagon", (a, b), font, 0.5, (1))
                                    elif len(approx) == 5:
                                        cv2.putText(clone, "Pentagon", (a, b), font, 0.5, (1))
                if (argument=='green'):
                    contours, _ =cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    for pic, contour in enumerate(contours):
                            area = cv2.contourArea(contour)
                            approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
                            a = approx.ravel()[0]
                            b= approx.ravel()[1]
                            if(area>300):
                                    clone = cv2.rectangle(clone,(x,y),(x+w,y+h),(0,255,0),2)
                                    cv2.putText(clone,"green color",(50,50),font,1,(0,255,0),2)
                                    if len(approx) == 3:
                                        cv2.putText(clone, "Triangle", (a, b), font, 1, (0, 0, 0))
                                    elif len(approx) == 4:
                                        cv2.putText(clone, "Rectangle", (a, b), font, 1, (0, 0, 0))
                                    elif 10 < len(approx) < 20:
                                        cv2.putText(clone, "Circle", (a, b), font, 1, (0, 0, 0))
                                    elif len(approx) == 6:
                                        cv2.putText(clone, "Hexagon", (a, b), font, 0.5, (1))
                                    elif len(approx) == 5:
                                        cv2.putText(clone, "Pentagon", (a, b), font, 0.5, (1))
                
        
        cv2.rectangle(clone, (left, top), (right, bottom), (0,255,0), 2)

        # increment the number of frames
        num_frames += 1
        cv2.imshow("Video Feed", clone)
        keypress = cv2.waitKey(1) 

camera.release()
cv2.destroyAllWindows()




