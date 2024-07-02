MAX_T = 20

n, m = map(int, input().split())
pos_a, pos_b = [0]*(MAX_T+1), [0]*(MAX_T+1)

time_a = 1
for _ in range(n):
    t, d = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a-1] + (1 if d=='R' else -1)
        time_a += 1
    
time_b = 1
for _ in range(m):
    t, d = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b-1] + (1 if d=='R' else -1)
        time_b += 1

cnt = 0
for i in range(1, len(pos_a)):
    if pos_a[i] == pos_b[i] and pos_a[i-1] != pos_b[i-1]:
        cnt+=1

print(cnt)