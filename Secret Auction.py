def find_highest_bidder():
    highest_bid=0
    highest_bidder=""
    for bidder in bid_list:
        bid_amount=bid_list[name]
        if  bid_amount>highest_bid:
            highest_bid=bid_amount
            highest_bidder=name
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid} ")

bid_list={}
bids_ongoing="yes"
while bids_ongoing == "yes":
    name=input("What is your name?")
    bid_amount=int(input("What is your bid?: $"))
    bid_list[name]=bid_amount
    bids_ongoing=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if bids_ongoing == "yes":
        print("\n" * 20)
    else:
        find_highest_bidder()
