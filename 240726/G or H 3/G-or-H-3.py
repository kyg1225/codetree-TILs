INT_MAX = 1000000

n, k = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
placed = [0] * (INT_MAX + 1)

for elem in arr:
    if elem[1]=='G':
        placed[int(elem[0])] = 1
    else:
        placed[int(elem[0])] = 2

max_cnt = 0
for i in range(n - k + 1):
    num = 0
    for j in range(i, i + k):
        num += placed[j]
    max_cnt = max(max_cnt, num)

print(max_cnt+1)