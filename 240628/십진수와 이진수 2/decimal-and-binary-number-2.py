n = list(input())
num = 0
for i in range(len(n)):
    num = num*2 + int(n[i])

result= num*17
answer = []
while True:
    if result<2:
        answer.append(result)
        break
    answer.append(result%2)
    result//=2

for i in answer[::-1]:
    print(i, end='')