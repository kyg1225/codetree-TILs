n = int(input())

s = list(input().split())
s = list(''.join(s))

for i in range(1, len(s)+1):
    if i%5 == 0:
        print(''.join(s[i-5:i]))

if len(s)%5 > 0:
    print(''.join(s[-(len(s)%5):]))