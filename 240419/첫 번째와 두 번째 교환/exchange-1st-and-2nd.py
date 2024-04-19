s = input()

a = s[0]
b = s[1]
result = ''
for i in list(s):
    if i == s[0]:
        i = s[1]
    elif i == s[1]:
        i = s[0]
    result += i
print(result)