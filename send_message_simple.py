
from adafruit_macropad import MacroPad
import json
import os

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
    if key_event.key_number==3 and macropad.encoder % 5 ==0:
            for i in range(len(number)):
                text_lines[i].text=number[i]
                text_lines.show()


