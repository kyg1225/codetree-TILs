A = input()
B = input()

for i in range(len(A)):
    if A.find(B) != -1:
        A = A.replace(A[A.find(B):A.find(B)+len(B)],'')
    else:
        break

print(A)