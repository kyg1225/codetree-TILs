MAX_T = 1000000
n, m = map(int, input().split())

a_vt, b_vt = [0]*(MAX_T+1), [0]*(MAX_T+1)

time_a = 0
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a_vt[time_a] += v
        time_a += 1

time_b = 0
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b_vt[time_b] += v
        time_b += 1

wins = 'B'
cnt = 0
for i in range(time_a):
    if a_vt[i] > b_vt[i]:
        if wins != 'A':
            wins = 'A'
            cnt += 1
    elif a_vt[i] < b_vt[i]:
        if wins != 'B':
            wins = 'B'
            cnt += 1
print(cnt)