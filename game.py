"""A number-guessing game."""
import random

print("welcome!")
name = input("what is your name? ")
print(f"Hi {name}! Welcome to this really cool guessing game! Pick a number between 1 and 100: ")

#answer = random.randint(1, 101)
answer = 50
correct = False
top_score = 0
number_of_guesses = 0
first_game = True
while correct == False:
    try:
        guess = int(input("guess: "))
    except ValueError:
        print("integers only, c'mon!")
        continue
    if 1 <= guess <= 100:
        number_of_guesses += 1
        if guess < answer: 
            print("Too low! Try again.")
        elif guess > answer: 
            print("Too high! Try again.")
        else: 
            print("Correct! Nice job.")
            print("It took you {} guesses!".format(number_of_guesses))
            while first_game == True:
                top_score = number_of_guesses
                first_game = False
            if number_of_guesses <= top_score:
                top_score = number_of_guesses
            print(f"Your all time top score is {top_score}.")
            new_game = input("New game? Enter yes, anything else will exit: ")
            if new_game == "yes":
                #answer = random.randint(1, 101)
                number_of_guesses = 0
                continue
            else:
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