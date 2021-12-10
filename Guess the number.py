# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

# generate a random number
randNum = random.randint (0,100)

# generate the game using loop and if-else statements
while True:
    userGuess = int(input("Enter a number from 0-100: "))
    if userGuess > randNum:
        print("Greater than")
        continue
    elif userGuess < randNum:
        print ("less than")
        continue
    elif userGuess == randNum:
        print ("Congratulations! You guessed the correct number!")
        break
