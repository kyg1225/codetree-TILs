s = input()
condi = input()

for i in condi:
    if i == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]
print(s)