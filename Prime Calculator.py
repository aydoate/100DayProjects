def is_prime(num):
    #if 1, not prime
    if num==1:
        return False
    #if 2 or 3, prime
    if num == 2 or num==3:
        return True
    # if even number, not prime
    if num % 2 == 0:
        return False
    # for odd numbers:
    else:
        divider = (num - 1) / 2
        while num % divider != 0 and divider>2:
            divider -= 1
        if num % divider==0:
            return False
        else:
            return True

num=input("Welcome to the Prime Calculator. What whole number would you like to check?\n")
if is_prime(int(num)):
    print(f"Yes, {num} is a prime number.")
if not is_prime(int(num)):
    print(f"No, {num} is not a prime number.")
