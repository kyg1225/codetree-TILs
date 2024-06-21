n = int(input())
info = sorted([list(map(str, input().split())) for _ in range(n)])
# info = sorted(info)

for i in info:
    if i[2] == 'Rain':
        print(' '.join(i))
        break