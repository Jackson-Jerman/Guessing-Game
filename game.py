"""A number-guessing game."""

# Put your code here
from random import * 


num = randint(1, 100)
tries = 0

print("Howdy, what's your name?")

name = input('(type your name)')

print(name + " I'm thinking of a number between 1 and 100.")

print("Try to guess my number.")


while True: 

    guess = input("Your guess?")

    try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}" is not a valid number, try again.')
        continue

    tries += 1 

    if guess < num:
        print("Your guess is too low, try again.")
    elif guess > num:
        print("Your guess is too high, try again.")
    else:
        print(f'Well done, {name}!' + f' You found my number in {tries} tries!' )
        break
        
