n = int(input())

maps = [[0]*n for _ in range(n)]

nums = n*n
for i in range(n):
    for j in range(n-1, -1, -1):
        if i%2 == 0:
            maps[j][i] = nums
        else:
            maps[n-1-j][i] = nums
        nums -= 1

for i in maps:
    print(*i)