"""
File: anagram.py
Name: Jessica
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    # s = input('Find anagram for: ')
    dic = read_dictionary()
    while True:
        s = input('Find anagram for: ')
        start = time.time()
        if s != EXIT:
            all_case = find_anagrams(s, dic)
            # s = input('Find anagram for: ')
            print(str(len(all_case)) + ' anagram: ', end='')
            print(all_case)
        else:
            break
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    dic = []
    with open(FILE, 'r') as f:
        for line in f:
            dic += [line.strip()]
    return dic


def find_anagrams(s, dic):
    all_case = []
    print('Searching...')
    find_anagrams_helper(s, '', all_case, s, dic)
    anagrams = []
    for word in all_case:
        if word in dic:
            anagrams.append(word)
    return anagrams


def find_anagrams_helper(s, current_s, all_case, candidate_s, dic):
    if len(current_s) == len(s):
        if current_s not in all_case:
            all_case += [current_s]
            print('Found ' + str(current_s))
            print('Searching...')
    else:
        for i in range(len(candidate_s)):
            # Choose
            current_s += candidate_s[i]
            if has_prefix(current_s, dic):
                # Explores
                find_anagrams_helper(s, current_s, all_case, candidate_s[:i]+candidate_s[i+1:], dic)
            # Un-choose
            current_s = current_s[:-1]


def has_prefix(sub_s, dic):
    for word in dic:
        if sub_s[0] == word[0]:
            if word.startswith(sub_s):
                return True
        elif sub_s[0] < word[0]:
            break
    return False


if __name__ == '__main__':
    main()
