m1, d1, m2, d2 = map(int, input().split())

day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
if m2-m1 > 0:
    for i in range(m1+1, m2):
        day += day_of_month[i]
    print(day+d2+(day_of_month[m1]-d1))
else:
    print(day + d2-d1)