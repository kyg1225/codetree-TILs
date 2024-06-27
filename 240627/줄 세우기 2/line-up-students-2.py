n = int(input())

students = []
for i in range(n):
    height, kg = tuple(input().split())
    students.append((int(height), int(kg), i+1))

students.sort(key=lambda x:(x[0],-x[1]))

for student in students:
    print(student[0], student[1], student[2])