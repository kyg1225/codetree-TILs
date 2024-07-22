n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

result = 0
for i in range(n):
    for j in range(n):
        cnt=0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+i+dx, y+j+dx
            if in_range(nx, ny) and maps[nx][ny]==1:
                cnt+=1
        if cnt>=3:
            result+=1
print(result-1)