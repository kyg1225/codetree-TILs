n = int(input())
arr = list(map(int, input().split()))

def solution(array):
    def lcm(x, y):
        return x * y // gcd(x, y)

    def gcd(x, y):
        while y:
            x, y = y, x%y
        return x

    while True:
        array.append(lcm(array.pop(), array.pop()))
        if len(array) == 1:
            return array[0]

print(solution(arr))