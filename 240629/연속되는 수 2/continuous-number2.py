n = int(input())
n_list = [(int(input())) for _ in range(n)]

result, cnt = 0, 0
for i in range(n):
    if i>=1 and n_list[i] == n_list[i-1]:
        cnt += 1
    else:
        cnt = 1
    result = max(result, cnt)
print(result)