#!/usr/bin/env python

import pprint
from itertools import count
import string

# http://www.usb.org/developers/hidpage/Hut1_12v2.pdf  page.53

lower_str = string.ascii_lowercase
upper_str = string.ascii_uppercase
digits_str = "1234567890"
punctuation_str1 = "!@#$%^&*()"
punctuation_str2 = "-=[]\#;'`,./"
punctuation_str3 = '_+{}|:"~<>?'

sepcific_str = [
    "<Enter>", 
    "<Escape>", 
    "<Backspace>", 
    "<Tab>",
    "<Spacebar>"]

special_str = [
    "<Caps Lock>"
]
special_str.extend(["<F{}>".format(str(num)) for num in xrange(1, 13)])
special_str.extend([
    "<Print Screen>",
    "<Scroll Lock>",
    "<Pause>",
    "<Insert>",
    "<Home>",
    "<PageUp>",
    "<Delete Forward>",
    "<End>",
    "<PageDown>",
    "<RightArrow>",
    "<LeftArrow>",
    "<DownArrow>",
    "<UpArrow>"
])

keypad_str = [
    "<Num Lock>",
    "/",
    "*",
    "-",
    "+",
    "<Enter>",
]

keypad_str2 = ["<Clear>"] + keypad_str[1:]

keypad_str3 = digits_str + '.'

keypad_str4 = [
    "<End>",
    "<DownArrow>",
    "<PageDn>",
    "<LeftArrow>",
    "5",
    "<RightArrow>",
    "<Home>",
    "<UpArrow>",
    "<PageUp>",
    "<Insert>",
    "<Delete>"
]


dict_usb_code = {}

def add_dict_2_string(start_num, add_string1, add_string2):
    for idx, value1, value2 in zip(count(start_num), add_string1, add_string2):
        dict_usb_code[hex(idx)[2:].rjust(2, '0')] = [value1, value2]

def add_dict_1_string(start_num, add_string1):
    for idx, value in enumerate(add_string1, start_num):
        dict_usb_code[hex(idx)[2:].rjust(2, '0')] = [value]


keyboard_range = map(lambda s: hex(s)[2:].rjust(2, '0'), xrange(0x4, 0x53))
keypad_range = map(lambda s: hex(s)[2:].rjust(2, '0'), xrange(0x53, 0x64))

# 0x04 ~ 0x27
add_dict_2_string(0x4, lower_str+digits_str, upper_str+punctuation_str1)
# 0x28 ~ 0x2c
add_dict_2_string(0x28, sepcific_str, special_str)
# 0x2d ~ 0x38
add_dict_2_string(0x2d, punctuation_str2, punctuation_str3)
# 0x39 ~ 0x52
add_dict_2_string(0x39, special_str, special_str)
# 0x53 ~ 0x58
add_dict_2_string(0x53, keypad_str, keypad_str2) 
# 0x59 ~ 0x63
add_dict_2_string(0x59, keypad_str3, keypad_str4)

if __name__ == "__main__":
    pprint.pprint(dict_usb_code)


