import random
import sys

print('ROCK, PAPER, SCISSORS')

# Keeping track of wins, loses, and ties
wins = 0
ties = 0
losses = 0


while True:
    print(f"{wins} wins, {losses} Losses, and {ties} Ties")
    # Player Input Loop
    while True:
        print("Enter your move (r)ock, (p)aper, (s)cissors, or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # quick the program
        if playerMove == "r" or playerMove == "p" or playerMove == 's':
            break
        print('Type of one of r, p, s, q.')

    # Display what the player chooses
    if playerMove == "r":
        print('ROCK versus ....')
    elif playerMove == 'p':
        print("PAPER versus ....")
    elif playerMove == 's':
        print('SCISSOR versus ....')

    # Randomly generate a number between 1 and 3
    randomNum = random.randint(1, 3)
    if randomNum == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNum == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNum == 3:
        computerMove = 's'
        print("SCISSOR")

    # display and record the win / lose / tie

    if playerMove == computerMove:
        print("It's a tie")
        ties += 1
    elif playerMove == "r" and computerMove == 's':
        print('You Win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win')
        wins += 1
    elif playerMove == "s" and computerMove == "p":
        print('You Win')
        wins += 1
    elif computerMove == 'r' and playerMove == 's':
        print("You Lose")
        losses += 1
    elif computerMove == 'p' and playerMove == 'r':
        print("You Lose")
        losses += 1
    elif computerMove == 's' and playerMove == "p":
        print("You Lose")
        losses += 1
