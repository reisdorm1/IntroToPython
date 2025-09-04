# Step 1: Initialize student data
student_grades = {
    "Robert": [85, 92, 78],
    "William": [70, 88, 84],
    "Mia": [95, 91, 100]
}

# Step 2: Calculate average grades
student_averages = {}
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    student_averages[student] = average

# Step 3: Determine letter grades
student_letter_grades = {}
for student, average in student_averages.items():
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    student_letter_grades[student] = letter\
# Step 4: Find the top performer
top_student = None
top_average = 0
for student, average in student_averages.items():
    if average > top_average:
        top_student = student
        top_average = average

print(f"Top performer: {top_student} with an average grade of {top_average:.2f}")

# Step 5: Calculate class statistics
total_average = sum(student_averages.values()) / len(student_averages)

passing_count = 0
for grade in student_letter_grades.values():
    if grade in ["A", "B", "C"]:
        passing_count += 1

print(f"Class average: {total_average:.2f}")
print(f"Number of students passing (C or better): {passing_count}")