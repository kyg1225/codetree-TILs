OFFSET = 0
MAX_R = 10

rects = [tuple(map(int, input().split())) for _ in range(3)]
checked = [[0]*(MAX_R+1) for _ in range(MAX_R+1)]

for idx, (x1, y1, x2, y2) in enumerate(rects):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET
    
    if idx == 2:
        for x in range(x1, x2):
            for y in range(y1, y2):
                checked[x][y] = 0
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                checked[x][y] = 1
    
cnt = 0
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y]==1:
            cnt += 1
print(cnt)
# for i in range(MAX_R+1):
#     print(checked[i])