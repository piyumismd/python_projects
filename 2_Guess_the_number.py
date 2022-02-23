
import random


def guess(x):
    random_number = random.randint(1, x)
    guess_count = 0
    while guess_count != random_number:
        guess_count = int(input("Guess a number between 1 and " + str(x) + ": "))
        if guess_count < random_number:
            print("Sorry guess again, Too low")
        elif guess_count > random_number:
            print("Sorry guess again, Too high")
    print("Yay, Congrats, You have guessed the number " + str(random_number) + " correctly.")


guess(10)

