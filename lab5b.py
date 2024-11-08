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
    """Reads the entire contents of a file and returns it as a string."""
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    """Reads the entire contents of a file and returns it as a list of lines without newline characters."""
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]

def append_file_string(file_name, string_of_lines):
    """Appends a string to the end of a file."""
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes each item from a list to a new line in a file."""
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Reads data from one file and writes it to another with line numbers added at the start of each line."""
    with open(file_name_read, 'r') as read_file, open(file_name_write, 'w') as write_file:
        for index, line in enumerate(read_file, start=1):
            write_file.write(f"{index}:{line}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Append string to file1 and print its contents
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    # Write list to file2 and print its contents
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    # Copy file2 to file3 with line numbers and print its contents
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
