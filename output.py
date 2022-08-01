import contextlib  
import numpy as np
from adafruit_macropad import MacroPad
macropad = MacroPad()
from adafruit_hid.keycode import Keycode
# we need the number of arrays we want to split it in
# so we need the number of outputs from the terminal

my_lines=[]
input_list=[]
num_of_output=0 # a internal counter
output_file_path="E:\output"
file_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Laser Quantum Ltd\LQ Terminal.lnk"
with open(file_path, "w") as text_file:
    with contextlib.redirect_stdout(text_file):
        for my_lines in text_file:
            num_of_output +=1
            my_lines.append(my_lines)
        print("The output is added to the list in the file")
        # splits=np.split(my_lines, num_of_output)
# we need a way to assign the specific commands with the numbers
# mylines[0][num_of_output]
# length of the array is the num_of_output

        for element in range(0, num_of_output):
            while True:
                key_event = macropad.keys.events.get()
                if key_event and key_event.pressed and key_event !='':
                    continue
                if key_event.key_number =='ENTER' and key_event.pressed:
                    continue
                if key_event.key_number != '' and key_event.key_number != 'ENTER':
                    input_list.append(key_event.key_number)


# we compare the lists to each other using the same position
        for i, j, k in zip(my_lines, input_list):
            output_file_path="E:\output"
            x=zip(input_list,my_lines)
            tuple(x)


            # element at that position 

                
                

                    
                



                


                
                


                

                # need to find a way to sort elements in a list

            

