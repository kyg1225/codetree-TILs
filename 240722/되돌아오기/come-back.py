n = int(input())

dir_dic = {
    'N':0,
    'E':1,
    'S':2,
    'W':3
}

x, y, d_num = 0, 0, 0
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

cnt = 0
for i in range(n):
    d, f = input().split()
    d_num = dir_dic[d]
    for j in range(int(f)):
        x, y = x + dxs[d_num], y + dys[d_num]
        cnt += 1
        if x == 0 and y == 0:
            print(cnt)
            break
    if x==0 and y==0:
        break
        
if x!=0 and y!=0:
    print(-1)