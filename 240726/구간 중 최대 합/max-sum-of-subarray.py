n, k = map(int, input().split())
arr = list(map(int, input().split()))

maxi = 0
for i in range(n-2):
    result = 0
    result = arr[i]+arr[i+1]+arr[i+2]
    maxi = max(result, maxi)
print(maxi)