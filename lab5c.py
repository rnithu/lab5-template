#!/usr/bin/env python3

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

# Author: Nithurshan Raveendran
# Author ID: 188141212
# Date Created: 2024/11/08

#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    """Add two numbers together. Returns the result, or an error message if addition fails."""
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    """Reads a file and returns a list of all lines. Returns an error message if reading fails."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))               # Expected: 15
    print(add('10', 5))             # Expected: 15
    print(add('abc', 5))            # Expected: 'error: could not add numbers'
    print(read_file('seneca2.txt')) # Expected: List of lines if file exists
    print(read_file('file10000.txt')) # Expected: 'error: could not read file'
