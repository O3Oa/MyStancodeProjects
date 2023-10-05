"""
File: name_sq.py (extension)
Name: Jessica
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    TODO:
    Print the string user input, in four mode
    1. general spelling, from left to right
    2. general spelling, from up to down
    3. reverse spelling, from left to right
    4. reverse spelling, from up to down
    1.& 2.use the same first alphabet
    3.use 2.last alphabet to be it's first alphabet
    4.use 1.last alphabet to be it's first alphabet, and use the same alphabet with 3.
    1.2.3.4.can make around to print like a rectangle.
    """
    print('This program prints a name in a square pattern!')
    name = input('Name: ')
    re_name = ''
    for i in range(len(name)):  # make a reverse string user input
        re_name = name[i] + re_name
    print(name)  # just print the string user input
    for i in range(len(name)-2):  # do it length of user input -2 times
        # because the top line and bottom line print out of this loop
        print(name[i+1], end='')  # print from the second alphabet in string name to the second last.
        for j in range(len(name)-2):
            print(' ', end='')  # quantity of space each line is length of name -2 times
        print(re_name[i+1], end='')  # print from the second alphabet in string rename to the second last.
        print('')
    print(re_name)  # just print the reverse name string

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
