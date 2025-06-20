

units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("You must Enter a value greater or equal to zero")
else:
    if units <= 100:
        bill = float(units*5.0)
        print("Initial bill: ", bill)
    elif units <= 200:
        bill = float(units*7.0)
        print("Initial bill: ", bill)
    elif units > 201:
        bill = float(units*10.0)
        print("Initial bill: ", bill)

if bill >= 2000:
    discount = bill*0.05
    print("Discount Applied: ", discount)
    print("Final Payable Amount: ", bill+discount)
elif bill < 2000:
    print("Final Payable Amount: ", bill)



