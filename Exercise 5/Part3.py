# Name: Jorens Ivan Rance
# School: FEU TECH
# Machine Problem – 3

# Original list of numbers
nums = [
    30, 7, 30, 2, 88, 44, 60, 40, 1, 53, 100, 72, 86,
    64, 40, 85, 3, 19, 63, 84, 17, 31, 95, 84, 99, 60,
    85, 74, 65, 38, 43, 80, 39, 70, 8, 21, 32, 68, 64,
    55, 88, 84, 49, 68, 70, 98, 21, 51, 3, 97
]

# Replace all values greater than 10 with 666
replaced = []
equal_count = 0
not_equal_count = 0

for value in nums:
    if value > 10:
        replaced.append(666)
        equal_count += 1
    else:
        replaced.append(value)
        not_equal_count += 1

# Output
print("Name: Jorens Ivan Rance")
print("School: FEU TECH")
print("Machine Problem – 3")
print("OUTPUT is", replaced)
print("Total equal values", equal_count)
print("Total not equal values", not_equal_count)
