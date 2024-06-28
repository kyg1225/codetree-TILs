MAX_R = 200000
robot = 100000

n = int(input())
segments = [tuple(input().split()) for _ in range(n)]
black = [0]*(MAX_R+1)
white = [0]*(MAX_R+1)
checked = [0]*(MAX_R+1)

for x, d in segments:
    x = int(x)
    if d == 'L':
        while x > 0:
            checked[robot] = 1
            white[robot] += 1
            x -= 1

            if x:
                robot -= 1
    else:
        while x > 0:
            checked[robot] = 2
            black[robot] += 1
            x -= 1

            if x:
                robot += 1


b, w, g = 0, 0, 0
for i in range(MAX_R+1):
    if black[i]>=2 and white[i]>= 2:
        g += 1
    elif checked[i]==2:
        b+=1
    elif checked[i]==1:
        w+=1

print(w, b, g)