def is_div_2(n):
    if n%2==0:
        return True
    return False

def is_div_5(n):
    if str(n)[-1] == '5':
        return True
    return False

def is_div_39(n):
    if n%3 == 0 and n%9 != 0:
        return True
    return False


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_div_2(i)==False and is_div_5(i)==False and is_div_39(i)==False:
        cnt+=1

print(cnt)