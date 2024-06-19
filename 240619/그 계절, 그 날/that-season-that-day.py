def is_date(y, m, d):
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    
    if y%4==0 and y%100!=0 or y%400==0:
        if m==2 and 1<=d<=29:
            return True
        elif m in day_30 and 1<=d<=30:
            return True
        elif m in day_31 and 1<=d<=31:
            return True
    else:
        if m==2 and 1<=d<=28:
            return True
        elif m in day_30 and 1<=d<=30:
            return True
        elif m in day_31 and 1<=d<=31:
            return True
    return False

def what_season(m):
    if 3<=m<=5:
        print('Spring')
    elif 6<=m<=8:
        print('Summer')
    elif 9<=m<=11:
        print('Fall')
    else:
        print('Winter')

y, m, d = map(int, input().split())
if is_date(y, m, d)==False:
    print(-1)
else:
    what_season(m)