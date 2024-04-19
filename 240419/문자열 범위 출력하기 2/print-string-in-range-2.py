s = input()
n = int(input())

if len(s) < n:
    print(s[::-1])
else:
    for i in range(len(s)-1, -1, -1):
        if n!=0:
            print(s[i],end='')
            n-=1