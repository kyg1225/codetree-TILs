def is_seq(n1, n2):
    if ''.join(n2) in ''.join(n1):
        return True
    return False

n1, n2 = map(int, input().split())
a = list(map(str, input().split()))
b = list(map(str, input().split()))

if is_seq(a, b)==True:
    print('Yes')
else:
    print('No')