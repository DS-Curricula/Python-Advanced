# Define student GPA and test score
student_gpa = 4.5
student_score = 75

# Check scholarship eligibility using nested conditionals
if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} may be eligible for a partial "
              f"scholarship.")
    elif student_score > 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is eligible for a full scholarship.")
    else:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship.")
else:
    print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship.")
