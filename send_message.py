

from adafruit_macropad import MacroPad
macropad = MacroPad()
import logging
file_path="C:\Users\atiya.mahboob\OneDrive - Novanta\Documents\test_file.txt"
number=[]
letter=[]
while True:
    key_event = macropad.keys.events.get()
    if key_event.key_number==3 and key_event.pressed and macropad.encoder_switch==True:
        