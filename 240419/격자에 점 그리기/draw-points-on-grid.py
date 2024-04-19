n, m = map(int, input().split())

points = [list(map(int, input().split())) for _ in range(m)]
maps = [[0]*n for _ in range(n)]
num = 1

for point in points:
    maps[point[0]-1][point[1]-1] = num
    num += 1

for i in maps:
    print(*i)