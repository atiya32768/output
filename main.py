
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import terminalio
from adafruit_display_text import label
from adafruit_macropad import MacroPad
macropad=MacroPad()

#need to print this out only if you press a specific button
# text is the function used to display something onto the screen
text = "Hello world"
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 10
text_area.y = 10
#board.DISPLAY.show(text_area)
while True:
    key_event=macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            if macropad.encoder==0 or macropad.encoder%5==0:
                if key_event.key_number==3:
                    board.DISPLAY.show(text_area)
            elif macropad.encoder==2 or macropad.encoder %5==2:
                if key_event.key_number==3:
                    board.DISPLAY.show(text_area)
            else:
                if macropad.encoder==2 or macropad.encodeer %5==4:
                    if key_event.key_number==3:
                        board.DISPLAY.show(text_area)

                