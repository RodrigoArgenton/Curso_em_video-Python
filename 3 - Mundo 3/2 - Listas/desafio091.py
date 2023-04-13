students = []
student = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])


students = sorted(students, key=lambda alunos: alunos[1], reverse=True)
for a in students:
    if a[1] == students[1][1]:
        student.append(a)
student = sorted(student)
print(student)

for a in student:
    print(a[0])