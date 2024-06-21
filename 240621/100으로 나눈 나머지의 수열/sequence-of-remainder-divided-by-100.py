n = int(input())

def seq(a):
    if a == 1:
        return 2
    if a == 2:
        return 4
    
    return (seq(a-1)*seq(a-2))%100

print(seq(n))