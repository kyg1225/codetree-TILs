n = int(input())

dist = []
for i in range(1, n+1):
    x, y = tuple(input().split())
    dist.append((abs(int(x))+abs(int(y)), i))

dist.sort(key=lambda x: (x[0], x[1]))

for d in dist:
    print(d[1])