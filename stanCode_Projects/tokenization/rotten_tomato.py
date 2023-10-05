"""
File: rotten_tomato.py
Name: Jessica
-------------------------------
This file shows basic AI in classification task:
movie review classification.
First, tokenize the review
Second, count each token and give them corresponding scores
Finally, calculate the score for each word such that we can
predict a movie review by summing over the scores
"""


# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	with open(FILENAME, 'r') as f:
		word_d = {}
		for line in f:
			score, review = line.split(':')
			#  (+1) (-1)
			score = int(score[1:3])
			tokens = review.split()
			for token in tokens:
				token = string_manipulation(token)
				if token not in word_d:
					word_d[token] = score
				else:
					word_d[token] += score
		print(word_d)
	all_d = {'positive': [], 'neutral': [], 'negative': []}
	for word, score in word_d.items():
		if score > 0:
			all_d['positive'].append(word)
		elif score == 0:
			all_d['neutral'].append(word)
		else:
			all_d['negative'].append(word)


def string_manipulation(token):
	ans = ''
	for ch in token:
		if ch.isalpha():
			ans += ch.lower()
	return ans

if __name__ == '__main__':
	main()
