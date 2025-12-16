num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

class_total = 0
total_scores = num_students * num_subjects

for student in range(1, num_students + 1):
    print(f"\nStudent {student}")
    student_total = 0

    for subject in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        student_total += score
        class_total += score

    student_average = student_total / num_subjects
    print(f"Average for Student {student} = {student_average}")

class_average = class_total / total_scores
print(f"\nClass Average = {class_average}")
