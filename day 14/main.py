# generating random account from game data
import random
import os
from art import logo,vs
from game_data import data

def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name=='nt' else 'clear')
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

def check_answer(user_guess, a_followers, b_followers):
    """Takes a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

    # Format the account data into printable format
def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

while game_should_continue:
    account_a = account_b
    while account_a==account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Asking user for a guess
    valid_guesses = ['a', 'b']
    guess = ""
    while guess not in valid_guesses:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear the screen
    clear_screen()
    print(logo)

    # -Getting follower count of each account

    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    # -Using if statements
    # Passing the function in a variable for further use
    is_correct = check_answer(guess, follower_count_a, follower_count_b)

    if is_correct:
        score+=1
        print(f"You are right! Current score is {score}.")
    else:
        print(f"Sorry, you are wrong! Final score is {score}.")
        game_should_continue = False


