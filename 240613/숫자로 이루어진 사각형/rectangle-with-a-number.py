def printo(x):
    n = 1
    for _ in range(x):
        for _ in range(x):
            print(n,end=' ')
            n+=1
            if n == 10:
                n = 1
        print()

n = int(input())
printo(n)