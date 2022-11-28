import cv2
import numpy as np
import sklearn
import time
from sklearn.metrics import pairwise
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

template1 = cv2.imread("red_1.png", cv2.IMREAD_GRAYSCALE)
template4 = cv2.imread("yellow_1.png",cv2.IMREAD_GRAYSCALE)
w, h =template1.shape[::-1]
countred=0
countyellow=0
red=0
yellow=0

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res1 = cv2.matchTemplate(gray_frame, template1, cv2.TM_CCOEFF_NORMED)
    res4 = cv2.matchTemplate(gray_frame, template4, cv2.TM_CCOEFF_NORMED)
    loc1 = np.where(res1 >= 0.62)
    loc4 = np.where(res1 >= 0.45)
    def to_be_done_if_red():
        print('Helllooooo')
        time.sleep(2)
    def to_be_done_if_yellow():
        print('Hiiiiiiiiii')
        time.sleep(2)
    def Enquiry1(loc1):
        return(np.array(loc1))
    #def Enquiry2(loc2):
        #return(np.array(loc2))

    def Enquiry4(loc4):
        return(np.array(loc4))
    
    if Enquiry1(loc1).size:
        countred=countred+1
        red=1
        print('detected red',countred)
        cv2.putText(frame,"RED",(50,50),font,1,(0,255,0),2)
        for pt in zip(*loc1[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        if red==1:
            to_be_done_if_red()     
        
    elif Enquiry4(loc4).size:
        countyellow=countyellow+1
        yellow=1
        print('detected yellow',countyellow)
        cv2.putText(frame,"YELLOW",(50,50),font,1,(0,255,0),2)
        for pt in zip(*loc4[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        if yellow==1:
            to_be_done_if_yellow()
            continue
            
    else:
        time.sleep(5)
        print('empty')

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

