def is_yun(y):
    if y%4!=0:
        return 'false'
    if y%100 == 0 and y%400 != 0:
        return 'false'
    return 'true'

y = int(input())
print(is_yun(y))