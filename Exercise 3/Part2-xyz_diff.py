def xyz_diff(str1, str2):
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            return i

    if len(str1) != len(str2):
        return min_length

    return -1


str1 = input("Enter first string:")
str2 = input("Enter second string:")

result = xyz_diff(str1, str2)
print(result)
