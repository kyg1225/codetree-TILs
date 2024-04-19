n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(m)]

grid = [[0]*n for _ in range(n)]

for point in points:
    grid[point[0]-1][point[1]-1] = point[0]*point[1]

for i in grid:
    print(*i)