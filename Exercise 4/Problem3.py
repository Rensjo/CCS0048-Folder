#Name: Jorens Ivan C Rance
#School: FEU-TECH
#Machine Problem number - 3

class RomanConverter:
    def __init__(self):
        self.roman_numeral_map = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

    def int_to_roman(self, num):
        result = ""
        for roman, value in self.roman_numeral_map:
            while num >= value:
                result += roman
                num -= value
        return result

    def roman_to_int(self, roman):
        roman = roman.upper()
        i = 0
        num = 0
        while i < len(roman):
            # Check for 2-character numeral first
            if i + 1 < len(roman) and roman[i:i+2] in dict(self.roman_numeral_map):
                num += dict(self.roman_numeral_map)[roman[i:i+2]]
                i += 2
            else:
                num += dict(self.roman_numeral_map)[roman[i]]
                i += 1
        return num

def get_integer_input(prompt):
    while True:
        try:
            value = input(prompt)
            if '.' in value:
                print("Please enter a whole number value.")
                continue
            value = int(value)
            if value <= 0:
                print("Please enter a positive integer.")
            elif value > 5000:
                print("MAX VALUE IS 5000.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

def main():
    converter = RomanConverter()
    while True:
        print("\nMENU")
        print("1. convert an integer to a roman numeral")
        print("2. convert a roman numeral to an integer")
        print("3. exit\n")

        choice = input("Enter your choice:")

        if choice == '1':
            num = get_integer_input("Enter Integer - ")
            roman = converter.int_to_roman(num)
            print(f"Output in Roman numerals is: {roman}")

        elif choice == '2':
            roman_input = input("Enter roman numeral - ")
            roman_input_upper = roman_input.upper()

            valid_roman_chars = set('IVXLCDM')
            if all(char in valid_roman_chars for char in roman_input_upper):
                integer_value = converter.roman_to_int(roman_input_upper)
                print(f"Output in Integer is - {integer_value}")
            else:
                print("Invalid Roman numeral input. Please try again.")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
