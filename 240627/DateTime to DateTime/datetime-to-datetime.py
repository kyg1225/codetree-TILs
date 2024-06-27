a, b, c = map(int, input().split())

if a <= 11 and b <= 11 and c < 11:
    print(-1)
else:
    d = (a - 11)*24*60
    h = (b - 11)*60
    m = c- 11
    print(d+h+m)