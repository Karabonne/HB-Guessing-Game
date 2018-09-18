"""A number-guessing game."""
import random

print("welcome!")
name = input("what is your name? ")
print(f"Hi {name}! Welcome to this really cool guessing game! Pick a number between 1 and 100: ")

answer = random.randint(1, 101)
number_of_guesses = 0
correct = False
excepted = True
while correct == False:
    while True: 
        try:
            guess = int(input())
            if 1 <= guess <= 100:
                number_of_guesses += 1
                if guess < answer: 
                    print("Too low! Try again.")
                elif guess > answer: 
                    print("Too high! Try again.")
                else: 
                    print("Correct! Nice job.")
                    print("It took you {} guesses!".format(number_of_guesses))
                    correct = True
                    break
            else:
                print("Please enter a valid guess this time, yo. :)")
        except ValueError:
            print("integers only, c'mon!")



#repeat forever:
#    get guess
#    if guess is incorrect:
#        give hint
#        increase number of guesses
#    else:
#        congratulate player