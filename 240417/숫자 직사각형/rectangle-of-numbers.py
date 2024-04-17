n, m = map(int, input().split())

maps = [[0]*m for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        maps[i][j] += num
        num += 1

for i in maps:
    print(*i)