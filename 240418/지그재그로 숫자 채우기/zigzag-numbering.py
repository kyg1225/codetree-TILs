n, m = map(int, input().split())
maps = [[0]*m for _ in range(n)]

num = 0
for i in range(m):
    for j in range(n):
        if i%2 == 0:
            maps[j][i] = num
        else:
            maps[n-1-j][i] = num
        num+=1

for i in maps:
    print(*i)