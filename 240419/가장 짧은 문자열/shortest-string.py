s = list(map(str, input().split()))

maxi = 0
mini = 0
for i in s:
    if maxi <len(i):
        maxi = len(i)
    if mini > len(i):
        mini = len(i)

print(maxi - mini)