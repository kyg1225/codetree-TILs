n = int(input())
moving = [tuple(input().split()) for _ in range(n)]
checked = [0]*21

for x, p in moving:
    if p=='R':
        for i in range(int(x), int(x)+int(x)):
            checked[i]+=1
    else:
        for i in range(int(x), 0,-1):
            checked[i]+=1
cnt = 0
for i in checked:
    if i>=2:
        cnt+=1
        
print(cnt)