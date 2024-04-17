arr1 = [list(map(int, input().split())) for _ in range(3)]
tmp = input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

maps = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        maps[i][j] += (arr1[i][j]*arr2[i][j])

for i in maps:
    print(*i)