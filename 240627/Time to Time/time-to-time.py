a, b, c, d = map(int, input().split())

h = c - a
if d < b:
    m = b - d
    print(h*60 - m)
else:
    m = d - b
    print(h*60 + m)