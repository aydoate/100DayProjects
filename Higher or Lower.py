##import art and game data
import art
import game_data
import random

#Initial game conditions: Chooses 2 random entries as A and B, creates dictionaries, and set score to 0:

user_score=0
dictionary_a=random.choice(game_data.data)
dictionary_b=random.choice(game_data.data)
print(dictionary_a["follower_count"])
print(dictionary_b["follower_count"])
#Function to compares follower count and returns either A or B as what the user's guess needs to be in order to be correct
def compare(dictionary_a,dictionary_b):
    if dictionary_a["follower_count"]>dictionary_b["follower_count"]:
        return "A"
    if dictionary_a["follower_count"]<dictionary_b["follower_count"]:
        return "B"


#Prompts user for input, evaluates input, tells them if right or wrong
def ask():
    print(f"Compare A: {dictionary_a["name"]}, a {dictionary_a["description"]}, from {dictionary_a["country"]}.")
    print(f"Against B: {dictionary_b["name"]}, a {dictionary_b["description"]}, from {dictionary_b["country"]}.")
    user_selection=input("Who has more followers? Type 'A' or 'B'").upper()
    correct_answer = compare(dictionary_a,dictionary_b)
    if user_selection==correct_answer:
        global user_score
        user_score+=1
        print("You're right!")

    else:
        global should_continue
        should_continue=0


ask()
should_continue=1
while should_continue==1:
    dictionary_a=dictionary_b
    dictionary_b=random.choice(game_data.data)
    ask()
else:
    print("Sorry that's wrong")
    print(f"Your score was {user_score}")

