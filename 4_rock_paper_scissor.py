
import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a Tie'

    if is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost'


def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())


def play():
    player = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    opponent = random.choice(['r', 'p', 's'])

    if player == opponent:
        return 'Match Tie'

    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return 'You won!'
    else:
        return 'You lost'


print(play())





