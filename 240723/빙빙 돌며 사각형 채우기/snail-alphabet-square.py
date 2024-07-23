n, m = map(int, input().split())
arr = [['']*m for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir_num = 1
arr[0][0] = chr(65)

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

alpha = 64
for i in range(2, n*m+1):
    nx, ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny]!= '':
        dir_num = (dir_num+1)%4
    x, y = x + dxs[dir_num], y+dys[dir_num]
    if alpha==90:
        alpha = 64
    arr[x][y] = chr(alpha+i)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()