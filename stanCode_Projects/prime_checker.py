"""
File: prime_checker.py
Name: Jessica
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

import math

EXIT = -100


def main():
	"""
	Find the number to divide exactly the input data from 2 # all number can divide by 1
	to the square root of the input data # no more possibility can find if no fount any number in this range
	if can't found any divisor, the input data is a prime number
	if found one or more divisor, the input data is not a prime number

	Print with the following format according number is prime or not
	(input data) is not a prime number.
	(input data) is a prime number.
	"""

	print('Welcome to the prime checker!')
	n = int(input('n= '))
	while n != EXIT:
		candidate = 2
		sqrt_n = math.sqrt(n)  # square root of n
		while True:
			if candidate <= sqrt_n:  # find 2 to square root of n
				if n % candidate != 0:  # not divisor of n
					candidate += 1  # test next
				else:
					print(str(n) + ' is not a prime number.')
					break
			else:
				print(str(n) + ' is a prime number')
				break
		n = int(input('n= '))
	print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
