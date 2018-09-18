"""A number-guessing game."""
import random

print("welcome!")
name = input("what is your name? ")
print("Hi {}! Welcome to this really cool guessing game! Pick a number between 1 and 100: ".format(name))

answer = random.randint(1, 101)
number_of_guesses = 0
correct = False
while correct == False:
    
    guess = int(input())
    number_of_guesses += 1
    if 1 <= guess <= 100:
        if guess < answer: 
            print("Too low! Try again.")
        elif guess > answer: 
            print("Too high! Try again.")
        else: 
            print("Correct! Nice job.")
            print("It took you {} guesses!".format(number_of_guesses))
            correct = True
    else:
        print("Please enter a valid guess this time, yo. :)")


#repeat forever:
#    get guess
#    if guess is incorrect:
#        give hint
#        increase number of guesses
#    else:
#        congratulate player