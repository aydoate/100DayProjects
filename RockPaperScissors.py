rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''
import random
choices=["Rock","Paper","Scissors"]
player_choice=input("Let's play a game. Choose 0 for Rock,1 for Paper, or 2 for Scissors")
computer_choice=random.randint(0,2)
if player_choice=="0":
    print(rock)
    if computer_choice==0:
        print(rock)
        print("Tie Game")
    elif computer_choice==1:
        print(paper)
        print("Computer Wins")
    elif computer_choice==2:
        print(scissors)
        print("You win!")
elif player_choice=="1":
    print(paper)
    if computer_choice == 1:
        print(paper)
        print("Tie Game")
    elif computer_choice == 2:
        print(scissors)
        print("Computer Wins")
    elif computer_choice == 0:
        print(rock)
        print("You win!")
elif player_choice=="2":
    print(scissors)
    if computer_choice == 2:
        print(scissors)
        print("Tie Game")
    elif computer_choice == 0:
        print(rock)
        print("Computer Wins")
    elif computer_choice == 1:
        print(paper)
        print("You win!")
else: print("You broke the program. Congratulations, bet you feel pretty smart.")