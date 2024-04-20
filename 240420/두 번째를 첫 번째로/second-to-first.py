s = input()
result = ''
for i in s:
    if i == s[1]:
        result += s[0]
    else:
        result += i

print(result)