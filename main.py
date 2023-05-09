from art import logo, vs
from game_data import data
# needs replit or equivalent
from replit import clear
import random


def checkAnswer(user_choice, user_not_choice, game_array):
    '''checks if the users choice is correct. Returns true if yes, else returns false'''
    print(user_choice)
    print(user_not_choice)
    if int(game_array[user_choice]["follower_count"]) > int(game_array[user_not_choice]["follower_count"]):
        return True
    else:
        return False


def higherLowerGame():
    # some initialization
    current_score = 0
    choice = 0
    game_data = random.sample(data, 2)
    # start the game
    isWinner = True

    while isWinner:
        print(logo)
        if current_score > 0:
            print(f"You're right! Current score: {current_score}")
        print(
            f"Compare A: {game_data[0]['name']}, a {game_data[0]['description']}, from {game_data[0]['country']}")
        print(vs)
        print(
            f"Against B: {game_data[1]['name']}, a {game_data[1]['description']}, from {game_data[1]['country']}")
        answer = input("Who has more followers? Type 'A' or 'B':").lower()
        # choice = 0 if answer == 'a' else 1
        if answer == 'a':
            choice = 0
            un_choice = 1
        elif answer == 'b':
            choice = 1
            un_choice = 0
        else:
            isWinner = False
            print(f"Sorry that's wrong. Final score: {current_score}")
            return

        isWinner = checkAnswer(choice, un_choice, game_data)
        clear()
        if isWinner:
            current_score += 1
            del game_data[1]
            game_data.append(random.choice(data))
            while game_data[0] == game_data[1]:
                del game_data[1]
                game_data.append(random.choice(data))
        else:
            print(logo)
            isWinner = False
            print(f"Sorry that's wrong. Final score: {current_score}")


higherLowerGame()
