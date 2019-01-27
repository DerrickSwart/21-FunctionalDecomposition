"""
Hangman.

Authors: Derrick Swart, Joshua Giambattista , Joseph Conrad
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random
with open('words.txt') as words:
    words.readline()
    string = words.read()
    word = string.split()



def lose(secret_word):
    print('Im sorry, you lose. The secret word was:  ', secret_word)
    x = str(input('would you like to play again? y/n:   '))
    if x == 'y':
        main()
    if x == 'n':
        print('Thanks for playing Hangman!')
        exit()
def get_word(word_length):
    r = random.randrange(0,len(word))
    if len(word[r])< word_length:
        get_word(word_length)
    secret_word = word[r]
    return secret_word

def get_guess():
    guess = input('Please enter a letter to guess:    ')
    return guess
def check_if_correct(secret,max):

    guess = get_guess()
    for k in range(len(secret)):
        if guess == secret[k]:
            return guess
    max[0] = max[0] -1
    left = incorrect_guess(max)

    if left == 0:
        lose(secret)

def incorrect_guess(max):
    return max[0]

def print_correct_letters(secret, max):
    sequence = []
    for k in range(len(secret)):
        sequence = sequence + ['-']
    while True:
        guess = check_if_correct(secret,max)
        for j in range(len(sequence)):
            if guess == secret[j]:
                sequence[j] = secret[j]
        string = construct_string(sequence)
        print('you have', max[0], 'incorrect guesses remaining')
        print(string)
        if string == secret:
            break
    win()
def construct_string(sequence):
    string = ''
    for k in range(len(sequence)):
        string = string + sequence[k]
    return string
def win():
    print('Conradulations, you Win')
    x = input('Would you like to play again? y/n:  ')
    if x == 'y':
        main()
    if x == 'n':
        print('Thank you for playing Hangman!')
        exit()
def main():
    word_length = int(input('What would you like the minimum length of the word to be:   '))
    secret = get_word(word_length)
    max = [int(input('please enter how many incorrect guesses you would like to have:   ')),0]
    print_correct_letters(secret,max)


main()