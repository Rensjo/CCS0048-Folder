
earthquake = float(input("Enter an Earthquake magnitude: "))

if earthquake < 2.0:
    descriptor = "Micro"
elif earthquake < 3.0:
    descriptor = "Very Minor"
elif earthquake < 4.0:
    descriptor = "Minor"
elif earthquake < 5.0:
    descriptor = "Light"
elif earthquake < 6.0:
    descriptor = "Moderate"
elif earthquake < 7.0:
    descriptor = "Strong"
elif earthquake < 8.0:
    descriptor = "Major"
elif earthquake < 10.0:
    descriptor = "Great"
elif earthquake > 10:
    descriptor = "Meteoric"


print("The Earthquake is classified as", descriptor)
