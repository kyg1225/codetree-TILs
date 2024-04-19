n, m = map(int, input().split())

coin = [list(map(int, input().split())) for _ in range(m)]
maps = [[0]*n for _ in range(n)]

for i in coin:
    maps[i[0]-1][i[1]-1] = 1

for i in maps:
    print(*i)