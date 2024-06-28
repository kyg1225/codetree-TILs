n = list(map(int, input()))
result = 0

for i in range(len(n)):
    result = result*2 + n[i]

print(result)