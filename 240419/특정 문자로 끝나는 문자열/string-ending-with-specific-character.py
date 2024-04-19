s = list(input() for _ in range(10))
char = input()

cnt = 0
for i in s:
    if i[-1] == char:
        print(i)
        cnt += 1

if cnt == 0:
    print('None')