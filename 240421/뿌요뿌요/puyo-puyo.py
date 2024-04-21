n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

max_block, bomb_cnt = 0, 0
cur_block_num = 0

def is_safe(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, color):
    if not is_safe(x, y):
        return False
    if visited[x][y] or maps[x][y] != color:
        return False
    return True

def dfs(x, y):
    global cur_block_num

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for ddx, ddy in zip(dx, dy):
        nx, ny = x + ddx, y + ddy

        if can_go(nx, ny, maps[x][y]):
            visited[nx][ny] = 1
            cur_block_num += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j]:
            visited[i][j] = 1
            cur_block_num = 1

            dfs(i, j)

            if cur_block_num >= 4:
                bomb_cnt += 1
            
            max_block = max(max_block, cur_block_num)

print(bomb_cnt, max_block)