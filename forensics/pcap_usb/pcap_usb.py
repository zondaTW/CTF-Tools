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
control_list = usb_code.control_list
keyboard_range = usb_code.keyboard_range
keypad_range = usb_code.keypad_range

trans_content = ''

num_lock = 0
caps_lock = 0

for line in file_content:
    line_list = line.split(':')
    control_code = bin(int('0x'+line_list[0], 16))[2:].rjust(8, '0')
    key_code = line_list[2]
    control_value = ''
    value = ''
    
    shift = 0
    for idx, bin_num in enumerate(reversed(control_code)):
        if bin_num:
            control_value += control_list[idx]
            if control_list[idx] == "<Shift>":
                shift = 1
    
    if not key_code == '00':
        if key_code in keyboard_range:
            value += dict_usb_code[key_code][shift]
            
            if caps_lock and value in string.letters:
                value = (value.upper() if value in string.lowercase else value.lower())
            if value == "<Caps Lock>":
                caps_lock ^= 1

        elif key_code in keypad_range:
            value = dict_usb_code[key_code][num_lock]
            if value == "<Num Lock>" or value == "<Clear>":
                num_lock ^= 1
    trans_content += control_value + value

print(trans_content)
