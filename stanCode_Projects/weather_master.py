"""
File: weather_master.py
Name: Jessica
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -10


def main():
	"""
	Figure out the target information from user's all input data
	When Users input new data, do following determine and calculate at the same time
	(1)Highest temperature
		When input new data, compare the new data with old, the bigger one is the Highest.
	(2)Lowest temperature
		When input new data, compare the new data with old, the smaller one is the Lowest.
	(3)Average temperature
		Add up all input data and then divide to how many data user input
	(4)Cold days
		When input new data, determine is it smaller than 16, if yes, counter plus one

	Print with the following format:
	(1)Highest Temperature = (biggest date)
	(2)Lowest Temperature = (smallest data)
	(3)Average = (total/times)
	(4)(how many) cold day(s)
	"""
	print('stanCode "Weather master 4.0"!')
	n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if n == EXIT:
		print('No Data')
	else:
		maximum = n
		minimum = n
		counter = 1
		total = n
		counter2 = 0
		if n < 16:
			counter2 += 1
		while True:
			n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if n == EXIT:
				break
			if n > maximum:
				maximum = n
			if n < minimum:
				minimum = n
			if n < 16:
				counter2 += 1
			total += n
			counter += 1

		ave = total / counter

		print('Highest Temperature = ' + str(maximum))
		print('Lowest Temperature = ' + str(minimum))
		print('Average = ' + str(ave))
		print(str(counter2) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
