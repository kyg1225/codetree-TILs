s = list(input())

for i in range(len(s)):
    if i == 1 or i == len(s)-2:
        pass
    else:
        print(s[i],end='')