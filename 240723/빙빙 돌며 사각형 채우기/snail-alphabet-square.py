n, m = map(int, input().split())
arr = [['']*m for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir_num = 1
arr[0][0] = chr(65)

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

alpha = 66
for i in range(66, n*m+65):
    nx, ny = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny]!= '':
        dir_num = (dir_num+1)%4
    if chr(alpha)=='[':
        alpha = 65
    x, y = x + dxs[dir_num], y+dys[dir_num]
    arr[x][y] = chr(alpha)
    alpha+=1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()