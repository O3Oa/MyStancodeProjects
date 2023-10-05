"""
File: complement.py
Name: Jessica
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO:
    Build complement DNA strand.
    Check is there right argument to a function, if no argument, return 'DNA strand is missing.'
    Build complement DNA strand, A to T, T to A, C to G, G to C.
    Build all DNA strand, and return the function value.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    if dna == "":  # check is there get the right argument
        return 'DNA strand is missing.'
    else:
        complement = ''
        for i in range(len(dna)):  # check and change for length of dna string times
            ch = dna[i]  # number i in string dna
            if ch == 'A':
                complement = complement + 'T'  # if the word is A, change to T
            elif ch == 'T':
                complement = complement + 'A'  # if the word is T, change to A
            elif ch == 'C':
                complement = complement + 'G'  # if the word is C, change to G
            elif ch == 'G':
                complement = complement + 'C'  # if the word is G, change to C
        return complement  # return this function value to main function


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
