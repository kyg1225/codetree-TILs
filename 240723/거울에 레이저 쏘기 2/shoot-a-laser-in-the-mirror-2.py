n = int(input())
maps = [list(input()) for _ in range(n)]
k = int(input())

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n


def nums_123(x, y):
    dxs, dys = [0,-1, 1, 0], [1, 0, 0, -1]
    dir_num = 2
    result = 1
    while in_range(x, y):
        if maps[x][y]=='\\':
            dir_num = (dir_num+3)%4
            x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
        else:
            dir_num = (dir_num+1)%4
            x, y = x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
    return result+1

def nums_456(x, y):
    dxs, dys = [0,-1, 1, 0], [1, 0, 0, -1]
    dir_num = 3
    result = 1
    while in_range(x, y):
        if maps[x][y]=='\\':
            dir_num = (dir_num+1)%4
            x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
        else:
            dir_num = (dir_num+3)%4
            x, y = x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
    return result+1

def nums_789(x, y):
    dxs, dys = [0,-1, 1, 0], [1, 0, 0, -1]
    dir_num = 1
    result = 1
    while in_range(x, y):
        if maps[x][y]=='\\':
            dir_num = (dir_num+3)%4
            x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
        else:
            dir_num = (dir_num+1)%4
            x, y = x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
    return result+1

def nums_101112(x, y):
    dxs, dys = [0,-1, 1, 0], [1, 0, 0, -1]
    dir_num = 0
    result = 1
    while in_range(x, y):
        if maps[x][y]=='\\':
            dir_num = (dir_num+1)%4
            x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
        else:
            dir_num = (dir_num+3)%4
            x, y = x, y = x+dxs[dir_num], y+dys[dir_num]
            result += 1
    return result+1

if 1<= k < 4:
    dir_num = 2
    x, y = 0, k-1
    print(nums_123(x, y))
    
elif k < 7:
    dir_num = 3
    x, y = k-4, 2
    print(nums_456(x, y))

elif k < 10:
    dir_num = 0
    x, y = abs(k-9), 0
    print(nums_789(x, y))

else:
    dir_num = 1
    x, y = 2, abs(k-12)
    print(nums_101112(x, y))