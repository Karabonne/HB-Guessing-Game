"""A number-guessing game."""
import random

print("welcome!")
name = input("what is your name? ")
print("Hi {}! Welcome to this really cool guessing game! Pick a number between 1 and 100: ".format(name))

answer = random.randint(1, 101)
number_of_guesses = 0
while True: 
    guess = int(input())
    if guess < answer: 
        print("Too low! Try again.")
        number_of_guesses += 1
    elif guess > answer: 
        print("Too high! Try again.")
        number_of_guesses += 1
    else: 
        print("Correct! Nice job.")
        number_of_guesses += 1
        print("It took you {} guesses!".format(number_of_guesses))
        break


#repeat forever:
#    get guess
#    if guess is incorrect:
#        give hint
#        increase number of guesses
#    else:
#        congratulate player