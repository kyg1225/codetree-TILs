def swap(n, m):
    n, m = m, n
    print(n, m)
    
n, m = map(int, input().split())
swap(n, m)