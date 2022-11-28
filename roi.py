import cv2
import imutils
import numpy as np
import sklearn
from sklearn.metrics import pairwise
bg = None
cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
top, right, bottom, left = 10, 350, 225, 590
roi = frame[top:bottom, right:left]
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
    cv2.imshow('jsefcb',diff)

    # threshold the diff image so that we get the foreground
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]#binary (basically seperated from the background)
    cv2.imshow('the',thresholded)
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
    while(True):
        (grabbed, frame) = camera.read()#getting current frame
        frame = imutils.resize(frame, width=700)#resize the frame
        frame = cv2.flip(frame, 1)#flipping
        clone = frame.copy()#clone the frame)
        (height, width) = frame.shape[:2]#getting height and width o frame
        roi = frame[top:bottom, right:left]#getting region of interest
        cv2.imshow('rfawef',roi)
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        if num_frames < 30:
            run_avg(gray, accumWeight)
            if num_frames == 1:
                print("[STATUS] please wait! calibrating...")
            elif num_frames == 29:
                print("[STATUS] calibration successfull...")
                
        else:
            # segment the hand region+
            hand = segment(gray)
            # check whether hand region is segmented
            
        
        cv2.imshow("Video Feed", clone)
        keypress = cv2.waitKey(1) 

camera.release()
cv2.destroyAllWindows()

