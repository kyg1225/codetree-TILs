n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

x = [i for i in range(1, n)]
y = [i for i in range(1, n)]
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n


cnt, result = 0, 0
for i in range(n-1):
    for j in range(n-1):
        if cnt >= 3:
            result += 1
            cnt=0
        for dx, dy in zip(dxs, dys):
            nx, ny = x[i]+dx, y[j]+dx
            # print(nx, ny)
            if in_range(nx, ny) and maps[nx][ny]==1:
                cnt+=1
print(result)