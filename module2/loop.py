

count = 0
while count < 5:
    print (count, " is less than 5")
    count = count + 1
else:
    print (count, " is not less than 5 anymore")


oni=["Oh, loko, bungangang kriminal, what the fuck? (Yah)",
    "Kung si mommy bumagsak, lagapak (Yah, yah)",
    "Pumutok ka na agad, wala pang suck (Ah)",
    "Ibaon mo, daddy, dapat maglo-lock (Ayy, ayy)"]

for i in range(len(oni)):
    print(oni[i])

for val in "string":
    if val == "n":
        continue
    print(val)
print("The end")


diamond = int(input("Enter number of rows: "))

for i in range(1, diamond + 1, 2):
    spaces = (diamond - i) // 2
    print(' ' * spaces + '*' * i)

for i in range(diamond - 2, 0, -2):
    spaces = (diamond - i) // 2
    print(' ' * spaces + '*' * i)
