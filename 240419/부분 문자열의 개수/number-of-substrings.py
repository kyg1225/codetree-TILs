s = input()
char = input()

cnt = 0
for i in range(len(s)-1):
    if s[i]+s[i+1] == char:
        cnt += 1

print(cnt)