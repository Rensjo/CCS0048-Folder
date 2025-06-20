def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def nextPrimeList(n):
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1


while True:
    user_input = input("Enter a positive number:")
    try:

        value = float(user_input)
        

        if not value.is_integer():
            print("The number should be whole value.")
            continue
        

        n = int(value)
        

        if n < 0:
            print("The number is not a positive integer")
            continue
        

        break
    
    except ValueError:

        print("Invalid input. Please enter a number.")
        continue


next_prime = nextPrimeList(n)
print("The first prime greater than the number entered is:", next_prime)
