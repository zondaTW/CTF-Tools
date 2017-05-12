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

def add_content(content, idx, string):
    return content[:idx] + string + content[idx:], idx + len(string)
 
def remove_content(content, idx):
    return content[:idx] + content[idx+1:]
 
def get_current_line_idx(string, idx):
    temp_string_list = string.split('\n')
    for list_idx in range(len(temp_string_list)):
        cuurent_line_num = len(temp_string_list[list_idx]) + 1
        if idx < cuurent_line_num:
            break
        idx -= cuurent_line_num
    return list_idx, idx
     
def up_arrow(string, idx):
    current_line, current_line_idx = get_current_line_idx(string, idx)
    temp_string_list = string.split('\n')
    if current_line != 0:
        up_line_num = len(temp_string_list[current_line-1])
        if current_line_idx < up_line_num:    
            dif = up_line_num + 1
            return idx - dif
        else:
            return idx - (current_line_idx + 1)
    else:
        return idx
 
def down_arrow(string, idx):
    current_line, current_line_idx = get_current_line_idx(string, idx)
    temp_string_list = string.split('\n')
    if current_line != len(temp_string_list)-1:
        down_line_num = len(temp_string_list[current_line+1])
        current_line_num = len(temp_string_list[current_line])
        if current_line_idx < down_line_num:
            dif = current_line_num + 1
            return idx + dif
        else:
            dif = (current_line_num - current_line_idx) + 1 + down_line_num
            return idx + dif
    else:
        return idx
 
def left_arrow(string, idx):
    try:
        string[idx-1]
        idx -= 1
    except:
        pass
    return idx
 
def right_arrow(string, idx):
    try:
        string[idx+1]
        idx += 1
    except:
        pass
    return idx
     
dict_line_control = {
    "<Enter>": "\n",
    "<Tab>": "\t",
    "<Spacebar>": " "
}
 
dict_rm_control = {
    "<Delete>": 0,
    "<Backspace>": 1,
}
 
dict_direction_control = {
    "<UpArrow>": up_arrow,
    "<DownArrow>": down_arrow,
    "<LeftArrow>": left_arrow,
    "<RightArrow>": right_arrow,
}
 
 
ret_content = ''
control_content = ''
content_idx = 0
for char in file_content:
    if control_content:
        control_content += char
        if char == ">":
            if control_content in dict_line_control:
                ret_content += dict_line_control[control_content]
                content_idx += 1
            elif control_content in dict_rm_control:
                content_idx -= dict_rm_control[control_content]
                ret_content = remove_content(ret_content, content_idx)
            elif control_content in dict_direction_control:
                content_idx = dict_direction_control[control_content](ret_content, content_idx)
            else:
                ret_content, content_idx = add_content(ret_content, content_idx, control_content)
            control_content = ""
            print(ret_content[:content_idx] + '|' + ret_content[content_idx:], content_idx)
            print('===========================')
    else:
        if char == "<":
            control_content += char
        else:
            ret_content, content_idx = add_content(ret_content, content_idx, char)
     
            print(ret_content[:content_idx] + '|' + ret_content[content_idx:], content_idx)
            print('===========================')
print(ret_content)
