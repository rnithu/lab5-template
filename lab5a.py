#!/usr/bin/env python3

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/11/08

def read_file_string(file_name):
    """Takes file_name as a string, returns its entire contents as a string."""
    with open(file_name, 'r') as file:
        return file.read()  # Reads the entire content as a single string

def read_file_list(file_name):
    """Takes file_name as a string, returns its entire contents as a list of lines without new-line characters."""
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]  # Reads lines and removes newline characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
