"""
File: rocket.py
Name: Jessica
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
    """
    TODO:
    Write a program can make every customized size rocket!
    Dismantle the rocket into several parts.(head/belt/upper/lower)
    make SIZE = S rocket for standard
    head:
        consists of 'space' 'forward slash' 'backslash'
            quantity of 'space' is S - 1 /each line
            quantity of 'forward slash' is the index of row + 1/each line
            quantity of 'backslash' is the index of row +1/each line
    belt:
        consists of '+' '='
            quantity of '+' is one on the leftest,and one on the rightest
            quantity of '=' is s*2
    upper:
        consists of '|' '.' '/\'
            quantity of '|' is one on the leftest,and one on the rightest
            quantity of left '.' is s - the index of row - 1
            quantity of '/\' is the index of row + 1
            quantity of right '.' is s - the index of row - 1
    lower:
        consists of '|' '.' '\/'
            quantity of '|' is one on the leftest,and one on the rightest
            quantity of left '.' is s
            quantity of '\/' is s - the index of row
            quantity of right '.' is s

    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):  # quantity of row == SIZE
        for j in range(SIZE - i):  # quantity of '' is SIZE - index of row
            print(' ', end='')  # space
        for j in range(i + 1):  # quantity of '/' is index of row + 1
            print('/', end='')
        for j in range(i + 1):  # quantity of '\' is index of row + 1
            print('\\', end='')  # to print '\' have to type two
        print('')


def belt():
    print('+', end='')  # fixed print, not related to any variable
    for i in range(SIZE * 2):  # quantity of '=' is SIZE * 2
        print('=', end='')
    print('+')  # fixed print, not related to any variable


def upper():
    for i in range(SIZE):  # quantity of row == SIZE
        print('|', end='')  # fixed print, not related to any variable
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(i + 1):
            print('/\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        print('|')  # fixed print, not related to any variable


def lower():
    for i in range(SIZE):  # quantity of row == SIZE
        print('|', end='')  # fixed print, not related to any variable
        for j in range(i):
            print('.', end='')
        for j in range(SIZE - i):
            print('\\/', end='')
        for j in range(i):
            print('.', end='')
        print('|')  # fixed print, not related to any variable


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
