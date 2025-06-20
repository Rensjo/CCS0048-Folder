def digital_root(n):
    while n >= 10:
        sum_of_digits = 0
        while n > 0:
            sum_of_digits += n % 10
            n //= 10
        n = sum_of_digits
    return n

n = int(input("Enter the number:"))
result = digital_root(n)
print("The digital root is:", result)
