MAX_R = 200000
tile = 100000

n = int(input())
checked = [0]*(MAX_R+1)

for _ in range(n):
    x, d = input().split()
    x = int(x)
    # white
    if d == 'L':
        while x > 0:
            checked[tile] = 1
            x -= 1

            if x:
                tile -= 1
    else: # black
        while x > 0:
            checked[tile] = 2
            x -= 1

            if x:
                tile += 1

cnt_w, cnt_b = 0, 0
for i in checked:
    if i==1:
        cnt_w += 1
    elif i==2:
        cnt_b += 1

print(cnt_w, cnt_b)