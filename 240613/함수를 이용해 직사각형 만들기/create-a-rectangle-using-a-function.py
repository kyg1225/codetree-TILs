def printo(x, y):
    for _ in range(x):
        print('1'*y)

r, c = map(int, input().split())
printo(r, c)