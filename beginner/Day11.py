#Blackjack game
import random
cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
# cards = [11,11,11]
game = input("Do you want to start the game? Type yes if you do and no if you don't\n").lower()
while game == "yes":
    player_cards =[]
    computer_cards =[]
    player_score = 0
    computer_score = 0
    for i in range(0,2):
        player_cards.append(random.choice(cards))
        player_score += player_cards[i]  
    for i in range(0,2):
        computer_cards.append(random.choice(cards))
        computer_score += computer_cards[i]  
    if computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score+=computer_cards[len(computer_cards)-1] 
    if computer_score > 21:
        for i in range(0,2):
            if computer_cards[i]==11:
                computer_cards[i] = 1
            else:
                continue   
    
    print(f"Your cards are {player_cards}")
    print(f"Your score is {player_score}")
    print(f"Computer's first card is {computer_cards[0]}")

    desicion = input("do you want to add another card?").lower()
    while desicion =="yes":
        
        player_cards.append(random.choice(cards))
        player_score += player_cards[len(player_cards) - 1]
        print(player_score)
        print(player_cards)
        if player_score >21:
            print("You Lose")
            break
        if desicion == "no":
            break
        desicion = input("do you want to add another card?").lower()


    if player_score > 21:
        for i in range(0,2):
            if player_cards[i]==11:
                player_cards[i] = 1
            else:
                continue    
    

    if player_score== 21:
        print("You win\n") 
    elif player_score >= computer_score:
        print("You win\n") 
    else:
        print("You lose\n") 

    game = input("Do you want to start the game? Type yes if you do and no if you don't\n").lower()

    if game =="no":
        break




