"""
File: triangular_checker.py
Name: Jessica
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Subtract the number from 1 step 1, until the difference not less than zero,
    and determine if the difference equal to zero or not.
    If the difference equal to zero, the input data is a triangular number.
    If the difference can't equal to zero, the input data is not a triangular number.
    """
    print('Welcome to the triangular number checker!')
    n = int(input('n= '))
    while n != EXIT:
        t = 1  # minuend from 1
        m = n
        while True:
            if m > 0:  # difference not less than 0
                m = m - t  # difference
                t += 1  # minus next number
            else:
                break
        if m == 0:
            print(str(n) + ' is a triangular number ')
        else:
            print(str(n) + ' is not a triangular number')
        n = int(input('n= '))
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
