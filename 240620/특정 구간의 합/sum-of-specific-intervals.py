def add_all(list_a12):
    result = 0
    for i in range(list_a12[0]-1,list_a12[1]):
        result += list_A[i]
    return print(result)

n, m = map(int, input().split())
list_A = list(map(int, input().split()))
a1_a2 = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    add_all(a1_a2[i])