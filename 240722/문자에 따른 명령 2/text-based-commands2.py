lr_f = input()

dir_num = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

if lr_f[0]=='L':
    dir_num = (dir_num-1+4)%4
    x, y = x + dx[dir_num] , y + dy[dir_num]
elif lr_f[0]=='R':
    dir_num = (dir_num+1)%4
    x, y = x + dx[dir_num] , y + dy[dir_num]

print(x, y)