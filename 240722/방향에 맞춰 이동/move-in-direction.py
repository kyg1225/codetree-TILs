n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0

for i in range(n):
    direction, dir_num = input().split()
    if direction == 'E':
        for j in range(int(dir_num)):
            x, y = x+dx[0], y+dy[0]
    elif direction == 'S':
        for j in range(int(dir_num)):
            x, y = x+dx[1], y+dy[1]
    elif direction == 'W':
        for j in range(int(dir_num)):
            x, y = x+dx[2], y+dy[2]
    else:
        for j in range(int(dir_num)):
            x, y = x+dx[3], y+dy[3]

print(x, y)