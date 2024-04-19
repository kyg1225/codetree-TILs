A = input()

chars = ''
cnt = 1
for i in range(1, len(A)):
    if A[i] == A[i-1]:
        cnt += 1
    elif A[i] != A[i-1]:
        chars += A[i-1] + str(cnt)
        cnt = 1

chars += A[-1] + str(cnt)

print(f'{len(chars)}\n{chars}')