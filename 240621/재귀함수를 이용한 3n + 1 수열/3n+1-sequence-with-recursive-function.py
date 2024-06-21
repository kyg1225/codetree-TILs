n = int(input())

def seq(n):
    if n == 1:
        return 0
    if n%2==0:
        return seq(n//2) + 1
    if n%2==1:
        return seq((n*3)+1) + 1

print(seq(n))