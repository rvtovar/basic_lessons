# Guessing Game

import random

secretNum = random.randint(1, 20)

# Ask the player to guess the number a certain number of times lets say 6

for guessTaken in range(1, 7):
    print("Take a Guess: ")
    guess = int(input())

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your Guess is too high')
    else:
        break

if guess == secretNum:
    print(f"Yes the number was {secretNum}")
else:
    print(f'Sorry you lose the number was {secretNum}')
