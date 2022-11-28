import cv2
import numpy as np
import sklearn
import time
from sklearn.metrics import pairwise
from serial import Serial
import serial
arduinodata = serial.Serial('COM6',9600)#Create Serial port object called ArduinoUnoSerialData
time.sleep(2)#wait for 2 secounds for the communication to get established
print (arduinodata.readline())#read the serial data and print it as line 
print ("You have new message from Arduino")
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
        arduinodata.write(b'1')
        cv2.putText(frame,"RED",(50,50),font,1,(0,255,0),2)
        for pt in zip(*loc1[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        if red==1:
            to_be_done_if_red()     
        
    elif Enquiry4(loc4).size:
        arduinodata.write(b'0')
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
        arduinodata.write(b'2')
        print('empty')

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

