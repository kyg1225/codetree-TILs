n = int(input())
maps = [[0]*n for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        maps[j][i] = num
        num += 1

for i in maps:
    print(*i)