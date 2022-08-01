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

            

#get output from the terminal- LQ terminal is like a file, where the output is always changing
#use the file path
#store output - maybe store it in a list
#strip-to only have the numbers
#now that we've stored all of the numbers in a list
#we need to seperate the values out-so every 4 numbers, we should add a new line
#the ouput format is 4 numbers

#keep a log of output in a file-json file?
#then save in macros file on ciruitpy drive
#output on macropad screen
#add a number to the list, then add a new line
#then seperate


#We have the list of outputs
#We need a way to assign all of the inputs from the command line into a list
#then append the two values together in a list
#print to screen

#We need to find a way to refer to the enter button



#Need to find a way to store all of the commands pressed in a list 
#we store the value in the list, if they choose a command that isn't N/A and press enter
#the order is to press a command, then enter

#we then compare the positions of this list and my_lines list

#we have alot of options
#we have some if statements
#we have an if statement where if key_event and key_event is pressed...
#then we store those commands in a list
#somehow find a way to store all of the possible options into a list
#then compare this list to my_lines[]


#we compare the position and add the elements in their relative positions into a third array
#we concatentate

#the position of elements in their separate arrays need to be compared

#write the elements to the file after the comparison