n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if (i+1)%2==1:
        tmp = sorted(arr[:i+1])
        print(tmp[i//2], end=' ')