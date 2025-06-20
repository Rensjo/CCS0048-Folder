
Letter_grade = input("Enter your Letter Grade:")

if Letter_grade in ("A+", "A"):
    grade_point = 4.0
elif Letter_grade == "A-":
    grade_point = 3.7
elif Letter_grade == "B+":
    grade_point = 3.3
elif Letter_grade == "B":
    grade_point = 3.0
elif Letter_grade == "B-":
    grade_point = 2.7
elif Letter_grade == "C+":
    grade_point = 2.3
elif Letter_grade == "C":
    grade_point = 2.0
elif Letter_grade == "C-":
    grade_point = 1.7
elif Letter_grade == "D+":
    grade_point = 1.3
elif Letter_grade == "D":
    grade_point = 1.0
elif Letter_grade == "F":
    grade_point = 0
else:
    print("Invalid Grade Entered")

if grade_point is not None:
    print("For this grade, you will receive a grade points of", grade_point)