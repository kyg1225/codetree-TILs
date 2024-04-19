s, q = input().split()
qs = [list(input().split()) for _ in range(int(q))]

for i in qs:
    tmp = ''
    if i[0] == '1':
        s = list(s)
        tmp = s[int(i[1])-1]
        s[int(i[1])-1] = s[int(i[2])-1]
        s[int(i[2])-1] = tmp
        print(''.join(s))

    if i[0] == '2':
        s = ''.join(s)
        print(s.replace(i[1], i[2]))