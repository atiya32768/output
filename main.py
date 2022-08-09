#port
#baudrate
#bytesize
#timeout
#stopbits

#import time
#import usb
#import usb.util

#try to send signal to the macropad
import keyboard
import time

import serial

ser=serial.Serial(port="COM4" , baudrate= "9600" , bytesize=8 , timeout= 2, stopbits=serial.STOPBITS_ONE)

ser.isOpen()


while True:
    ser.write("This is the message\r\n".encode('Ascii'))
    receive=ser.readline()
    print(receive.decode('Ascii'))
    time.sleep(1)
    if keyboard.is_pressed('1'):
        print("User need to Quit the application")
        break

# we need to get information from the PC to the macropad screen

ser.close()
