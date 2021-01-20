# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:36:11 2021

@author: mojtaba Ebrahimi
alterasonic
"""
import serial
from vpython import *

yl=50
xl=500

Box=box(length=0.25,width=10,height=5,color=color.blue,pos=vector(-8.5,0,0))
Triger=cylinder(pos=vector(-8.5,0,-2.5),color=color.white,length=1.5)
Echo=cylinder(pos=vector(-8.5,0,+2.5),color=color.white,length=1.5)
#axial
pointerx=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.blue)#x is blue
pointery=arrow(pos=vector(0,0,0),axis=vector(0,1,0),color=color.red)#y is red
pointerz=arrow(pos=vector(0,0,0),axis=vector(0,0,1),color=color.white)#z is white
#Target Plane
Plane=box(length=0.1,width=10,height=5)
lamp=local_light(pos=vector(0,8,0),color=color.yellow)

L= label(pos= vector(0,3.5,0), text= 'Distance is : ')

arduinoData=serial.Serial('com3',9600)
i=0
while (i<xl):
    rate(20)
    if(arduinoData.inWaiting() >0):
        data1=arduinoData.readline()
        data=float(data1)
        data2=str(data)
        Plane.pos=vector(-7+data,0,0)
        L.text = b'X (cm) =' + data2.encode()
        i=i+1
        
          
        
       
        
arduinoData.close()