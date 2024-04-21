def is_safe(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not is_safe(x, y):
        return False

    if visited[x][y] or maps[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    visited[x][y] = 1
    dx, dy = [0, 1], [1, 0]

    for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                dfs(nx, ny)


n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

dfs(0, 0)
print(visited[n-1][m-1])