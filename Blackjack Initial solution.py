import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards=[]
cpu_cards=[]
user_cards = random.sample(cards,2)
cpu_cards = random.sample(cards,2)

print(f"Computer showing {cpu_cards[0]}")
print(f"User draws {user_cards}")

def hitting():
    user_total = sum(user_cards)
    cpu_total = sum(cpu_cards)
    if user_total==21:                                                  #Checking if user or CPU has 21
        if cpu_total==21:
            print("The game ends in a draw")
        else:
            print("You have Blackjack! You win!")
    elif cpu_total==21:
        print("The computer has Blackjack. You lose.")

    else:                                                                  #If not, move to player and cpu hitting
        player_hitting = True
        while player_hitting:
            user_total = sum(user_cards)
            if user_total>21:
                print(f"Your hand is {user_cards}. Your total is {user_total}. You went over 21. You lose.")
                return
            else:
                hit_stand=input(f"Your hand is {user_cards}. Your hand total is {user_total}. Do you hit or stand? Type 'hit' or 'stand': ").lower()
                if hit_stand=="hit":
                    user_cards.extend(random.sample(cards,1))
                    user_total=sum(user_cards)
                    while user_total>21 and 11 in user_cards:
                        ace_index=user_cards.index(11)
                        user_cards[ace_index]=1
                        user_total=sum(user_cards)

                if hit_stand=="stand":
                    player_hitting = False
        while not player_hitting:
            if cpu_total<17:
                    cpu_cards.extend(random.sample(cards, 1))
                    cpu_total=sum(cpu_cards)

                    while cpu_total>21 and 11 in cpu_cards:
                        ace_index=cpu_cards.index(11)
                        cpu_cards[ace_index]=1
                        cpu_total=sum(cpu_cards)
                    if cpu_total>21:
                        print(f"Computer busts with {cpu_cards}. You win!")
                        return
            elif cpu_total<22:
                    print(f"Computer ends with {cpu_cards} and a total of {cpu_total}.")
                    if user_total>cpu_total:
                        print(f"Congratulations, your {user_total} beats the computer's {cpu_total}. You win!")
                    if user_total==cpu_total:
                        print(f"You have {user_total} and the computer has {cpu_total}. The game ends in a draw")
                    if user_total<cpu_total:
                        print(f"Your {user_total} loses to the computer's {cpu_total}. You lose.")
                    return

##Program:

hitting()
play_again=input("Would you like to play again? Type 'yes' or 'no'").lower()
if play_again=="yes":
    user_cards = []
    cpu_cards = []
    user_cards = random.sample(cards, 2)
    cpu_cards = random.sample(cards, 2)
    print(f"Computer showing {cpu_cards[0]}")
    print(f"User draws {user_cards}")
    hitting()


