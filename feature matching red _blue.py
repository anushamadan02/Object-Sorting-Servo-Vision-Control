import cv2
import numpy as np
import sklearn
from sklearn.metrics import pairwise
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)

template1 = cv2.imread("red_1.png", cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread("green_1.png",cv2.IMREAD_GRAYSCALE)
template3 = cv2.imread("blue_1.png",cv2.IMREAD_GRAYSCALE)
template4 = cv2.imread("yellow_1.png",cv2.IMREAD_GRAYSCALE)
w, h =template1.shape[::-1]
while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res1 = cv2.matchTemplate(gray_frame, template1, cv2.TM_CCOEFF_NORMED)
    res3 = cv2.matchTemplate(gray_frame, template3, cv2.TM_CCOEFF_NORMED)
    res4 = cv2.matchTemplate(gray_frame, template4, cv2.TM_CCOEFF_NORMED)
    loc1 = np.where(res1 >= 0.62)
    loc3 = np.where(res1 >= 0.62)
    loc4 = np.where(res1 >= 0.45)
    
    def Enquiry1(loc1):
        return(np.array(loc1))
    #def Enquiry2(loc2):
        #return(np.array(loc2))
    def Enquiry3(loc3):
        return(np.array(loc3))
    def Enquiry4(loc4):
        return(np.array(loc4))
    
    if Enquiry1(loc1).size:
        print('detected')
        cv2.putText(frame,"RED TRIANGLE",(50,50),font,1,(0,255,0),2)
        for pt in zip(*loc1[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
            
    elif Enquiry3(loc3).size:
        print('detected')
        cv2.putText(frame,"BLUE PENTAGON",(50,50),font,1,(0,255,0),2)
        for pt in zip(*loc3[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        
    elif Enquiry4(loc4).size:
        print('detected')
        cv2.putText(frame,"YELLOW CIRCLE",(50,50),font,1,(0,255,0),2)
        for pt in zip(*loc4[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    else:
        print('empty')

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

