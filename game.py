"""A number-guessing game."""
import random


correct = False
top_score = 0
number_of_guesses = 0
first_game = True




def game_mode_1():
    answer = random.randint(lower_bound, upper_bound)
    while correct == False:
        try:
            guess = int(input("guess: "))
        except ValueError:
            print("integers only, c'mon!")
            continue
        if lower_bound <= guess <= upper_bound:
            number_of_guesses += 1
            if number_of_guesses >= 10:
                print("Too many guesses, sorry :(. Exiting...")
                break
            else:
                if guess < answer: 
                    print("Too low! Try again.")
                elif guess > answer: 
                    print("Too high! Try again.")
                else: 
                    print("Correct! Nice job.")
                    print(f"It took you {number_of_guesses} guesses!")
                    while first_game == True:
                        top_score = number_of_guesses
                        first_game = False
                    if number_of_guesses <= top_score:
                        top_score = number_of_guesses
                    print(f"Your all time top score is {top_score}, in a range of {lower_bound} to {upper_bound}.")
                    new_game = input("New game? Enter yes, anything else will exit: ")
                    if new_game == "yes":
                        answer = random.randint(lower_bound, upper_bound)
                        number_of_guesses = 0
                        continue
                    else:
                        correct = True
        else:
            print("Please enter a valid guess this time, yo. :)")

def game_mode_2():
    print("In this version, the computer will guess your number. You will tell it the upper bound and lower bound.")
    lower_bound = int(input("your lower bound: "))
    upper_bound = int(input("your upper bound: "))

    while True:
        guess = random.randint(lower_bound, upper_bound)
        print(f"Computer's guess is {guess}")
        if lower_bound <= guess <= upper_bound:
            number_of_guesses += 1
        if number_of_guesses >= 10:
            print("Too many guesses, sorry :(. Exiting...")
            break
        else:
            if guess < answer: 
                print("Too low! Try again.")
            elif guess > answer: 
                print("Too high! Try again.")
            else: 
                print("Correct! Nice job.")
                print(f"It took you {number_of_guesses} guesses!")
                while first_game == True:
                    top_score = number_of_guesses
                    first_game = False
                if number_of_guesses <= top_score:
                    top_score = number_of_guesses
                print(f"Your all time top score is {top_score}, in a range of {lower_bound} to {upper_bound}.")
                new_game = input("New game? Enter yes, anything else will exit: ")
                if new_game == "yes":
                    answer = random.randint(lower_bound, upper_bound)
                    number_of_guesses = 0
                    continue
                else:
                    correct = True

print("welcome!")
name = input("what is your name? ")


print(f"Hi {name}! Welcome to this really cool guessing game! Pick your game mode.")
lower_bound = int(input("Set the lower bound: "))
upper_bound = int(input("Set the upper bound: "))
while upper_bound <= lower_bound:
    print("Please make sure the upper bound is actually greater than the lower one...")
    upper_bound = int(input("Set the upper bound: "))
mode = int(input("Enter 1 for Guessing CPU Number, enter 2 for CPU Guessing Your Number: "))
if mode == 1:
    game_mode_1()
elif mode == 2:
    game_mode_2()
else:
    print("Please pick one or two! Exiting...")