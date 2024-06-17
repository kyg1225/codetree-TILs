def is_magic_num(n, m):
    num_list = []
    for i in range(n, m+1):
        if i%3==0 or in_369(i)==True:
            num_list.append(i)
    return len(num_list)

def in_369(num):
    if '3' in str(num) or '6' in str(num) or '9' in str(num):
        return True

a, b = map(int, input().split())
print(is_magic_num(a, b))