def smallest(n1, n2, n3):
    mini = n1
    if mini > n2:
        mini = n2
    if mini > n3:
        mini = n3
        
    print(mini)
    

a, b, c = map(int, input().split())
smallest(a, b, c)