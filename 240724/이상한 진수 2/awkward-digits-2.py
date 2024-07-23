a = list(input())

max_num, num = 0, 0
cnt = 0

for i in range(len(a)):
    if a[i] == '0' and cnt == 0:
        a[i] = '1'
        cnt += 1
    num += int(a[len(a)-i-1])*2**i
    max_num = max(max_num, num)

print(max_num)