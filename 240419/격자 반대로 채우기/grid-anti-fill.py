n = int(input())

maps = [[0]*n for _ in range(n)]

nums = 1
for i in range(n-1,-1,-1):
    if (n-1-i)%2 == 0:
        for j in range(n-1, -1, -1):
            maps[j][i] = nums
            nums += 1
    else:
        for j in range(n):
            maps[j][i] = nums
            nums += 1

for i in maps:
    print(*i)