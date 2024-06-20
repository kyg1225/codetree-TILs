n = int(input())

def jegui(n):
    if n==0:
        return 0
    return jegui(n-1) + n

print(jegui(n))