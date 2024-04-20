s = input()

result = s
for i in range(len(s)+1):
    if i == 0 or i==len(s)+1:
        print(s)
    else:
        result = s[-i:] + s[:-i]
        print(result)