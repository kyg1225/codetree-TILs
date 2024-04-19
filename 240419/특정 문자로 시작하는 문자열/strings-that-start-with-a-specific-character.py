n = int(input())
s = list(input() for _ in range(n))
char = input()

cnt = 0
length = 0
for i in s:
    if i[0] == char:
        cnt += 1
        length += len(i)
print(cnt, f"{length/cnt:.2f}")