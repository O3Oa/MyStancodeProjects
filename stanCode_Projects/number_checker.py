"""
File: number_checker.py
Name: Jessica
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    Find all divisor of the input data(except itself)
    Add up all number we found, and compare the sum is bigger, smaller or equal to the input data.
    If sum of all divisor except itself bigger than input data, is an abundant number.
    If sum of all divisor except itself equal to input data, is a perfect number.
    If sum of all divisor except itself smaller than input data, is a deficient number.

    Print with the following format according number is a abundant number, an perfect number, or a deficient number:
    (1) (input data) is a an abundant number.
    (2) (input data) is a a perfect number.
    (3) (input data) is a a deficient number.
    """
    print('Welcome to the number checker!')
    n = int(input('n: '))
    while n != EXIT:
        d = 1   # find divisor of n test from 1
        ans = 0
        while True:
            if d < n:  # find divisor from 1 to n
                if n % d == 0:  # d is divisor of n
                    ans += d  # add up all divisor of n
                    d += 1  # test next
                else:  # d is not divisor of n
                    d += 1  # test next
            else:
                break
        if ans > n:
            print(str(n) + ' is an abundant number')
        elif ans == n:
            print(str(n) + ' is a perfect number')
        else:
            print(str(n) + ' is an deficient number')
        n = int(input('n= '))
    print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
