def total(n1, n2):
    total = 0
    for i in range(n1, n2+1):
        if is_prime(i)==True:
            total+=i
    return total

def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True


a, b = map(int, input().split())
print(total(a, b))