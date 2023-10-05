"""
File: similarity.py
Name: Jessica
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    """
    # long = str(input('Please give me a DNA sequence to search: ')).upper()
    # short = str(input('What DNA sequence would you like  to match? ')).upper()
    long = 'ATGCCTGATA'
    short = 'TG'
    # print(len(long), len(short))
    match = 0
    best = match
    homology = ''
    for i in range(len(long)-len(short)+1):
        long_part = long[i:i+len(short)]
        # print(long_part)
        match = 0
        for j in range(len(short)):
            if long_part[j] == short[j]:
                match += 1
            if match > best:
                best = match
                homology = long_part
    print(f'The best match is {homology}')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
