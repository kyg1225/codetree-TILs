arr = list(input())

x, y, dir_num = 0, 0, 0
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

t = 0 
for i in range(len(arr)):
    if arr[i] == 'L':
        dir_num = (dir_num + 3)%4
        t+=1
    elif arr[i] == 'R':
        dir_num = (dir_num + 1)%4
        t+=1
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]
        t+=1
    if x==0 and y==0:
        print(t)
        break
if x!=0 or y!=0:
    print(-1)