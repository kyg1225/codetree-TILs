n = int(input())


maps = []
for i in range(1, n+1):
    for j in range(i+1):
        maps.append([1]*j)
maps = maps[-n:]

for i in range(1, n):
    for j in range(i):
        if j == 0:
            maps[i][j] = 1
        else:
            maps[i][j] = maps[i-1][j-1] + maps[i-1][j]

for i in maps:
    print(*i)