n = int(input())
students_grades = {}

for i in range(n):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student, grade in students_grades.items():
    string_of_grade = ''
    for g in grade:
        if len(str(g)) == 3:
            g = str(g) + "0"
        string_of_grade += str(g) + " "
    avg = sum(grade)/len(grade)

    print(f"{student} -> {string_of_grade}(avg: {avg:.2f})")

# (avg: {(sum(grade)/len(grade)):.2f}")