def is_2021y(n1, n2):
    if (1<=n1<=12) and (1<=n2<=31):
        if n1%2==1 or n1==8:
            return True
        elif n1%2==0:
            if n1==2 and n2<=28:
                return True
            elif n2<=30:
                return True
    return False



m, d = map(int, input().split())
if is_2021y(m, d)==True:
    print('Yes')
else:
    print('No')