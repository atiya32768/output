
from adafruit_macropad import MacroPad
import json
import os
from adafruit_display_text import label, bitmap_label
from adafruit_bitmap_font import bitmap_font


macropad = MacroPad()
# relate the file path to the arrays
# file_path="C:\Users\atiya.mahboob\OneDrive - Novanta\Documents\test_file.txt"
file_path="C:\Users\atiya.mahboob\OneDrive - Novanta\Documents\test_file.txt"
path=os.getcwd()+file_path
line=open(path,'r').read().splitlines()[0]
number=json.loads(line)

text_lines=macropad.display_text(title="Test")
while True:
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        continue
    if  key_event.key_number==3 and key_event.pressed and macropad.encoder_switch==True:
        text_lines[1].text=macropad.display_text(number)
        text_lines.show()


