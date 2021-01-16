n = int(input())
student_list = []

for i in range(n):
    student_list.append(input())
student_list = set(student_list)
for student in student_list:
    print(f"{student}")
