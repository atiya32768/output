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

class App:
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']
    
    def getname(self):
        return self.name
    #list of commands
    # a way to return the specific command pressed
    #passing the output as info
    # we are passing a list to the function
    
    
    def mapping(self):
        #group[0].text="hello world"
        for x in range(len(info)):
            group[x].text=self.info[x]

        macropad.display.refresh()
        macropad.pixels.show()
        
    def set_info(self,info):
        self.info=info
        self.mapping()
    


        #  for x in self.output_dictionary.keys():
        #     macropad.pixels[x]=self.output_dictionary_keys[x]
        #     output_group[x].text=self.output_dictionary_keys[x]

    #     macropad.display.refresh()
    #     macropad.pixels.show()

    #     for y in self.output_dictionary.values():
    #         macropad.pixels[y] = self.output_dictionary_values[y]
    #         input_group[y].text = self.output_dictionary_keys[y]

    #     macropad.display.refresh()
    #     macropad.pixels.show()

    def switch(self):
        group[13].text = self.name.upper()  # Application name
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
        macropad.stop_tone()
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
                             anchor_point=(x / 2, 1.0)))
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
group.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, -2),
                         anchor_point=(0.5, 0.0)))
macropad.display.show(group)


# if we add this the pixels do not show

# for key_index in range(1):
#     x = key_index % 1
#     y = key_index // 3
#     output_group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
#                             anchored_position=((macropad.display.width - 5) * x / 5,
#                                                 macropad.display.height - 1 - (3-y)*12),
#                             anchor_point=(x/2, 1.0)))# label.Label is used to display something to the screen
# output_group.append(Rect(0, 0, macropad.display.width, 8, fill=0xFFFFFF)) # this is for the box at the top
# output_group.append(label.Label(terminalio.FONT, text='', color=0x000000,
#                         anchored_position=(macropad.display.width//10, -2),
#                         anchor_point=(0.5, 0.0)))# this is for the label at the top
# macropad.display.show(output_group)

# #display the outputs on the left of the screen and the middle of the macroapd screen
# input_group=displayio.Group()
# for key_index in range(4):
#     x = key_index % 2
#     y = key_index // 3
#     input_group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
#                             anchored_position=((macropad.display.width - 5) * x / 5,
#                                                 macropad.display.height - 1 - (3-y)*12 ),
#                             anchor_point=(x/2, 1.0)))# label.Label is used to display something to the screen
# input_group.append(Rect(0, 0, macropad.display.width, 8, fill=0xFFFFFF)) # this is for the box at the top
# input_group.append(label.Label(terminalio.FONT, text='', color=0x000000,
#                         anchored_position=(macropad.display.width//10, -2),
#                         anchor_point=(0.5, 0.0))) # this is for the label at the top
# macropad.display.show(input_group)



# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py') and not filename.startswith('._'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)
    
if not apps:
    group[13].text = 'NO MACRO FILES FOUND'
    macropad.display.refresh()
    while True:
        pass

last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
apps[app_index].switch()




# MAIN LOOP ----------------------------

while True:
    position = macropad.encoder
    app_index = position % len(apps)
    if position != last_position:
        #app_index = position % len(apps)
        
        apps[app_index].switch()
        last_position=position
        #last_position=position
    current_app=apps[app_index]


    info=[] # append an input with an output from the output list
    file=open("macros/output.txt", "r")
    lines=file.readlines()
    for line in range(len(lines)):
        info.append(lines[line].strip('\n'))
    

    # we have the specific command from the keyboard

    # print(input)
    
    # info=[] # append an input with an output from the output list
    # file=open("macros/output.txt", "r")
    # lines=file.readlines()
    # for line in range(len(lines)):
    #     info.append(lines[line].strip('\n'))
    
    #current_app.set_info(info.mapping)
    # info.mapping()

    # we are passing the info list and assigning it to test

    # output_dictionary={}
    # output=current_app.getname()
    # output_dictionary[output]={}
    # output_dictionary[output][input]=output
    # print(output_dictionary)
    # output_dictionary.mapping()
    
    # we have the current command
    #print(current_app.getname()) # name of current macro file

    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        if len(apps[app_index].macros) < 13:
            continue   
        key_number = 12 
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            continue # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed # we have pressed the key 


    # we have that the key is pressed
    # we need to edit this so that if the key is pressed, we do something
    # arbitary length list 
    
        # create some conditions to output the result
    sequence = apps[app_index].macros[key_number][2]
    if pressed:
        # 'sequence' is an arbitrary-length list, each item is one of:
        # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
        # Negative integer: (absolute value) key released
        # Float (e.g. 0.25): delay in seconds
        # String (e.g. "Foo"): corresponding keys pressed & released
        # List []: one or more Consumer Control codes (can also do float delay)
        # Dict {}: mouse buttons/motion (might extend in future)
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
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
    # once we have pressed action 

  
    # if encoder_switch:
    current_app.set_info(info)
    




















        