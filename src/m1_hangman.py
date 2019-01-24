"""
Hangman.

Authors: Derrick Swart and Joshua Giambattista 
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random
with open('words.txt') as words:
    words.readline()
    string = words.read()
    word = string.split()




def get_word():
    r = random.randrange(0,len(word))
    secret_word = word[r]
    print(secret_word)
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
        lose()

def incorrect_guess(max):
    print('you have', max[0], 'left')
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
        print(string)
        if string == secret:
            break
def construct_string(sequence):
    string = ''
    for k in range(len(sequence)):
        string = string + sequence[k]
    return string
def main():
    secret = get_word()
    max = [int(input('please enter how many incorrect guesses you would like to have')),0]
    print_correct_letters(secret,max)


main()