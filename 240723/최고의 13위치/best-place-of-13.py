n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

max_v = 0
for i in range(n):
    for j in range(n-2):
        max_v = max(max_v, maps[i][j]+maps[i][j+1]+maps[i][j+2])

print(max_v)