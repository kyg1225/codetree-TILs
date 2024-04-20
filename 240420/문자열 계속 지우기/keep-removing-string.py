A = input()
B = input()

result = A
for i in range(len(A)):
    result = result.replace(result[result.find(B):result.find(B)+len(B)],'')
print(result)