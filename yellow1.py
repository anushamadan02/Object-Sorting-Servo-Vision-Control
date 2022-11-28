import cv2
import numpy as np
import sklearn
from sklearn.metrics import pairwise

cap = cv2.VideoCapture(0)
template = cv2.imread("yellow_1.png", cv2.IMREAD_GRAYSCALE)
font = cv2.FONT_HERSHEY_SIMPLEX
w, h =template.shape[::-1]
while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.5)
    #print(loc)
    def Enquiry(loc):
        #print(np.array(loc))
        return(np.array(loc))
    if Enquiry(loc).size:
        print('not empty')
        cv2.putText(frame,"YELLOW CIRCLE",(50,50),font,1,(0,255,0),2)
    else:
        print('empty')
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
