n = int(input())
s = list(input() for _ in range(n))

add = 0
cnt = 0
for i in s:
    if i[0] == 'a':
        cnt += 1
    add += len(i)

print(add, cnt)