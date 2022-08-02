import contextlib  
import numpy as np
from adafruit_macropad import MacroPad
from adafruit_hid.keycode import Keycode
import logging
macropad = MacroPad()
# we need the number of arrays we want to split it in
# so we need the number of outputs from the terminal
logging.basicConfig(level=logging.DEBUG)
my_lines=[]
input_list=[]
num_of_output=0 # a internal counter
output_file_path="E:\output"
file_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Laser Quantum Ltd\LQ Terminal.lnk"

while True:
    key_event = macropad.keys.events.get()
    with open(file_path, "a") as text_file:
        with contextlib.redirect_stdout(text_file):
            for my_lines in text_file:
               # print out output at that specific position
                num_of_output +=1
                if key_event.key_number==1 and key_event.pressed and macropad.encoder_switch==True: # prints out the output at that specific moment 
                    one_output=macropad.display_text(my_lines[num_of_output])
                    one_output.show() 
                else:
                    if key_event.key_number==2 and key_event.pressed and macropad.encoder_switch==True:
                        continue
                # display each output in turn onto the macropad screen for a specific amount of time
                my_lines.append(my_lines)
            logging.debug("The output is added to a list in the file")
            # splits=np.split(my_lines, num_of_output)
    # we need a way to assign the specific commands with the numbers
    # length of the array is the num_of_output

            for element in range(0, num_of_output):
                if key_event and key_event.pressed and key_event !='':
                    continue
                if key_event.key_number ==11 and key_event.pressed:
                    continue
                if key_event.key_number != '' and key_event.key_number != 'ENTER': #apppend the initial commands into a list
                    input_list.append(key_event.key_number)

    # we compare the lists to each other using the same position
            for i, j, k in list(zip(my_lines, input_list)):
                output_file_path="E:\output"
                x=list(zip(input_list,my_lines))  # use zip function to format lists in a specific way
                tuple(x) 
                tuple_no_space=str(tuple(x)).replace(', ', '')

    # displays all of the commands and outputs stored in the list onto the macropad screen
    text_lines= macropad.display_text(title="Commands & Output")
    if key_event.key_number==3 and key_event.pressed and macropad.encoder_switch==True:
        text_lines[1].text=macropad.display_text(tuple_no_space)
        text_lines.show()






                    
                



                


                
