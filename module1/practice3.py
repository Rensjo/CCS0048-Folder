def get_student_input():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    math_grade = float(input("Enter grade for Math: "))
    english_grade = float(input("Enter grade for English: "))
    science_grade = float(input("Enter grade for Science: "))
    print(f"Student {name} added successfully!")
    return name, age, math_grade, english_grade, science_grade

def calculate_average(math_grade, english_grade, science_grade):
   average = (math_grade + english_grade + science_grade) / 3
   return round(average, 2)

def determine_grade_category(average):
    if 90 <= average <= 100:
        return "Excellent"
    elif 80 <= average <= 89:
        return "Very Good"
    elif 70 <= average <= 79:
        return "Good"
    elif 60 <= average <= 69:
        return "Needs Improvement"
    elif average < 60:
        return "Fail"
    
def add_student(gradebook):
    name, age, math_grade, english_grade, science_grade = get_student_input()
    average = calculate_average(math_grade, english_grade, science_grade)
    category = determine_grade_category(average)
    student = {
        'Name': name,
        'Age': age,
        'Math': math_grade,
        'English': english_grade,
        'Science': science_grade,
        'Average': average,
        'Grade Category': category
    }
    
    gradebook.append(student)



def display_gradebook_summary(student):
    print(f"{'Name: ':<15} {student['Name']}")
    print(f"{'Age: ':<15} {student['Age']}")
    print(f"{'Math: ':<15} {student['Math']}")
    print(f"{'English: ':<15} {student['English']}")
    print(f"{'Science: ':<15} {student['Science']}")
    print(f"{'Average: ':<15} {student['Average']}")
    print(f"{'Grade Category: ':15} {student['Grade Category']}")
    return


def show_menu():
    print("--- STUDENT GRADEBOOK SYSTEM ---")
    print("1. Add new student")
    print("2. View gradebook summary")
    print("3. Exit")
    choice = int(input("Enter your choice (1/2/3): "))
    return choice


    


def main():
    gradebook = []

    while True:
        choice = show_menu()
        
        if choice == 1:
            add_student(gradebook)

        elif choice == 2:
            if gradebook:
                for student in gradebook:
                    print("\n===== GRADEBOOK SUMMARY =====")
                    display_gradebook_summary(student)
            else:
                print("No student records yet. Please add students first.")

        elif choice == 3:
            print("Thank you for using the Student Gradebook System. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
            
main()


