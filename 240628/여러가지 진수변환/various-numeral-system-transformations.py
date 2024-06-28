n, b = map(int, input().split())

result = []
while True:
    if n<b:
        result.append(n)
        break
    result.append(n%b)
    n//=b

for i in result[::-1]:
    print(i, end='')