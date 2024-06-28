n, k = map(int, input().split())

block = [0]*8
for i in range(k):
    a, b = map(int, input().split())
    block[a]+=1
    block[b]+=1

print(max(block))