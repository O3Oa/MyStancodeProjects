"""
File: adv_permutation.py
Name: Jessica
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	permutation_helper(lst, [], len(lst))


def permutation_helper(lst, current_lst, ans_len):
	if len(current_lst) == ans_len:
		print(current_lst)
	else:
		for num in lst:
			if num in current_lst:
				pass
			else:
				# # Choose
				current_lst.append(num)
				# # Explore
				permutation_helper(lst, current_lst, ans_len)
				# # Un-choose
				current_lst.pop()
				# permutation_helper(lst, current_lst+[num], ans_len)





if __name__ == '__main__':
	main()