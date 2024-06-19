def change_abs(n):
    print(abs(n), end=' ')


n = int(input())
list_n = list(map(int, input().split()))

for i in list_n:
    change_abs(i)