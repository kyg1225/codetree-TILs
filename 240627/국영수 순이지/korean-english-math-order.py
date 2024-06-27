class Student:
    def __init__ (self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []
for _ in range(n):
    n, k, e, m = map(str, input().split())
    k ,e, m = int(k), int(e), int(m)
    students.append(Student(n, k, e, m))

students.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for student in students:
    print(student.name, student.kor, student.eng, student.math)