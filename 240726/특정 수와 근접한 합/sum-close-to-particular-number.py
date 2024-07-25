import sys
INT_MAX = sys.maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))

mini = INT_MAX

for i in range(n):
    for j in range(i+1, n):
        arr[i] = 0
        arr[j] = 0
        result = abs(s - sum(arr))
        mini =  min(result, mini)

print(mini)