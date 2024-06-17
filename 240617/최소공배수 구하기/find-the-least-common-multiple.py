def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return int(gcd(b, a%b))
        
def lcm(a, b):
    return int((a*b)/gcd(a, b))

n, m = map(int, input().split())

print(lcm(n, m))