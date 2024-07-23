a = list(input())

cnt = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]=='(' and i < j and a[j]==')':
            cnt+=1
print(cnt)