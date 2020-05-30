import random
print("-----GUESS THE NUMBER GAME-----")
num = random.randint(1,25)
chance = 0
print("Guess a number between 1 and 25 : ")
while chance < 7:
    guess = int(input())
    if guess == num:
        print("Congratulations! You got the number!")
        break
    elif guess < num:
        print("Guess a high number! ")
    else:
        print("Guess a low number! ")
    chance = chance + 1

if not chance < 7:
    print("No more chances to guess, the number is ",num)