n =int(input())

sorting = []
for _ in range(n):
    name, height, kg = tuple(input().split())
    sorting.append((name, int(height), int(kg)))

sorting.sort(key=lambda x: (x[1], -x[2]))

for s in sorting:
    print(s[0],s[1],s[2])