s = list(input())
s[1], s[-2] = 'a', 'a'

print(''.join(s))