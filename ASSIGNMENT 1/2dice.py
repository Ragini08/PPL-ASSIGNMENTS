import random

min = 1
max = 6

s = input('Would you like to roll the dice?(Y/N)  ')


def roll():
    print("Your number is: " + str(random.randint(min, max)))
    global play_again
    play_again = input('Would you like to play again?(Y/N)  ')


if s == "y":
    roll()
    while play_again == "y":
        roll()

elif s == "no":
    print("Game Over")
else:
    print('Wrong input')