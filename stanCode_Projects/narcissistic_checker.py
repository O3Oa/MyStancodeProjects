"""
File: narcissistic_checker.py
Name: Jessica
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
    """
    figure out how many digits of the input
    apart all digits and make power, and then add it up
    compare the sum and itself
    if equal to itself, the input data is a narcissistic number
    if not, the input data is not a narcissistic number
    """
    print('Welcome to the narcissistic number checker!')
    n = int(input('n: '))
    while n != EXIT:
        p = 0  # power,find how many digits of the input
        while n > 10 ** p:
            p += 1

        ans = 0
        m = n  # each digits number
        for i in range(p):
            ans += (m % 10) ** p  # find digit, ten digit, hundreds digit and so on
            m = m // 10

        if ans == n:
            print(str(n) + ' is a narcissistic number')
        else:
            print(str(n) + ' is not a narcissistic number')
        n = int(input('n: '))
    print('Have a good one!')


if __name__ == '__main__':
    main()
