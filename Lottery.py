# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

# generate random numbers and ask user for 3 numbers
def gameplay():
    lotteryNum1 = random.randint(0,9)
    lotteryNum2 = random.randint(0,9)
    lotteryNum3 = random.randint(0,9)
    userNum1 = int(input("Enter the first number(0-9): "))
    userNum2 = int(input("Enter the second number(0-9): "))
    userNum3 = int(input("Enter the third number(0-9): "))
    if lotteryNum1 == userNum1 and lotteryNum2 == userNum2 and lotteryNum3 == userNum3:
        score = 1
    else:
        score = 0
    if score == 1:
        print (f"Winning numbers: {lotteryNum1}, {lotteryNum2}, {lotteryNum3}.")
        print ("Congratulations! You win!")
    else:
        print (f"Winning numbers: {lotteryNum1}, {lotteryNum2}, {lotteryNum3}.")
        print ("Sorry! Your guess didn't match with the numbers. You lose.")
    return lotteryNum1, lotteryNum2, lotteryNum3, userNum1, userNum2, userNum3

lottery = gameplay()

while True:
    userDecision = input("Would you like to try again? y/n?: ")
    if userDecision == "y":
        gameplay()
        continue
    elif userDecision == "n":
        break
    else:
        print("y or n are the only valid answers.")