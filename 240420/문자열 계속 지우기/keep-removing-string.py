A = input()
B = input()

for i in range(len(A)):
    if A.find(B) != -1:
        A = A.replace(result[result.find(B):result.find(B)+len(B)],'')
    else:
        break

print(A)