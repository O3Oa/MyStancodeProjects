
"""
File: hangman.py
Name: Jessica
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    answer = random_word()
    # answer = 'CAUTIOUS'
    life = N_TURNS
    print(answer)
    print('The world looks like: '+'-'*len(answer))
    print(f'You have {N_TURNS} wrong guesses left.')
    change = '-' * len(answer)
    while life > 0:
        guess = str(input('Your guess: ')).upper()
        if len(guess) != 1 or not str.isalpha(guess):
            print('Illegal format.')
        else:
            if guess not in answer:
                life -= 1
                print(f"There is no {guess}'s in the world.")
                print_hangman(life)
                if life > 0:
                    print(f'The word looks like: {change}')
                    print(f'You have {life} wrong guesses left.')
                else:
                    print('You are completely hung :(')
                    print(f'The answer is: {answer}')
                    break
            else:
                show = ''
                for i in range(len(answer)):
                    if answer[i] == guess:
                        show += guess
                    else:
                        show += change[i]
                print('Your are correct!')
                if '-' in show:
                    print(f'The word looks like: {show}')
                    print(f'You have {life} wrong guesses left.')
                else:
                    print('You win!!')
                    print(f'The answer is: {answer}')
                    break
                change = show


def print_hangman(life):
    if life == N_TURNS - 1:
        print('(030)')
    elif life == N_TURNS - 2:
        print('(030)')
        print('  |')
    elif life == N_TURNS - 3:
        print('(030)')
        print(' /|')
    elif life == N_TURNS - 4:
        print('(030)')
        print(' /|\\')
    elif life == N_TURNS - 5:
        print('(030)')
        print(' /|\\')
        print(' /')
    elif life == N_TURNS - 6:
        print('(030)')
        print(' /|\\')
        print(' / \\')
    elif life == N_TURNS - 7:
        print('(Q_Q)')
        print(' /|\\')
        print(' / \\')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
