def is_palin(s):
    if s[:] == s[::-1]:
        print('Yes')
    else:
        print('No')

a = input()
is_palin(a)