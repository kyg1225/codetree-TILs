def get_sum(n):
    if n<10:
        return n
    return get_sum(n//10) + (n%10)

a, b, c = map(int,input().split())
print(get_sum(a*b*c))