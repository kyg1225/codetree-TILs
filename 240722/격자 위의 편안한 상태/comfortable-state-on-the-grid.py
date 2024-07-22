n, m = map(int, input().split())

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
maps = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def check_color(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and maps[nx][ny]==1:
            cnt+=1
    return cnt

for i in range(m):
    x, y = map(int, input().split())
    maps[x-1][y-1] = 1
    if check_color(x-1, y-1)==3:
        print(1)
    else:
        print(0)