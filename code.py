import os
import time
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'

# CLASSES AND FUNCTIONS ----------------

class Manager:
    def read_line(filename):
        try:
            list_of_values = []
            file = open(filename, "r")
            lines = file.readlines()
            for line in range(len(lines)):
                list_of_values.append(lines[line].strip('\n'))
            file.close()
        except:
            print("Error reading the file")

        return list_of_values

    input = read_line("macros/input.txt")  
    output = read_line("macros/output.txt")

    output_dictionary = {}

    for each_line in input:
        key_element=each_line.split('\n')[0]
        for line_each in output:
            value_element=line_each.split('\n')[0]
            output_dictionary[key_element]=value_element
            output.remove(value_element)
            break
          
    # we can call the dictionary
    # 
class Output(Manager):
   
    def __init__(self, key, value, output_dictionary):
        self.output_dictionary_keys = output_dictionary[key]
        self.output_dictionary_values = output_dictionary[value]

    def mapping(self):  # switching between the different files 
        # define some for loop
        # where we assign each line to text and pixel
        # for each item in the output_from_file list
        for x in self.output_dictionary.keys():
            macropad.pixels[x] = self.output_dictionary_keys[x]
            output_group[x].text = self.output_dictionary_keys[x]           
            # need to
        for y in self.output_dictionary.values():
            macropad.pixels[y] = self.output_dictionary_values[y]
            input_group[y].text = self.output_dictionary_keys[y]
            
            # we assign a pixel to each item in the txt file
        macropad.display.refresh() 
        macropad.pixels.show()

class App:
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']
    # when they press a certain button
    # we need a way to refer to the 
    # have some string in the app, that we call, depending on which button is pressed
    # this will be displayed on the screen
    # until a certain button is pressed

    def switch(self):  # we are switching the name of the app and app macros
        """ Activate application settings; update OLED labels and LED
            colors. """
        group[13].text = self.name   # Application name 
        for i in range(12):
            if i < len(self.macros):  # Key in use, set label + LED color - i
                macropad.pixels[i] = self.macros[i][0] 
                group[i].text = self.macros[i][1]   # we then assign the group text
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0 
                group[i].text = ''
                
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()

# INITIALIZATION -----------------------

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False


group = displayio.Group() 
for key_index in range(12):  
    x = key_index % 3  
    y = key_index // 3  
    group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((macropad.display.width - 1) * x / 2,
                                                macropad.display.height - 1 -
                                                (3 - y) * 12), 
                             anchor_point=(x / 2, 1.0)))
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))  
group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, -2),
                         anchor_point=(0.5, 0.0)))  
macropad.display.show(group)


output_group = displayio.Group()
for key_index in range(4):
    x = key_index % 1
    y = key_index // 3
    output_group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                            anchored_position=((macropad.display.width - 5) * x / 5,
                                                macropad.display.height - 1 - (3-y)*12),
                            anchor_point=(x/2, 1.0)))# label.Label is used to display something to the screen
output_group.append(Rect(0, 0, macropad.display.width, 8, fill=0xFFFFFF)) # this is for the box at the top
output_group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                        anchored_position=(macropad.display.width//10, -2),
                        anchor_point=(0.5, 0.0)))# this is for the label at the top
macropad.display.show(output_group)

#display the outputs on the left of the screen and the middle of the macroapd screen
input_group=displayio.Group()
for key_index in range(4):
    x = key_index % 2
    y = key_index // 3
    input_group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                            anchored_position=((macropad.display.width - 5) * x / 5,
                                                macropad.display.height - 1 - (3-y)*12 ),
                            anchor_point=(x/2, 1.0)))# label.Label is used to display something to the screen
input_group.append(Rect(0, 0, macropad.display.width, 8, fill=0xFFFFFF)) # this is for the box at the top
input_group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                        anchored_position=(macropad.display.width//10, -2),
                        anchor_point=(0.5, 0.0))) # this is for the label at the top
macropad.display.show(input_group)
    

# input_group=append(label.Label(terminalio.FONT, text='', color=0xFFFFFF, anchored_position=((macropad.display.width-1)* x/2,

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []  # list of all the macrofiles
outputs = []  # we can have a list with one item in it - a list containing one item 
files = os.listdir(MACRO_FOLDER)
# list of all the names in the directory 
files.sort()

for filename in files:
    if filename.endswith('.py') and not filename.startswith('._'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))  # we append the values to the keys 
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)

try:
    output_append = Output.output_dictionary
    outputs.append(output_append) # append all of the values in this file to one position in the outputs list
except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
    IndexError, TypeError) as err:
    print("ERROR in output_dictionary")
    import traceback
    traceback.print_exception(err, err, err.__traceback__)

if not apps and not outputs:
    group[13].text = 'NO MACRO FILES FOUND'
    macropad.display.refresh()
    while True:
        pass
# outputs
last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
index_app = 0  # used to relate to one apps dictionary
apps[index_app].switch() 

index_output=0
outputs[index_output].mapping()

#index_temporary = 0

# MAIN LOOP ----------------------------
# an if statement of the different macropad numbers on switch
while True:
    # assign the dicts from apps and outputs to the macropad encoder position
    
    position = macropad.encoder
    if position != last_position: 
        index_app = position % (len(apps))
        if apps or outputs:
            apps[index_app].switch()
            outputs[index_output].mapping()
        last_position=position
           
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    # macropad.encoder_switch_debounced.pressed is true when the switch is pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch 
        if len(apps[index_app].macros) < 13:
            continue
        key_number = 12
        pressed = encoder_switch 
        event = macropad.keys.events.get() 

        if event.key_number >= len(apps[index_app].macros):
            continue
        key_number = event.key_number  
        pressed = event.pressed  

 
    sequence = apps[index_app].macros[key_number][2]
    if pressed:
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = 0xFFFFFF  
            macropad.pixels.show()      
        for item in sequence:
            if isinstance(item, int): 
                if item >= 0:  
                    macropad.keyboard.press(item)   
                else:
                    macropad.keyboard.release(-item)
            elif isinstance(item, float):
                time.sleep(item)
            elif isinstance(item, str):
                macropad.keyboard_layout.write(item)
            elif isinstance(item, list):
                for code in item:
                    if isinstance(code, int):
                        macropad.consumer_control.release()
                        macropad.consumer_control.press(code)
                    if isinstance(code, float):
                        time.sleep(code)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.press(item['buttons'])
                    else:
                        macropad.mouse.release(-item['buttons'])
                macropad.mouse.move(item['x'] if 'x' in item else 0,
                                    item['y'] if 'y' in item else 0,
                                    item['wheel'] if 'wheel' in item else 0)
                if 'tone' in item:
                    if item['tone'] > 0:
                        macropad.stop_tone()
                        macropad.start_tone(item['tone'])
                    else:
                        macropad.stop_tone()
                elif 'play' in item:
                    macropad.play_file(item['play'])
    else:

        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.release(item)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.release(item['buttons'])
                elif 'tone' in item:
                    macropad.stop_tone()
        macropad.consumer_control.release()
        if key_number < 12:
            macropad.pixels[key_number] = apps[index_app].macros[key_number][0]
            macropad.pixels.show()

            # https://github.com/Sidpatchy/MacroControl/blob/main/code.py
