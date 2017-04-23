#!/usr/bin/env python

from itertools import count
import string
import subprocess
import sys

import usb_code

if len(sys.argv) < 2:
    print('Usage: filename')
    exit()
try:
    file_content = subprocess.check_output("tshark -r " + sys.argv[1] + " -T fields -e usb.capdata", shell=True).split()
except:
    exit()

dict_usb_code = usb_code.dict_usb_code
keyboard_range = usb_code.keyboard_range
keypad_range = usb_code.keypad_range

trans_content = ''

num_lock = 0
caps_lock = 0

for line in file_content:
    line_list = line.split(':')
    control_code = line_list[0]
    key_code = line_list[2]
    value = ''
    if key_code == '00':
        continue
    if key_code in keyboard_range:
        shift = 0
        if control_code == '20':
            shift = 1
        
        value = dict_usb_code[key_code][shift]
        
        if caps_lock and value in string.letters:
            value = (value.upper() if value in string.lowercase else value.lower())
        if value == "<Enter>":
            value += "\n"
        if value == "<Caps Lock>":
            caps_lock ^= 1

    elif key_code in keypad_range:
        value = dict_usb_code[key_code][num_lock]
        if value == "<Num Lock>" or value == "<Clear>":
            num_lock ^= 1
    trans_content += value



print trans_content
