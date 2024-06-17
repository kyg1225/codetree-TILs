def add(n1,n2):
    return n1+n2

def minus(n1,n2):
    return n1-n2

def multi(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1//n2


a,o,c = map(str, input().split())
if o == '+':
    print(f'{a} {o} {c} = {add(int(a), int(c))}')
elif o == '-':
    print(f'{a} {o} {c} = {minus(int(a), int(c))}')
elif o == '*':
    print(f'{a} {o} {c} = {multi(int(a), int(c))}')
elif o == '/':
    print(f'{a} {o} {c} = {div(int(a), int(c))}')
else:
    print('False')