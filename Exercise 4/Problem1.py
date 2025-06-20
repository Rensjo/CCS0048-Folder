#Name: Jorens Ivan C. Rance
#School: FEU-TECH
#Machine Problem number - 1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width

def get_positive_integer(prompt):
    while True:
        try:
            value = input(prompt)
            
            # Check for negative values
            if '-' in value:
                print("The number is not a positives integer:")
                continue

            # Check if it's an integer value
            if '.' in value:
                print("Input the correct data format is not a Positive integer:")
                continue

            value = int(value)

            if value <= 0:
                print("The number is not a positives integer:")
            else:
                return value
        except ValueError:
            print("Input the correct data format is not a Positive integer:")

# Main Program
if __name__ == "__main__":
    length = get_positive_integer("Enter Length value:")
    width = get_positive_integer("Enter the width of the rectangle:")
    
    rect = Rectangle(length, width)
    area = rect.compute_area()
    print(f"The Area of the Rectangle is:{area}")
