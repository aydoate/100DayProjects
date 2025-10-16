##import random and card deck at the beginning of file
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

##this function deals 1 card
def deal_cards():
    return random.choice(cards)

##this function calculates the score
def calculate_score(hand):
    score=sum(hand)
    if score==21 and len(hand)==2:
        return 0 # 0 is blackjack
    while score>21 and 11 in hand: #converts Aces to 1 if over 21
        ace_index=hand.index(11)
        hand[ace_index]=1
        score=sum(hand)
    return score

##compare user and CPU scores
def compare_score(user_score,cpu_score):
    if user_score == 0:
        return "You have Blackjack! You win! 🥳"
    elif cpu_score == 0:
        return "Computer has Blackjack. You lose. 😫"
    elif user_score > 21:
        return f"You went over 21 with {user_score}, you lose. 😭"
    elif cpu_score > 21:
        return f"Computer busts with {cpu_score}, you win! 😁"
    elif user_score == cpu_score:
        return f"You both have {user_score}, the game ends in a draw. 🤝"
    elif user_score > cpu_score:
        return f"Congratulations, your {user_score} beats the computer's {cpu_score}. You win! 🎉"
    else:  # cpu_score > user_score
        return f"Sorry, the computer's {cpu_score} beats your {user_score}. You lose. 😔"

##This function plays a single game of blackjack

def play_game():
    user_cards=[]
    cpu_cards=[]
    for initial_cards in range(2):
        user_cards.append(deal_cards())
        cpu_cards.append(deal_cards())
    user_score=calculate_score(user_cards)
    cpu_score=calculate_score(cpu_cards)
    print(f"\n--- New Game ---")
    print(f"Computer showing {cpu_cards[0]}")
    print(f"Your cards are {user_cards}, current score: {user_score}")
    #Check if anyone has blackjack
    if user_score == 0 or cpu_score==0:
        pass
    #User hitting section
    else:
        user_hitting=True
        while user_hitting:
            if user_score>21:
                user_hitting=False
            else:
                hit_stand=input(f"your hand total is {user_score}. Would you like another card? Type 'hit' or 'stand': ").lower()
                if hit_stand=="hit":
                    user_cards.append(deal_cards())
                    user_score = calculate_score(user_cards)
                    if user_score>21:
                        print(f"Your hand is {user_cards} with a total of {user_score}. You went over 21, you lose.")
                        user_hitting=False
                elif hit_stand=="stand":
                    user_hitting=False
                else:
                    print("Invalid input. Please type 'hit' or 'stand'.")
        # CPU hitting section
        if user_score<=21 and user_score!=0:
            print(f"\nComputer's turn. Computer's full hand is {cpu_cards}, total score: {cpu_score}")
            while cpu_score<17 and cpu_score !=0:
                cpu_cards.append(deal_cards())
                cpu_score = calculate_score(cpu_cards)
            print(f"Computer ends with {cpu_cards} and a total of {cpu_score}.")
            print(f"Your final hand: {user_cards}, final score: {user_score}")
    user_score=calculate_score(user_cards)
    cpu_score=calculate_score(cpu_cards)
    print(compare_score(user_score,cpu_score))

#Main game loop
while input("\nWould you like to play a game of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    play_game()
print("Thanks for playing! Goodbye.")


