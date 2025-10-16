# Generate a number between 1 and 100
import random
NUMBER=random.randint(1,100)

#Set default user lives to 10
USER_LIVES=10

##Function to compare user choice with NUMBER
def compare_numbers(NUMBER,guess):
    global USER_LIVES
    if NUMBER==guess:
        print(f"You got it! The answer was {NUMBER}")
    if NUMBER>guess:
        USER_LIVES-=1
        print("Too low. Guess again")
    if NUMBER<guess:
        USER_LIVES -= 1
        print("Too high. Guess again")

##Ask user for number
def ask():
    print(f"You have {USER_LIVES} attempts remaining to guess the number")
    guess=int(input("Make a guess: "))
    compare_numbers(NUMBER,guess)
    if USER_LIVES==0:
        print("You ran out of lives. Try again")
        return
    if guess==NUMBER:
        return
    else:
        ask()

##Game Start
print("Welcome to the number guessing game!\n")
print("I'm thinking of a number between 1 and 100\n")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard'").lower()
if difficulty=="hard":
    USER_LIVES=5
ask()



