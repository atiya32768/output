#we read the lines from the input and output file and concatenate the two different lists
from adafruit_macropad import MacroPad
import sys
macropad=Macropad()
class Manager:
        # Initialization ------

    def read_line(filename):
        try:
            list_of_values=[]
            file=open(filename, "r")
            lines=file.readlines()
            for line in range(len(lines)):
                list_of_values.append(lines[line].strip('\n'))
            file.close()
        except: 
            print("Error reading the file")

        return list_of_values    
    # put text into the input file
    input=read_line("input.txt")  
    output=read_line("output.txt")       

    result_on_screen=list(zip(input, output))
    result_on_screen='\n'.join(map(str,result_on_screen))
    result_on_screen=tuple(result_on_screen)

    with open("final_output.txt", 'w') as final_file:
        sys.stdout=final_file
        print(result_on_screen)
        final_file.close()


while True:
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        continue
    if macropad.encoder == 0 or macropad.encoder % 5 == 0:
        print("Encoder: {}".format(macropad.encoder))
        print("Key pressed: {}".format(key_event.key_number))
        if key_event.key_number == 0:
            print("N/A")
        elif key_event.key_number == 1:
            print("CURRENT")
        elif key_event.key_number == 2:
            print("N/A")
        elif key_event.key_number == 3:
            print("N/A")
        elif key_event.key_number == 4:
            print("POWER")
        elif key_event.key_number == 5:
            print("N/A")
        elif key_event.key_number == 6:
            print("N/A")
        elif key_event.key_number == 7:
            print("=")
        elif key_event.key_number == 8:
            print("N/A")
        elif key_event.key_number == 9:
            print("N/A")
        elif key_event.key_number == 10:
            print("ENTER")
        else:
            print("N/A")
    if key_event and key_event.pressed:
        continue
    if macropad.encoder == 1 or macropad.encoder % 5 == 1:
        print("Encoder: {}".format(macropad.encoder))
        print("Key pressed: {}".format(key_event.key_number))
        if key_event.key_number == 0:
            print("7")
        elif key_event.key_number == 1:
            print("8")
        elif key_event.key_number == 2:
            print("9")
        elif key_event.key_number == 3:
            print("4")
        elif key_event.key_number == 4:
            print("5")
        elif key_event.key_number == 5:
            print("6")
        elif key_event.key_number == 6:
            print("1")
        elif key_event.key_number == 7:
            print("2")
        elif key_event.key_number == 8:
            print("3")
        elif key_event.key_number == 9:
            print("*")
        elif key_event.key_number == 10:
            print("0")
        else:
            print("#")
    if key_event and key_event.pressed:
        continue
    if macropad.encoder == 2 or macropad.encoder % 5 == 2:
        print("Encoder: {}".format(macropad.encoder))
        print("Key pressed: {}".format(key_event.key_number))
        if key_event.key_number == 0:
            print("N/A")
        elif key_event.key_number == 1:
            print("N/A")
        elif key_event.key_number == 2:
            print("N/A")
        elif key_event.key_number == 3:
            print("N/A")
        elif key_event.key_number == 4:
            print("ON")
        elif key_event.key_number == 5:
            print("N/A")
        elif key_event.key_number == 6:
            print("N/A")
        elif key_event.key_number == 7:
            print("OFF")
        elif key_event.key_number == 8:
            print("N/A")
        elif key_event.key_number == 9:
            print("N/A")
        elif key_event.key_number == 10:
            print("ENTER")
        else:
            print("0")
    if key_event and key_event.pressed:
        continue
    if macropad.encoder == 3 or macropad.encoder % 5 == 3:
        print("Encoder: {}".format(macropad.encoder))
        print("Key pressed: {}".format(key_event.key_number))
        if key_event.key_number == 0:
            print("LTEMP")
        elif key_event.key_number == 1:
            print("DTEMP")
        elif key_event.key_number == 2:
            print("CTEMP")
        elif key_event.key_number == 3:
            print("N/A")
        elif key_event.key_number == 4:
            print("N/A")
        elif key_event.key_number == 5:
            print("N/A")
        elif key_event.key_number == 6:
            print("ACT")
        elif key_event.key_number == 7:
            print("N/A")
        elif key_event.key_number == 8:
            print("SET")
        elif key_event.key_number == 9:
            print("=")
        elif key_event.key_number == 10:
            print("ENTER")
        else:
            print("?")
    if key_event and key_event.pressed:
        continue
    if macropad.encoder == 4 or macropad.encoder % 5 == 4:
        print("Encoder: {}".format(macropad.encoder))
        print("Key pressed: {}".format(key_event.key_number))
        if key_event.key_number == 0:
            print("N/A")
        elif key_event.key_number == 1:
            print("VOAGOTO")
        elif key_event.key_number == 2:
            print("N/A")
        elif key_event.key_number == 3:
            print("N/A")
        elif key_event.key_number == 4:
            print("MIN")
        elif key_event.key_number == 5:
            print("N/A")
        elif key_event.key_number == 6:
            print("N/A")
        elif key_event.key_number == 7:
            print("MAX")
        elif key_event.key_number == 8:
            print("N/A")
        elif key_event.key_number == 9:
            print("N/A")
        elif key_event.key_number == 10:
            print("ENTER")
        else:
            print("N/A")




