n = int(input())
s = list(input() for _ in range(n))

result  = []
for i in s:
    result.append(i[0])

mini = result[0]

for i in result:
    if ord(i)<ord(mini):
        mini=i

print(s[result.index(mini)])