"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = str(-1)


def main():
    """
    TODO:
    """
    n = str(input('Which class? '))

    count1 = 0
    count2 = 0
    if n == EXIT:
        print('No class score were entered')
    else:
        while n != EXIT:  #分類
            if n.upper() == str('SC001'):  #統計這個班的成績
                s1 = int(input('Score: '))
                if count1 == 0:
                    maximum1 = s1
                    minimum1 = s1
                    count1 += 1
                    total1 = s1
                else:
                    if s1 > maximum1:
                        maximum1 = s1
                    if s1 < minimum1:
                        minimum1 = s1
                    count1 += 1
                    total1 += s1

            else:
                s2 = int(input('Score: '))
                if count2 == 0:
                    maximum2 = s2
                    minimum2 = s2
                    count2 += 1
                    total2 = s2
                else:
                    if s2 > maximum2:
                        maximum2 = s2
                    if s2 < minimum2:
                        minimum2 = s2
                    count2 += 1
                    total2 += s2
            n = str(input('Which class? '))
        print("==============SC001=============")
        if count1 != 0:
            print('Max(001): ' + str(maximum1))
            print('Min(001): ' + str(minimum1))
            print('Avg(001): ' + str(total1/count1))
        else:
            print('No score for SC001')
        print("==============SC101=============")
        if count2 != 0:
            print('Max(101): ' + str(maximum2))
            print('Min(101): ' + str(minimum2))
            print('Avg(011): ' + str(total2 / count2))
        else:
            print('No score for SC101')


    # if n == EXIT:
    #     print('No class scores were entered')
    #
    # if n.upper() == str('SC001'):
    #     s1 = int(input('Score: '))
    #     maximum = s1
    #     minimum = s1
    #     count = 1
    #     total = s1
    #     while True:
    #
    #
    # if n.upper() == str('SC101'):
    #     s2 = int(input('Score: '))
    pass


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
