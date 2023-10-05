"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}
	######################
	with open(FILE, 'r') as f:
		for line in f:
			student_info_lst = line.split()
			all_d[student_info_lst[0]] = {
				'AGE': student_info_lst[1],
				'EMAIL':student_info_lst[2],
				'FOOD':student_info_lst[3:]
			}

			# name = student_info_lst[0]
			# age = student_info_lst[1]
			# email = student_info_lst[2]
			# food = student_info_lst[3:]
			# d_student = {} # 0xABC, 0XBBC, 0X456,...
			# print(hex(id(d_student)))
			# d_student['AGE'] = age
			# d_student['EMAIL'] = email
			# d_student['FOOD'] = food
			# all_d[name] = d_student
	######################
	print_out_d(all_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is the name of student
				value of type dict is the info of the student
	---------------------------------------------------------------
	This function prints out a nested data structure on console
	"""
	for student, student_info in d.items():
		print(student)
		print(student_info)
		print('-'*50)




if __name__ == '__main__':
	main()