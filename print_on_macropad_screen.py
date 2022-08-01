from adafruit_macropad import MacroPad
macropad = MacroPad()
#if you press as specific button
#the commands you press will show on screen
#automatically saves

with open('output.txt', "a") as f: 
    while True:
        key_event = macropad.keys.events.get()
        if key_event and key_event.pressed:
            continue
        if macropad.encoder == 0 or macropad.encoder % 5 == 0:
            f.write("Encoder: {}".format(macropad.encoder), file=f)
            f.write("Key pressed: {}".format(key_event.key_number), file=f)
            if key_event.key_number == 0:
                f.write("N/A", file=f)
            elif key_event.key_number == 1:
                f.write("CURRENT", file=f)
            elif key_event.key_number == 2:
                f.write("N/A", file=f)
            elif key_event.key_number == 3:
                f.write("N/A", file=f)
            elif key_event.key_number == 4:
                f.write("POWER", file=f)
            elif key_event.key_number == 5:
                f.write("N/A", file=f)
            elif key_event.key_number == 6:
                f.write("N/A", file=f)
            elif key_event.key_number == 7:
                f.write("=", file=f)
            elif key_event.key_number == 8:
                f.write("N/A", file=f)
            elif key_event.key_number == 9:
                f.write("N/A", file=f)
            elif key_event.key_number == 10:
                f.write("ENTER", file=f)
            else:
                f.write("N/A", file=f)
        if key_event and key_event.pressed:
            continue
        if macropad.encoder == 1 or macropad.encoder % 5 == 1:
            f.write("Encoder: {}".format(macropad.encoder))
            f.write("Key pressed: {}".format(key_event.key_number))
            if key_event.key_number == 0:
                f.write("7", file=f)
            elif key_event.key_number == 1:
                f.write("8", file=f)
            elif key_event.key_number == 2:
                f.write("9", file=f)
            elif key_event.key_number == 3:
                f.write("4", file=f)
            elif key_event.key_number == 4:
                f.write("5", file=f)
            elif key_event.key_number == 5:
                f.write("6", file=f)
            elif key_event.key_number == 6:
                f.write("1", file=f)
            elif key_event.key_number == 7:
                f.write("2", file=f)
            elif key_event.key_number == 8:
                f.write("3", file=f)
            elif key_event.key_number == 9:
                f.write("*", file=f)
            elif key_event.key_number == 10:
                f.write("0", file=f)
            else:
                f.write("#")
        if key_event and key_event.pressed:
            continue
        if macropad.encoder == 2 or macropad.encoder % 5 == 2:
            f.write("Encoder: {}".format(macropad.encoder))
            f.write("Key pressed: {}".format(key_event.key_number))
            if key_event.key_number == 0:
                f.write("N/A", file=f)
            elif key_event.key_number == 1:
                f.write("N/A", file=f)
            elif key_event.key_number == 2:
                f.write("N/A", file=f)
            elif key_event.key_number == 3:
                f.write("N/A", file=f)
            elif key_event.key_number == 4:
                f.write("ON", file=f)
            elif key_event.key_number == 5:
                f.write("N/A", file=f)
            elif key_event.key_number == 6:
                f.write("N/A", file=f)
            elif key_event.key_number == 7:
                f.write("OFF", file=f)
            elif key_event.key_number == 8:
                f.write("N/A", file=f)
            elif key_event.key_number == 9:
                f.write("N/A", file=f)
            elif key_event.key_number == 10:
                f.write("ENTER", file=f)
            else:
                f.write("0", file=f)
        if key_event and key_event.pressed:
            continue
        if macropad.encoder == 3 or macropad.encoder % 5 == 3:
            f.write("Encoder: {}".format(macropad.encoder))
            f.write("Key pressed: {}".format(key_event.key_number))
            if key_event.key_number == 0:
                f.write("LTEMP", file=f)
            elif key_event.key_number == 1:
                f.write("DTEMP", file=f)
            elif key_event.key_number == 2:
                f.write("CTEMP", file=f)
            elif key_event.key_number == 3:
                f.write("N/A", file=f)
            elif key_event.key_number == 4:
                f.write("N/A", file=f)
            elif key_event.key_number == 5:
                f.write("N/A", file=f)
            elif key_event.key_number == 6:
                f.write("ACT", file=f)
            elif key_event.key_number == 7:
                f.write("N/A", file=f)
            elif key_event.key_number == 8:
                f.write("SET", file=f)
            elif key_event.key_number == 9:
                f.write("=", file=f)
            elif key_event.key_number == 10:
                f.write("ENTER", file=f)
            else:
                f.write("?", file=f)
        if key_event and key_event.pressed:
            continue
        if macropad.encoder == 4 or macropad.encoder % 5 == 4:
            f.write("Encoder: {}".format(macropad.encoder))
            f.write("Key pressed: {}".format(key_event.key_number))
            if key_event.key_number == 0:
                f.write("N/A", file=f)
            elif key_event.key_number == 1:
                f.write("VOAGOTO", file=f)
            elif key_event.key_number == 2:
                f.write("N/A", file=f)
            elif key_event.key_number == 3:
                f.write("N/A", file=f)
            elif key_event.key_number == 4:
                f.write("MIN", file=f)
            elif key_event.key_number == 5:
                f.write("N/A", file=f)
            elif key_event.key_number == 6:
                f.write("N/A", file=f)
            elif key_event.key_number == 7:
                f.write("MAX", file=f)
            elif key_event.key_number == 8:
                f.write("N/A", file=f)
            elif key_event.key_number == 9:
                f.write("N/A", file=f)
            elif key_event.key_number == 10:
                f.write("ENTER", file=f)
            else:
                f.write("N/A", file=f)
        # button 1 and switch is pressed together
        if key_event.key_number==1 and macropad.encoder_switch==True:
            f.close()
        # we close the file