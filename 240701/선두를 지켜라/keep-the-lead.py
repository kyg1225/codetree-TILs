MAX_T = 1000000
n, m = map(int, input().split())

a_vt, b_vt = [0]*(MAX_T+1), [0]*(MAX_T+1)

time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a_vt[time_a] = a_vt[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b_vt[time_b] = b_vt[time_b - 1] + v
        time_b += 1

wins = []
cnt = 0
for i in range(1, time_a):
    if a_vt[i] > b_vt[i]:
        if wins == 2:
            cnt += 1
        wins = 1
    elif a_vt[i] < b_vt[i]:
        if wins == 1:
            cnt += 1
        wins = 2

print(cnt)