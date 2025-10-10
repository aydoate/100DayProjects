import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwlist=[]                                  # Create an empty list to begin storing PW variables

for char in range(0,nr_letters):           # for range 0-user entered amount of letters, go through letters list and add random letters
    pwlist+=random.choice(letters)
for char in range(0,nr_symbols ):           # for range 0-user entered amount of symbols, go through symbol list and add random symbols
    pwlist+=random.choice(symbols)
for char in range(0,nr_numbers):           # for range 0-user entered amount of numbers, go through letters list and add random numbers
    pwlist+=random.choice(numbers)
random.shuffle(pwlist)           # Now that we have all characters, randomly shuffle them and re-store as pwlist
pw=""                           # Set PW to a blank value
for char in pwlist:           #for each char in pwlist, add char to pw. basically, convert list of characters to a str
    pw+=char
print(pw)                        #print final PW
