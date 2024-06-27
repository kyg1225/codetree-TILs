n = int(input())
n_list = list(map(int, input().split()))

points = [(num, i) for i, num in enumerate(n_list)]
answer = [0 for _ in range(n)]

points.sort(key=lambda x:(x[0],x[1]))

for i, (_, idx) in enumerate(points):
    answer[idx] = i+1

for i in answer:
    print(i, end=' ')