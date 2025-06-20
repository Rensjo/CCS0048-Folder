#Name: Jorens Ivan C Rance
#School: FEU-TECH
#Machine Problem number - 2

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def compute_area(self):
        return math.pi * (self.radius ** 2)
    
    def compute_perimeter(self):
        return 2 * math.pi * self.radius

def get_positive_integer(prompt):
    while True:
        try:
            value = input(prompt)
            
            # Check for negative values
            if '-' in value:
                print("You use enter positive number")
                continue

            # Check if it's an integer value
            if '.' in value:
                print("You use input whole number value:")
                continue

            value = int(value)

            if value <= 0:
                print("You use enter positive number")
            else:
                return value
        except ValueError:
            print("You use input whole number value:")

# Main Program
if __name__ == "__main__":
    radius = get_positive_integer("Enter radius:")
    
    circle = Circle(radius)
    area = circle.compute_area()
    perimeter = circle.compute_perimeter()
    
    print(f"The answer is {round(area, 1)}")
    print(f"Here is the Answer: {perimeter}")
