n, m = map(int, input().split())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, d = 0, 0, 0

maps = [[0]*m for _ in range(n)]
maps[x][y] = 1

def in_range(x, y):
    return 0<=x and x < n and 0<=y and y < m

for i in range(2, n*m + 1):
    nx, ny = x + dxs[d], y + dys[d]
    if not in_range(nx, ny) or maps[nx][ny] !=0:
        d = (d + 1)%4
    x, y = x + dxs[d], y + dys[d]
    maps[x][y] = i

for i in range(n):
    for j in range(m):
        print(maps[i][j], end=' ')
    print()