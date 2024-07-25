import sys
INT_MAX = sys.maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))

mini = INT_MAX
result = 0
for i in range(n):
    for j in range(i+1, n):
        result = sum(arr) - (arr[i]+arr[j])
        mini =  min(abs(s-result), mini)
print(mini)