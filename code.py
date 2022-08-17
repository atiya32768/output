# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
A macro/hotkey program for Adafruit MACROPAD. Macro setups are stored in the
/macros folder (configurable below), load up just the ones you're likely to
use. Plug into computer's USB port, use dial to select an application macro
set, press MACROPAD keys to send key sequences and other USB protocols.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

from curses import KEY_ENTER
import os
import time
import sys
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'


# CLASSES AND FUNCTIONS ----------------
# this class seems random 
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

    input=read_line("input.txt")  
    output=read_line("output.txt")
    result_on_screen=list(zip(input, output))
    result_on_screen='\n'.join(map(str,result_on_screen))
    result_on_screen=tuple(result_on_screen)

    with open("final_output.txt", 'w') as final_file:
        print(result_on_screen)
        sys.stdout=final_file
        final_file.close()
class Output:
    #define some functions in relation to output.txt
    #edit to make it clear it's a txt file
    # have a function that 
    #the file contains commands and output as strings and numbers
    #everytime an instance of this class is created, this function is called
    def __init__(self):
        self.name="final_output.txt"  #name of the txt file 

    def switch(self): # switching between the different files 
        group[13].text=self.name
        macropad.display.refresh()
        macropad.pixels.show()

class App:
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']

    def switch(self):
        """ Activate application settings; update OLED labels and LED
            colors. """
        group[13].text = self.name   # Application name
        for i in range(12):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
                group[i].text = ''
                
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        #macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()

# INITIALIZATION -----------------------

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

# Set up displayio group with all the labels
group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((macropad.display.width - 1) * x / 2,
                                                macropad.display.height - 1 -
                                                (3 - y) * 12),
                             anchor_point=(x / 2, 1.0)))     #label.Label is used to display something to the screen
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, -2),
                         anchor_point=(0.5, 0.0)))
macropad.display.show(group)
# Load all the macro key setups from .py files in MACRO_FOLDER
apps = [] #list of all the macrofiles
outputs= [] # we can have a list with one item in it
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py') and not filename.startswith('._'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app)) # we append the values to the keys 
            # we  append all of the key values from each file in the macrofile to the apps list
            # try to append values to the screen without assigning values to the screen
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)
    # we don't need to append, we just need to display a screen on the macropad for it
    if filename.endswith('.txt') and filename.startswith('final_output'): 
        try:
            output_append = __import__(MACRO_FOLDER + '/' + filename[:-3])
            outputs.append(Manager(output_append.final_file)) #append all of the values in this file to one position in the outputs list
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
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
index_app = 0
apps[index_app].switch() #the OLED lights and label are assigned using switch
total_list=apps+outputs
total_list[index_app].switch()
# MAIN LOOP ----------------------------

while True:
    # Read encoder position. If it's changed, switch apps and outputs interchangeably
    position = macropad.encoder 
    if position != last_position: # the number on the macropad encoder divided by the number of macrofiles results is 0, so we are making a correspondence between the macropad.encoder and the position of a macrofile in the folder
        index_app = position % (len(total_list)) # the position of the key in the apps list is the remainder on dividing the number on the macropad encoder switch by the total number of elements in the apps list
        if apps: # if we have the apps elements in the the total list, we perform the switch operation
            total_list[index_app].switch() # only switches the contents of the apps_list
        last_position=position
        
    # switch what is to be the first element of the apps list
    # if the macropad encoder has changed, we switch the apps list, as different apps are assigned to different key commands 
    # Handle encoder button. If state has changed, and if there's a
    # corresponding macro, set up variables to act on this just like
    # the keypad keys, as if it were a 13th key/macro.

    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch 
        if len(apps[index_app].macros) < 13: #there are less than 13 macrobuttons stored in the apps list
            continue    # No 13th macro, just resume main loop
        key_number = 12 # else process below as 13th macro 
        pressed = encoder_switch
        event = macropad.keys.events.get()
        # edit this part
        if event.key_number >= len(apps[index_app].macros): # if you don't press a key or if your macro file (code) contains an extra key (out of bounds),we ignore it - sorting out possible errors
        # No key events, or no corresponding macro, resume loop
            continue
        key_number = event.key_number  # key number will be the equal to the key number chosen
        pressed = event.pressed  # the event (specific key) is pressed
        if not event:
            
            # then we have an output.txt file
            # we don't have any keys pressed
            # we just output the result to the screen



    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    #the encoder button being pressed is what the code is predicated on
    sequence = apps[index_app].macros[key_number][2]
    if pressed:
        # 'sequence' is an arbitrary-length list, each item is one of:     #Assigning different actions to different types
        # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
        # Negative integer: (absolute value) key released
        # Float (e.g. 0.25): delay in seconds
        # String (e.g. "Foo"): corresponding keys pressed & released
        # List []: one or more Consumer Control codes (can also do float delay)
        # Dict {}: mouse buttons/motion (might extend in future)
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = 0xFFFFFF  # assigns a colour to each key on the macropad
            macropad.pixels.show()      # displays the colour on the key
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
        # Release any still-pressed keys, consumer codes, mouse buttons
        # Keys and mouse buttons are individually released this way (rather
        # than release_all()) because pad supports multi-key rollover, e.g.
        # could have a meta key or right-mouse held down by one macro and
        # press/release keys/buttons with others. Navigate popups, etc.
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
        if key_number < 12: # No pixel for encoder button
            macropad.pixels[key_number] = apps[index_app].macros[key_number][0]
            macropad.pixels.show()

    #output is stored in final file

#come up with some seperate functionality
 #create a class to store the input of the keys-later
#we want to store the content of the final_file into the list outputs anduse that to print it out onto the screen

