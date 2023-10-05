"""
File: replace_keyword.py
Name: Jessica
----------------------
This file shows how to replace
old_word with new_word in old_s
by calling replace function
"""


def main():
    old_s = input('Old_s: ')
    old_word = input('Old_word: ')
    new_word = input('New_word: ')
    print(replace(old_s, old_word, new_word))


def replace(old_s, old_word, new_word):
    if old_word not in old_s:
        print('Error!')
    else:
        ans = ""
        i = old_s.find(old_word)
        ans += old_s[:i]
        ans += new_word
        ans += old_s[i+len(old_word):]
        return ans


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
