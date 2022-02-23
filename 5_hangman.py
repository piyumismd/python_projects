
import random
from hangman_words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and You have used these letter: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(f"Current word: ", " ".join(word_list))

        user_letter = input(f"Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # deduct a life for a wrong answer
                print(f"Letter is not in the word.")

        elif user_letter in used_letters:
            print(f"You have already guessed that letter. Try again.")
        else:
            print(f"Invalid letter. Try again")

    if lives == 0:
        print(f"You died. The word is  {word}.")
    else:
        print("You guessed the correct word.")


hangman()
