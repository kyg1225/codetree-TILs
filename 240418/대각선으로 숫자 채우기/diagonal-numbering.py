n, m = map(int, input().split())


nums = 1
maps = [[0]*m for _ in range(n)]

# Step 1
for start_col in range(m):
    cur_row = 0
    cur_col = start_col

    while 0 <= cur_col and cur_row < n:
        maps[cur_row][cur_col] = nums

        # 변수 업데이트
        cur_row += 1
        cur_col -= 1
        nums += 1

# Step 2
for start_row in range(1, n):
    cur_row = start_row
    cur_col = m - 1

    while 0 <= cur_col and cur_row < n:
        maps[cur_row][cur_col] = nums

        # 변수 update
        cur_row += 1
        cur_col -= 1
        nums += 1

for i in maps:
    print(*i)