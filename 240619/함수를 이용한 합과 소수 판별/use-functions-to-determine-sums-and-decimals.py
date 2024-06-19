def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def is_jjack(n):
    return True if (n//10 + n%10)%2 == 0 else False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_prime(i)==True and is_jjack(i)==True:
        cnt+=1
print(cnt)