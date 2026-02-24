
def find_highest_bidder(bidding_Dictionary):
    highest_bid=0
    for bidder in bidding_Dictionary:
        bid_amount = bidding_Dictionary[bidder]
        if bid_amount> highest_bid:
            highest_bid= bid_amount
            winner = bidder


    print(f"the winner is {winner} with the bid of ${highest_bid} ")

bidding = {

}

while True:
    name = input("What is your name\n")
    price = int(input("What is bid price\n"))
    choice = input("Are there any more bidders?\n ").lower()
    bidding[name] = price
    if choice == "yes":
        print("\n"*100)
    elif choice == "no":
        find_highest_bidder(bidding)
        print(bidding)
        break
    else:
        print("Try again!")
     




