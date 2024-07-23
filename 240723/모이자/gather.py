import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_sum = INT_MAX
for i in range(n):
    nb_sum = 0
    for j in range(n):
        nb_sum += arr[j]*abs(j-i)
    min_sum = min(min_sum, nb_sum)

print(min_sum)