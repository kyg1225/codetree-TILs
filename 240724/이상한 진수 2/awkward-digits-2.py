a = list(input())
# a = [int(i) for i in a]

max_num, num = 0, 0
cnt = 0

for i in range(len(a)):
    if '0' in a and a[i] == '0' and cnt == 0:
        a[i] = '1'
        cnt += 1
    elif '0' not in a and cnt==0:
        a[len(a)-1]='0'
        cnt+=1
    num = int(''.join(a), 2)
    max_num = max(max_num, num)

print(max_num)