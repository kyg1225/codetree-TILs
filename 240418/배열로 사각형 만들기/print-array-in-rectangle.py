maps = [[1]*5 for _ in range(5)]

for i in range(1, 5):
    for j in range(1, 5):
        maps[i][j] = maps[i][j-1] + maps[i-1][j]

for i in maps:
    print(*i)