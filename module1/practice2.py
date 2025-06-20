name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
weight = float(input("Enter your Weight (in kg): "))
height = float(input("Enter your Height (in m): "))

bmi = weight / height**2
bmi = round(bmi, 2)

registration = "Not eligible (Underage)"
bmi_category = "N/A"

if age >= 12:
    registration =  "Eligible"
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_category = "Normal"
    elif 25 <= bmi < 30:
        bmi_category = "Overweight"
    elif bmi >= 30:
        bmi_category = "Obese"
else:
    print("You are not yet eligible to register.")

print("\n===== USER PROFILE =====")
print(f"{'Name:':<15} {name}")
print(f"{'Age:':<15} {age}")
print(f"{'Weight:':<15} {weight} kg")
print(f"{'Height:':<15} {height} m")
print(f"{'BMI:':<15} {round(bmi, 2)}")
print(f"{'BMI Category:':<15} {bmi_category}")
print(f"{'Registration:':<15} {registration}")
