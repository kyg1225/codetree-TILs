n, t = map(int, input().split())
arr = list(input())
maps = [list(map(int,input().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = n//2, n//2
dir_num = 0

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

total = maps[x][y]
for i in range(t):
    if arr[i]=='L':
        dir_num = (dir_num + 3) % 4
    elif arr[i]=='R':
        dir_num = (dir_num+1)%4
    else:
        nx, ny = x+dxs[dir_num], y+dys[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            total += maps[x][y]

print(total)