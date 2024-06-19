def div_2(i):
    if i%2==0:
        print(i//2, end=' ')
    else:
        print(i, end=' ')

n = int(input())
list_n = list(map(int, input().split()))

for i in list_n:
    div_2(i)