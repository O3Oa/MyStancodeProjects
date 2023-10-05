"""
File: quadratic_solver.py
Name: Jessica
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    Find the root of equation defined by user

    Print with the following format
    (1) 'No real roots': if the discriminant less than zero
    (2) 'One root: root': if the discriminant equal to zero
    (3) 'Two roots: root1, root2': if the discriminant greater than zero
    """
    print('stanCode QuadraticSolver!')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    d = b * b - 4 * a * c  # discriminant
    if d < 0:
        print('No real roots')
    elif d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)  # First root
        if d == 0:
            print('One root: ' + str(x1))
        else:
            x2 = (-b - math.sqrt(d)) / (2 * a)  # Second root
            print('Two root: ' + str(x1) + ' , ' + str(x2))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
