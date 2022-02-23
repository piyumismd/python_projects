
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess_count = 0
    while feedback != 'c':
        if low != high:
            guess_count = random.randint(low, high)
        else:
            guess_count = low  # we also can put high in to this
        feedback = input(f'Is {guess_count} too high(H), too low(L), or correct(C)??').lower()
        if feedback == 'h':
            high = guess_count - 1
        if feedback == 'l':
            low = guess_count + 1

    print(f'Yay! The computer guessed your number, {guess_count} correctly!')


computer_guess(10)
