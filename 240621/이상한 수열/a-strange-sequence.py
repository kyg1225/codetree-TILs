n = int(input())

def what_seq(a):
    if a == 1:
        return 1
    if a==2:
        return 2
    return (what_seq(a//3)+what_seq(a-1))

print(what_seq(n))