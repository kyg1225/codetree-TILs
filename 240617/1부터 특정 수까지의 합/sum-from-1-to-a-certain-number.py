def addiv(a):
    total = 0
    for i in range(1,a+1):
        total += i
    return int(total/10)

n = int(input())
print(addiv(n))