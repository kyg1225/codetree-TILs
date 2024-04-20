s = list(input())

s.remove(s[1])
s.remove(s[-2])
print(''.join(s))