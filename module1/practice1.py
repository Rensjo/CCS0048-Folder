name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\n===== USER PROFILE =====")
print(f"   Name: {name} \n    Age: {age}")

status = "You are eligible to vote!"
if age > 0 and age < 120:
    if age > 18:
        print(f" Status: {status}")
    else:
        print("Status: Underaged. Unable to vote yet.")
else:
    print("Invalid age entered.")