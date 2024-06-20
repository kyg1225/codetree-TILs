n = int(input())
arr = list(map(int, input().split()))

def recur(n):
    if n==0:
        return arr[0]

    return max(recur(n-1), arr[n])

print(recur(n-1))