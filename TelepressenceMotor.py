#This is a simple python script to move a raspberry pi robot using WiFi

import RPi.GPIO as GPIO
import socket
import csv
import time
import os
import re
import subprocess


LeftMotarForward = 33
RightMotarForward = 31
LeftMotarReverse = 29
RightMotarReverse = 35


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)   
GPIO.setup(LeftMotarForward,GPIO.OUT)
GPIO.setup(RightMotarForward,GPIO.OUT)
GPIO.setup(LeftMotarReverse,GPIO.OUT)
GPIO.setup(RightMotarReverse,GPIO.OUT)

#Setting up UDP ip address and port 
UDP_IP = "192.168.29.123"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024)
    raw=data
    print  raw

    if raw=="A":
        #Forward Movement of Robot
         GPIO.output(LeftMotarForward,True)
         GPIO.output(RightMotarForward,True)
         GPIO.output(LeftMotarReverse,False)
         GPIO.output(RightMotarReverse,False)
         print "Robot Moving Forward"
        
        
    elif raw=="E":
        #Stop the Robot
        GPIO.output(LeftMotarForward,False)
        GPIO.output(RightMotarForward,False)
        GPIO.output(LeftMotarReverse,False)
        GPIO.output(RightMotarReverse,False)
        print "Robot Stoped"
        
        
    elif raw=="B":
        #Movement in Backward Direction
        GPIO.output(LeftMotarForward,False)
        GPIO.output(RightMotarForward,False)
        GPIO.output(LeftMotarReverse,True)
        GPIO.output(RightMotarReverse,True)
        print "Robot Moving Backward"
        
        
    elif raw=="R":
        #Movement in Right Direction
        GPIO.output(LeftMotarForward,True)
        GPIO.output(RightMotarForward,False)
        GPIO.output(LeftMotarReverse,False)
        GPIO.output(RightMotarReverse,False)
        print "Robot Moving Right"

    elif raw=="L":
        #Movement in Left Direction
        GPIO.output(LeftMotarForward,False)
        GPIO.output(RightMotarForward,True)
        GPIO.output(LeftMotarReverse,False)
        GPIO.output(RightMotarReverse,False)  
        print "Robot Moving Left"

    else:
        pass
    #else:
    #print "Killing all processes and sending control back to user"  
    #subprocess.call("./kill_process.sh")


GPIO.cleanup()

