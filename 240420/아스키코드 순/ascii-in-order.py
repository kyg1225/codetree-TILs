n = int(input())
s = list(input() for _ in range(n))

mini = ''
for i in range(len(s)-1):
    if ord(s[i][0]) == 65:
        mini = s[i]

print(mini)