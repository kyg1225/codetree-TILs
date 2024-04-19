n = int(input())

maps = [[1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            pass
        elif j == 0:
            pass
        else:
            maps[i][j] = maps[i-1][j] + maps[i][j-1] + maps[i-1][j-1]

for i in maps:
    print(*i)