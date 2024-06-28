MAX_R = 100

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
checked = [0]* (MAX_R+1)

for x1, x2 in segments:
    for i in range(x1, x2+1):
        checked[i] += 1

print(max(checked))