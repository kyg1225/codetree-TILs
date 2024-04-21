def is_safe(x, y):
    return 0 <= x < n and 0 <= y < n 

def can_go(x, y):
    if not is_safe(x, y):
        return False
    
    if visited[x][y] or maps[x][y] == 0:
        return False
    
    return True


def dfs(x, y):
    global visited, people_cnt
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for ddx, ddy in zip(dx, dy):
        nx = x + ddx
        ny = y + ddy
        if can_go(nx, ny):
            visited[nx][ny] = 1
            people_cnt += 1
            dfs(nx, ny)

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

people_cnt = 0
people_cnts = list()

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = 1
            people_cnt = 1

            dfs(i, j)
            people_cnts.append(people_cnt)

people_cnts.sort()

print(len(people_cnts))
for i in people_cnts:
    print(i)