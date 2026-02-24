#Number guessing game
import random
import artDay12
game_play = True
print(artDay12.logo)
while game_play == True:
    comp_guess = random.randint(1, 100)
    print("Hello! Welcome to the game!\n")
    print("I am thinking of a number between 1 and 100.\n")
    dificulty = input("Choose a difficulty. Easy for a game with 10 attempts and hard for a game with 5 attempts\n").lower()
    if dificulty == "easy":
        attempts = 10
        while True:
            guess = int(input("Make a guess\n"))
            if guess > comp_guess:
                print("Your guess is too high\n")
                attempts -= 1
                print(attempts, "attempts left")
            elif guess < comp_guess:
                print("Your guess is too low\n")
                attempts -= 1
                print(attempts, "attempts left")
            elif guess == comp_guess:
                print("You guessed the correct number\n")
                break
            if attempts == 0:
                print("You could not guess the number.")
                break
    if dificulty == "hard":
        attempts = 5
        while True:
            guess = int(input("Make a guess\n"))
            if guess > comp_guess:
                print("Your guess is too high\n")
                attempts -= 1
                print(attempts, "attempts left")
            elif guess < comp_guess:
                print("Your guess is too low\n")
                attempts -= 1
                print(attempts, "attempts left")
            elif guess == comp_guess:
                print("You guessed the correct number\n")
                break
            if attempts == 0:
                print("You could not guess the number.")
                break
