n = int(input())

def get_sum(n):
    if n==0:
        return 1
    if n%2==0:
        return get_sum(n//2)+n
    else:
        return get_sum(n//2)+n

print(get_sum(n))