# Given list of numbers
numbers = [63, 52, 10, 42, 32, 17, 60, 45, 47, 39, 71, 55, 41,
           95, 70, 48, 42, 32, 13, 35]

# (a) Print the list
print("a) List:", numbers)

# (b) Print the average
average = sum(numbers) / len(numbers)
print("b) Average:", average)

# (c) Largest and smallest values
print("c) Largest:", max(numbers))
print("   Smallest:", min(numbers))

# (d) Second largest and second smallest
unique_sorted = sorted(set(numbers))
print("d) Second Largest:", unique_sorted[-2])
print("   Second Smallest:", unique_sorted[1])

# (e) Count even numbers
even_count = len([n for n in numbers if n % 2 == 0])
print("e) Even numbers count:", even_count)

# (f) Count odd numbers
odd_count = len([n for n in numbers if n % 2 != 0])
print("f) Odd numbers count:", odd_count)
