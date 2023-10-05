"""
File: validEmailAddress.py
Name: Jessica
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: TODO:0.6538461538461539
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
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
		if score > 0:
			valid_email.append(True)
		else:
			valid_email.append(False)
	correct_num = 0
	for i in range(len(correct_bool)):
		if correct_bool[i] == valid_email[i]:
			correct_num += 1
	accuracy = correct_num / len(correct_bool)
	print(accuracy)


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with 10 values of 0's or 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
		###################################
		elif i == 2:
			if feature_vector[0]:
				feature_vector[i] = 1 if len(maybe_email.split('@')[0]) > 0 else 0

		elif i == 3:
			if feature_vector[0]:
				feature_vector[i] = 1 if len(maybe_email.split('@')[1]) > 0 else 0

		elif i == 4:
			num_of_at = maybe_email.split('@')
			if '.' in maybe_email.split('@')[-1] and len(num_of_at) == 2:
				feature_vector[i] = 1
			else:
				feature_vector[i] = 0

		elif i == 5:
			feature_vector[i] = 1 if ' ' not in maybe_email else 0

		elif i == 6:
			if '.com' in maybe_email and len(maybe_email.split('.com')[1]) == 0:
				feature_vector[i] = 1

		elif i == 7:
			if '.edu' in maybe_email and len(maybe_email.split('.edu')[1]) == 0:
				feature_vector[i] = 1

		elif i == 8:
			feature_vector[i] = 1 if maybe_email[-3:] == '.tw' else 0

		elif i == 9:
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0
		###################################
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that might be valid email addresses
	"""
	maybe_email_list = []
	with open(DATA_FILE, 'r') as f:
		for line in f:
			maybe_email_list.append(line)
	return maybe_email_list

if __name__ == '__main__':
	main()
