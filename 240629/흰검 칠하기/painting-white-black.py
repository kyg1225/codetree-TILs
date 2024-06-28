MAX_R = 200000
robot = 100000

n = int(input())
segments = [tuple(input().split()) for _ in range(n)]
black = [0]*(MAX_R+1)
white = [0]*(MAX_R+1)
checked = ['']*(MAX_R+1)

for x, d in segments:
    if d == 'L':
        for i in range(int(x)):
            checked[robot] = 'W'
            white[robot] += 1
            robot += 1
    else:
        for i in range(int(x)):
            robot -= 1
            checked[robot] = 'B'
            black[robot] += 1

g = 0
for i in range(MAX_R):
    if black[i]>=2 and white[i]>=2:
        g+=1
        checked[i] = 'G'

b, w = 0, 0
for i in range(MAX_R):
    if checked[i]=='B':
        b+=1
    if checked[i]=='W':
        w+=1

print(w, b, g)