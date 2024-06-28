MAX_R = 2000

n = int(input())
moving = [tuple(input().split()) for _ in range(n)]
checked = [0]*(MAX_R+1)

cur = 1000
for x, d in moving:
    if d=='R':
        for i in range(int(x)):
            checked[i]+=1
        cur += int(x)
    else:
        for i in range(int(x)):
            checked[i]+=1
        cur -= int(x)

cnt = 0
for i in checked:
    if i>=2:
        cnt+=1
        
print(cnt)