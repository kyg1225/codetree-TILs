n = int(input())

def print_n1(n):
    if n==0:
        return
    print_n1(n-1)
    print(n, end=' ')

def print_n2(n):
    if n==0:
        return
    print(n, end=' ')
    print_n2(n-1)

print_n2(n)
print_n1(n)