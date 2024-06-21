class RainyDay:
    def __init__(self, date, dow, weather):
        self.date = date
        self.dow = dow
        self.weather = weather

n = int(input())

rainy_day = RainyDay('9999-99-99', '', '')
for _ in range(n):
    d, do, w = tuple(input().split())

    f = RainyDay(d, do, w)
    if w == 'Rain':
        if rainy_day.date >=f.date:
            rainy_day = f

print(rainy_day.date, rainy_day.dow, rainy_day.weather)