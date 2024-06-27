n = int(input())
h_sort = []
for i in range(1, n+1):
    h, kg = tuple(map(int, input().split()))
    h_sort.append((h, kg, i))

h_sort.sort(key=lambda x:(-x[0], -x[1], -x[2]))

for h in h_sort:
    print(h[0], h[1], h[2])