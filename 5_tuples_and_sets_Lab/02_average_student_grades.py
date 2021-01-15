n = int(input())
students_grades = {}

for i in range(n):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = [float(grade)]
    students_grades[student].append(float(grade))

for student, grade in students_grades.items():
    print(f"{student} -> {grade}")

# (avg: {(sum(grade)/len(grade)):.2f}")