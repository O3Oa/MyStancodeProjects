"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""
# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Make new alphabet string.
    Get the alphabet's index in new string, to find the same index in original alphabet string.
    """
    move = int(input('Secret number: '))
    new_a = ALPHABET[26-move:]+ALPHABET[:26-move]
    # print(new_a)
    caesar = str(input("What's the ciphered string?")).upper()
    real = ''
    for i in range(len(caesar)):
        if caesar[i] not in ALPHABET:  # if caesar[i] == '!' or caesar[i] == ' ':
            real += caesar[i]
        for j in range(len(new_a)):
            if caesar[i] == new_a[j]:
                real += ALPHABET[j]
    print(real)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
