a, b = map(int, input().split())
n = list(input())

tmp = 0
for i in range(len(n)):
    tmp = tmp*a + int(n[i])

result = []
while True:
    if tmp<b:
        result.append(tmp)
        break
    result.append(tmp%b)
    tmp //= b

for i in result[::-1]:
    print(i, end='')