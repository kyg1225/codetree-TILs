n = int(input())

students = {'Bessie':0, 'Elsie':0, 'Daisy':0, 'Gertie':0, 'Annabelle':0, 'Maggie':0, 'Henrietta':0}
total = [0, 0, 0, 0, 0, 0, 0]

for i in range(n):
    name, score = input().split()
    students[name] += int(score)

maxi = [name for name, score in students.items() if max(students.values()) == score]

print('Tie' if len(maxi) >= 2 else maxi)