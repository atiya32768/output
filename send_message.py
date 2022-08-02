

from adafruit_macropad import MacroPad
macropad = MacroPad()
file_path="C:\Users\atiya.mahboob\OneDrive - Novanta\Documents\test_file.txt"
number=[]
letter=[]
while True:
    key_event = macropad.keys.events.get()
    if key_event.key_number==3 and key_event.pressed and macropad.encoder_switch==True:
         for i, j  in list(zip(number, letter)):
                output_file_path="E:\output"
                x=list(zip(number, letter))  # use zip function to format lists in a specific way
                tuple(x) 
                tuple_no_space=str(tuple(x)).replace(', ', '')

    text_lines= macropad.display_text(title="Commands & Output")
    if key_event.key_number==2 and key_event.pressed and macropad.encoder_switch==True:
        for i in range(len(tuple_no_space)):
            text_lines[i].text=macropad.display_text(tuple_no_space[i])
            text_lines.show()