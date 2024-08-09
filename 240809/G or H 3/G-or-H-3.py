INT_MAX = 1000000

n, k = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
placed = [0] * (INT_MAX + 1)

for elem in arr:
    placed[int(elem[0])]=(1 if elem[1]=='G' else 2)

max_cnt = 0
for i in range(1, n-k+2):
    num = 0
    for j in range(i, i+k):
        num += placed[j]
    max_cnt = max(max_cnt, num)
print(max_cnt+1)