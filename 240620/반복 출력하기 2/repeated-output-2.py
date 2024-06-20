def print_world(n):
    if n == 0:
        return
    print('HelloWorld')
    print_world(n-1)

n = int(input())
print_world(n)