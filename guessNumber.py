# This is a guess the number game.

import sys, random
guess_num = random.randint(1,20)

def guess():
    counter = 0
    while True:
        print("Take a guess")
        counter = counter + 1
        try:
            guess = int(input())
        except ValueError:
            print('Enter Valid Value')
            continue

        if guess < guess_num:
            print("Your guess number " + str(guess) + " is too low")
            continue
        elif guess > guess_num:
            print("Your guess number " + str(guess) + " is too high")
            continue
        elif guess == guess_num:
            print("You guessed a right number")
            print("You guessed in " + str(counter) + " times")
            sys.exit()
        else:
            print("Looks like you are exhausted... Bye")
            sys.exit()
guess()
