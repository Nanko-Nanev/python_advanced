n = int(input())
student_list = set([])

for i in range(n):
    student_list.add(input())

for student in student_list:
    print(f"{student}")
