import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

max_result = INT_MIN
for i in range(n-2):
    result = 0
    for j in range(i+2, n):
        result = arr[i] + arr[j]
        max_result = max(result, max_result)

print(max_result)