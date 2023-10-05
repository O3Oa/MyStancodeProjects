"""
File: hailstone.py
Name: Jessica
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

def main():
    """
    1.determine the termination conditions
    2.
    3.
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    counter = 0
    while n != 1:
        counter += 1
        if n % 2 == 0:
            print(int(input(str(n) + " is even, so I take half: "+str(n/2))))
            n = (n/2)
        else:
            print(int(input(str(n) + " is odd, so I make 3n+1: "+str((n*3)+1))))
            n = (n*3) + 1
    print('It took 0 steps to reach 1.')


def main_j():
    """
    Find the Hailstone Sequence from the number defined by user to 1
    (1) Detect the number is ood or even
    (2) Calculate the next number in Hailstone Sequence
    (3) Count step2 programming how many times

    Print with the following format according number is even, odd, or 1:
    (1) 'n is ood, so I make 3n+1: 3n+1'
    (2) 'n is even, so I make take half: n/2'
    (3) 'It took  steps to reach 1.'
    """
    print('This program computes Hailstone sequences')
    n = int(input('Enter a number: '))
    counter = 0  # counter for steps
    while n != 1:
        if n % 2 == 1:
            # n is odd
            print(str(n) + ' is odd, so I make 3n+1: ', end="")
            n = 3 * n + 1
        else:
            # n is even
            print(str(n) + ' is even, so I make take half: ', end="")
            n = n / 2
        print(str(int(n)))
        counter += 1
    print('It took ' + str(counter) + ' steps to reach 1.')

    # n = int(input('Enter a number: '))
    # counter = 0
    # while n != 1:
    #     if n % 2 == 1:
    #         print(str(int(n)) + ' is odd, so I make 3n+1: ', end="")
    #         n = 3 * n + 1
    #         print(str(int(n)))
    #         counter += 1
    #     if n % 2 == 0:
    #         print(str(int(n)) + ' is even, so I make take half: ', end="")
    #         n = n / 2
    #         print(str(int(n)))
    #         counter += 1
    # print('It took ' + str(counter) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
