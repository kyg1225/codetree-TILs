OFFSET = 100
MAX_R = 200

n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]
checked = [[0]*(MAX_R+1) for _ in range(MAX_R+1)]

for x1, y1 in rects:
    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            checked[x][y] = 1
cnt = 0
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y]:
            cnt += 1

print(cnt)