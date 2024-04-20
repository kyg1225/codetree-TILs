s = input()
nums = list(int(input()) for _ in range(len(s)-1))

leng = len(s)
result = list(s)
for i in nums:
    if i >= len(result):
        result.pop()
        print(''.join(result))
    else:
        result.pop(i)
        print(''.join(result))