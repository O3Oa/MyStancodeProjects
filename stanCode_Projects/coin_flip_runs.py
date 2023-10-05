"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:
	"""
	print("Let's flip a coin!")
	n = int(input('Number of run: '))
	pre_coin = None
	run = 0
	was_continue = False
	is_continue = False
	coinseq = ''
	while run < n:
		coin = coin_side()
		if coin == pre_coin:
			is_continue = True
		else:
			is_continue = False
		if is_continue == True and was_continue == False:
			run += 1
		was_continue = is_continue

		pre_coin = coin
		coinseq += coin
	print(coinseq)



def coin_side():
	if r.randint(1, 2) == 1:
		return 'H'
	else:
		return 'T'


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
