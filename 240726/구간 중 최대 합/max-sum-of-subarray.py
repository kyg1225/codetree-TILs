n, k = map(int, input().split())
arr = list(map(int, input().split()))

maxi = 0
for i in range(n-k+1):
    result = 0
    for j in range(i, i+k):
        result += arr[j]
    maxi = max(result, maxi)
print(maxi)