def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

function_dictionary={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate_new():
    should_continue=True
    n1=input("What's the first number?: ")
    while should_continue:
        operation=input("+\n-\n*\n/\nPick an operation: ")
        n2=input("What's the next number?: ")
        result=function_dictionary[f"{operation}"](int(n1),int(n2))
        print(result)
        again=input(f"Would you like to continue calculating with {result}? Type 'yes' or no'").lower()
        if again=="yes":
            n1=result
        else:
            should_continue=False
            print("\n"*50)
            calculate_new()
calculate_new()

