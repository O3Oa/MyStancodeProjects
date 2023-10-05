"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	with open(FILE, 'r') as f:
		word_d = {}
		for line in f:
			lst = line.split()
			for token in lst:
				token = string_manipulation(token)
				if token in word_d:
					# word_d[token] = word_d[token] + 1
					word_d[token] += 1
				else:
					word_d[token] = 1
		print_out_d(word_d)

def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
					value of type int is the word occurrence
	---------------------------------------------------------------
	This function prints out all the info in d
	"""
	for key, value in d.items():
		print(key, value)


def string_manipulation(token):
	ans = ''
	for ch in token:
		if ch.isalpha() or ch.isdigit():
			ans += ch.lower()
	return ans


if __name__ == '__main__':
	main()
