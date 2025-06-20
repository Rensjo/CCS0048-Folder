def get_user_input():
    """Get user input for name, age, weight, and height."""
    name = input("Enter your Name: ")
    age = int(input("Enter your Age: "))
    weight = float(input("Enter your Weight (in kg): "))
    height = float(input("Enter your Height (in m): "))
    return name, age, weight, height

def calculate_bmi(weight, height):
    """Calculate BMI and round to 2 decimal places."""
    bmi = weight / height**2
    return round(bmi, 2)

def determine_bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def is_registration_eligible(age):
    """Check if user is eligible to register (age >= 12)."""
    return age >= 12

def print_user_profile(profile):
    """Print the formatted user profile."""
    print("\n===== USER PROFILE =====")
    for key, value in profile.items():
        print(f"{key:<15} {value}")

def main():
    profile = {}  # To store user profile information
    
    while True:
        # Menu options
        print("\n--- MAIN MENU ---")
        print("1. Register and Calculate BMI")
        print("2. View Profile Summary")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Get user input
            name, age, weight, height = get_user_input()
            bmi = calculate_bmi(weight, height)
            bmi_category = determine_bmi_category(bmi)
            
            # Check registration
            if is_registration_eligible(age):
                registration = "Eligible"
            else:
                registration = "Not eligible (underage)"
                print("You are not yet eligible to register.")
            
            # Save to profile
            profile = {
                'Name:': name,
                'Age:': age,
                'Weight:': f"{weight} kg",
                'Height:': f"{height} m",
                'BMI:': bmi,
                'BMI Category:': bmi_category,
                'Registration:': registration
            }
            print("\nRegistration and BMI calculation completed!")
        
        elif choice == '2':
            if profile:
                print_user_profile(profile)
            else:
                print("No profile data available. Please register first.")
        
        elif choice == '3':
            print("Thank you for using the program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Run the main program
main()

