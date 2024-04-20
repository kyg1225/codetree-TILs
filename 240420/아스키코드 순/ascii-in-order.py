n = int(input())
s = list(input() for _ in range(n))

maxi = ''
for i in range(len(s)-1):
    if ord(s[i][0])>ord(s[i+1][0]):
        maxi = s[i+1]

print(maxi)