#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
# EASY_ATTEMPTS = 10
# HARD_ATTEMPTS = 5
# should_end = True
# attempts = 0
# def guess_number(guess,random_number,attempts):
#     while not should_end:
#         if attempts == 0:
#             print("You lose a game.")  
#         if guess == random_number:
#             print(f"You got it! The answer was {random_number}")
#             should_end = False
#         elif guess != random_number:
#             if guess < random_number:
#                 attempts -=1
#                 print("Too low.")
#                 print("Guess again.")
#                 print(f"You've {attempts} left to make a guess.")
#             elif guess > random_number:
#                 attempts -=1
#                 print("Too High.")
#                 print("Guess again.")
#                 print(f"You've {attempts} left to make a guess.")

# def level_of_game(level):
    
#     guess = int(input("Make a guess:"))
#     if level == "easy":
#         attempts = EASY_ATTEMPTS
        
#         guess_number(guess,random_number,attempts)
#     elif level == "hard":
#         attempts = HARD_ATTEMPTS
        
#         guess_number(guess,random_number,attempts)


# print(logo)
# print("Welcome to Number Guessing Game!")
# print("I'm thinking about number between 1 to 100 to guess.")
# random_number = random.randint(1,100)
# print("Random Number",random_number)
# level = input("Choose a level of game. Type 'easy' or 'hard'.:")
# level_of_game(level)

EASY_LEVEL = 10
HARD_LEVEL = 5

#Function to guess user's answer and actual answer.
def check_answer(guess,answer,turns):
    """Checks answer agianst guess.Returns number of turns remaining."""
    if guess > answer:
        print("Too High.")
        
        return turns - 1
    elif guess < answer:
        print("Too low.")
        
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard'.:")
    if level == "easy":
        
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    #choosing random number between 1 and 100.
    print("Welcome to Number Guessing Game!")
    print("I'm thinking about number between 1 to 100 to guess.")

    answer = random.randint(1,100)
    print(f"The answer is {answer}")

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You've {turns} attempts remaining to guess a number.")
        #let user to guess a number.
        guess = int(input("Make a guess:"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print(f"You ran out of guesses , You lose game. The answer was {answer}")
            return
        elif guess != answer:
            print("Guess Again.")

game()

            
        

    



