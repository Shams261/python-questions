## MODIFY GUESSING NUMBER GAMES 

import random
winning_number = random.randint(1,100)
guess = 1
user = int(input("enter a number between 1 to 100:"))
game_over = False
while not game_over:
    if user == winning_number:
        print(f"you win, you guess the number {guess} times")
        game_over = True
    else:
        if user < winning_number:
            print("too low")
            guess += 1
            user = int(input("guess number one again:"))
        else:
            print("too high")
            guess += 1
            user = int(input("guess number one again:"))