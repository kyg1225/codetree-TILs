maps = [list(map(int, input().split())) for _ in range(2)]
sero = [0]*4
total = 0

for i in range(4):
    sero[i] += (maps[0][i]+maps[1][i])/2

for i in range(2):
    for j in range(4):
        total += maps[i][j]


print('{:.1f} {:.1f}'.format(sum(maps[0])/4, sum(maps[1])/4))
print('{:.1f} {:.1f} {:.1f} {:.1f}'.format(*sero))
print('{:.1f}'.format(total/8))