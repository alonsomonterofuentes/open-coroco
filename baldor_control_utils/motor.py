#!/usr/bin/env python

#importing libraries

import yarp   as y
import serial as s
from serial import SerialException
from numpy import pi
from time import sleep
from motor_tools import *


#-----------------yarp connection----------------------------------

#stating yarp network
y.Network.init()

class motor_x(position)
    #starting a yarp network
    y.Network_init()
    
    #creating an ouput port for stm32_x position
    out_1      = y.BufferedPortBottle()
    out_1_name = "/stm32_"+ self.position "/position/out1"
    out_1.open(out_1_name) 

    #creating a input port
    in_1      = y.BufferedPortBottle()
    in_1_name = "/stm32_"+ self.position "/position/in1"
    in_1.open(in_1_name) 

    #creating an input port from ps3 controller
    in_speed      = y.BufferedPortBottle()
    in_speed_name = "/stm32_"+ self.position "/position/in1"
    in_speed.open(in_speed_name) 

    
