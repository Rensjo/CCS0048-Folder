number = int(input("Enter a positive integer: "))

for i in range(1, number + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print("Counting complete. Have a nice day!")

