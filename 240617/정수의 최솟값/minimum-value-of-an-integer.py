def smallest(n1, n2, n3):
    if n1 < n2:
        if n1 < n3 or n1 == n3:
            print(n1)
    elif n2 < n1:
        if n2 < n3 or n2 == n3:
            print(n2)
    elif n3 < n1:
        if n3 < n2 or n3 == n2:
            print(n1)
    

a, b, c = map(int, input().split())
smallest(a, b, c)