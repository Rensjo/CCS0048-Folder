# if False:

#     print("Nissan")

# elif True:

#     print("Ford")

# elif True:

#     print("BMW")

# else:

#     print("Audi")

# word = ""

# counter = 0

# letters = ["c", "a", "r"]

# while counter < len(letters):

#   word = word + letters[counter]

#   counter = counter + 1

# print(word)


# for x in range(4):
#     print("Hello")

# a = ['foo', 'bar', 'baz', 'qux', 'corge']

# while a:

#     if len(a) < 3:

#         continue

#     print(a.pop())

# print('Done.')


# a = 0

# for i in range(10):

#     a += 1

# for j in range(10):

#     a += 1

# print(a)


# sum = 0

# counter = 0

# numbers = [1, 2, 3, 4]

# while counter < len(numbers):

#   sum = sum + numbers[counter]

#   counter = counter + 1

# print(sum)


# d = {'foo': 1, 'bar': 2, 'baz': 3}

# while len(d) > 3:

#     print(d.popitem())

# print('Done.')


# for i in range(3):

#     print("*", end="")

# for j in range(3):

#     print("*", end="")


# a = 0

# for i in range(10):

#     a += 1

#     for j in range(10):

#         a += 1

# print(a)


# if 1:

#     print("1 is truthy!")

# else:

#     print("???")


# a=0

# for i in range(10):

#     a += 1

# print(a)


# for y in range(1,11):
#     print(y)


# for i in range(3):

#     for j in range(3):

#         print("*", end="")

#     print()


# a = 0

# for i in range(10):

#     for j in range(10):

#         a += 1

# print(a)


# a = 0

# for i in range(10):

#     a += 1

#     for j in range(10):

#         a += 1

# print(a)



# pyramid = int(input("Enter the number of rows for your pyramid: "))

# for rows in range(1, pyramid + 1, 2):
#     space = (pyramid - rows) // 2

#     print(" " * space, end="")
#     for rowz in range(1, rows+1):
#         print(rowz, end="")
#     print()


# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(absolute_value(2))
# print(absolute_value(-4))


# def my_func():
#     x = 10
#     print("Value inside function: ", x)
# x = 20
# my_func()
# print("Value outside function: ", x)



# def greet(name, msg):

#     print("Hello" + name + ', ' + msg)

# greet("Jorens", "Good Evening!")


# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
    
# num = int(input("Enter a Number you want to get the factorial of: "))
# print("The factorial of", num, "is", factorial(num))


my_list = [1, 2, 4, 6, 8, 10, 12]