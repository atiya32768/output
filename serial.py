#port
#baudrate
#bytesize
#timeout
#stopbits

#import time
#import usb
#import usb.util

#try to send signal to the macropad
import serial 
import keyboard

ser=serial.Serial(port=     , baudrate=     , bytesize= , timeout= 2, stopbits=serial.STOPBITS_ONE)

s=ser.read(100)


