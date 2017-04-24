#/usr/bin/env python

import sys


if len(sys.argv) < 2:
    print('Usage: filename')
    exit()
file_name = sys.argv[1]

file_content = ''
with open(file_name, 'r') as f:
    for line in f:
        file_content += line

dict_control = {
    "<Enter>": "\n",
    "<Tab>": "\t",
    "<Spacebar>": " "
}

ret_content = ''
control_content = ''
for char in file_content:
    if control_content:
        control_content += char
        if char == ">":
            if control_content in dict_control:
                ret_content += dict_control[control_content]
            elif control_content == "<Backspace>":
                ret_content = ret_content[:-1]
            else:
                ret_content += control_content
            control_content = ""
    else:
        if char == "<":
            control_content += char
        else:
            ret_content += char


print(ret_content)
