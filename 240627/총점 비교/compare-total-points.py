n = int(input())
total = []
for _ in range(n):
    (name, one, two, three) = tuple(input().split())
    total.append((name,int(one),int(two),int(three)))

total.sort(key=lambda x:x[1] + x[2] + x[3])

for t in total:
    name, one, two, three = t
    print(name, one, two, three)