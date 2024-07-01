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

ans = 0
for i in range(1, time_b):
    if a_vt[i] > b_vt[i]:
        ans += 1
print(ans)