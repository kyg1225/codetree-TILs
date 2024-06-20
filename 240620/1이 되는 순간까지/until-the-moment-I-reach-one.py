n = int(input())

def work(n):
    if n==1:
        return n-1
    if n%2==0:
        return work(n//2)+1
    elif n%2==1:
        return work(n//3)+1

print(work(n))