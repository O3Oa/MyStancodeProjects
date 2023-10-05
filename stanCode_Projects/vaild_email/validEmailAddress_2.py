"""
File: validEmailAddress_2.py
Name: Jessica
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  TODO: Only 1 '@' in the str
feature2:  TODO: There is '.' after '@'
feature3:  TODO: There is 'mail' after '@'
feature4:  TODO: Some str before '@' and some str after '@'
feature5:  TODO: Str start with '.' '@' '-' or end with '.' '@' '-'
feature6:  TODO: End with '.tw'/'.com'/'.edu'/'.org'
feature7:  TODO: Length > 30
feature8:  TODO: There is only 1 '@' but there is '.' near by '@'
feature9:  TODO: There is '..' in str, but not in between of two '"'
feature10: TODO: There is '/' '<' '>' '$' '^' '#' in str

Accuracy of your model: TODO:0.8846153846153846
"""

WEIGHT = [
	[0.5],
	[0.5],
	[0.8],
	[2],
	[-10],
	[0.6],
	[-1],
	[-5],
	[-5],
	[-10]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	valid_email = []
	correct_bool = [False] * 13 + [True] * 13
	# print(correct_bool)
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
		# TODO:
		score = 0
		for i in range(10):
			score += feature_vector[i] * WEIGHT[i][0]
		if score > 1:
			valid_email.append(True)
		else:
			valid_email.append(False)
	# print(valid_email)
	correct_num = 0
	for i in range(len(correct_bool)):
		if correct_bool[i] == valid_email[i]:
			correct_num += 1
	accuracy = correct_num / len(correct_bool)
	print(accuracy)
	print(valid_email)


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email and len(maybe_email.split('@')) == 2 else 0

		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@')[1] else 0

		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if 'mail' in (maybe_email.split('@')[1]) else 0

		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if maybe_email.split('@')[0] and \
										 maybe_email.split('@')[1] else 0

		elif i == 4:
			if '.' == maybe_email[0] or '.' == maybe_email[-1] or '-' == maybe_email[0] or '-' == maybe_email[-1]\
				or '@' == maybe_email[0] or '@' == maybe_email[-1]:
				feature_vector[i] = 1
			else:
				feature_vector[i] = 0

		elif i == 5:
			feature_vector[i] = 1 \
				if maybe_email[-3:] == '.tw' or maybe_email[-4:] == '.com' \
				or maybe_email[-4:] == '.org' or maybe_email[-4:] == '.edu' else 0

		elif i == 6:
			feature_vector[i] = 1 if len(maybe_email) > 30 else 0

		elif i == 7:
			if feature_vector[3]:
				feature_vector[i] = 1 if '.' is maybe_email.split('@')[0][-1] \
										 or '.' is maybe_email.split('@')[1][0] else 0

		elif i == 8:
			# feature_vector[i] = 1 if '..' in maybe_email
			if '..' in maybe_email:
				if '"' in maybe_email.split('..')[0] and '"' in maybe_email.split('..')[1]:
					feature_vector[i] = 0
				else:
					feature_vector[i] = 1

		elif i == 9:
			if '\\' in maybe_email or '<' in maybe_email or '>' in maybe_email \
					or '$' in maybe_email or '^' in maybe_email or '#' in maybe_email:
				feature_vector[i] = 1
			else:
				feature_vector[i] = 0

	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	maybe_email_list = []
	with open(DATA_FILE, 'r') as f:
		for line in f:
			maybe_email_list.append(line.strip())
	return maybe_email_list


if __name__ == '__main__':
	main()
