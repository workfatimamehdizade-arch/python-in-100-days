#Higher or lower game
# in this game you compare 2 people by the amount of follower they have
# and guess who has more followers. Game will stp once yu give wrong answer.

from data_for_day14_game import data
import artDay14
import random
play_game = True
print(artDay14.logo)
score = 0
while play_game:
    r_number1 = random.randint(0,len(data)-1)
    r_number2 = random.randint(0,len(data)-1)
    print(f"Compare {data[r_number1]['name']}, {data[r_number1]['description']}, from {data[r_number1]['country']}\n")
    print(artDay14.vs)
    print(f"{data[r_number2]['name']}, {data[r_number2]['description']}, from {data[r_number2]['country']}\n")
    decision = input(f"Who has more followers? Type  A if {data[r_number1]['name']} or B if {data[r_number2]['name']}\n").lower()
    if decision == "a" and data[r_number1]['follower_count'] > data[r_number2]['follower_count']:
        score += 1
        print("You are correct!\n")
        print(f"Your score is: {score}")
    elif decision == "a" and data[r_number2]['follower_count'] > data[r_number1]['follower_count']:
        print("You lose")
        print(f"Your score is: {score}")
        play_game = False
    elif decision == "b" and data[r_number2]['follower_count'] > data[r_number1]['follower_count']:
        score += 1
        print("You are correct!")
        print(f"Your score is: {score}")
    elif decision == "b" and data[r_number1]['follower_count'] > data[r_number2]['follower_count']:
        print("You lose")
        print(f"Your score is: {score}")
        play_game = False





