a = list(input())

cnt = 0
for i in range(len(a)-2):
    if a[i]+a[i+1] == '((':
        for j in range(i+2, len(a)-1):
            if a[j]+a[j+1]=='))':
                cnt+=1
            
print(cnt)