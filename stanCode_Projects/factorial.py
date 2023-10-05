"""
File: extension1_factioral.py
Name:  Jessica
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	n times n-1 until 1
	"""
	print('Welcome to stanCode factorial master!')
	n = int(input('Give me a number, and I will list the answer of factorial: '))
	while n != EXIT:
		m = n  # next number
		while True:
			if m < 2:
				break
			else:
				m = m-1  # minimum is 1
				n = n * m
		print(str(n))
		n = int(input('Give me a number, and I will list the answer of factorial: '))
	print('- - - - - See ya! - - - - -')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()