n = int(input())

s = list(input().split())
s = list(''.join(s))

for i in range(1, len(s)):
    if i%5 == 0:
        print(''.join(s[i-5:i]))
print(''.join(s[-(len(s)%5):]))