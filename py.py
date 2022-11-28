from serial import Serial
import serial
import time #Required to use delay functions

arduinodata = serial.Serial('COM6',9600)#Create Serial port object called ArduinoUnoSerialData
time.sleep(2)#wait for 2 secounds for the communication to get established
print (arduinodata.readline())#read the serial data and print it as line 
print ("You have new message from Arduino")
while True:        
    var = input()#get input from user             
    if (var == '1'):#if the value is 1         
        arduinodata.write(b'1')#send 1 to the arduino's Data code       
        print ("LED turned ON")         
        time.sleep(1)          
    elif (var == '0'): #if the value is 0         
        arduinodata.write(b'0')#send 0 to the arduino's Data code    
        print ("LED turned OFF")         
        time.sleep(1)
    else:
        arduinodata.write(b'0') #send 0    t   
        print ("I'm fine too,Are you Ready to !!!")         
        print ("Type 1 to turn ON LED and 0 to turn OFF LED")         
        time.sleep(1)
