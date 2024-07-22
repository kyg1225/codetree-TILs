n ,t = map(int, input().split())
r, c, d = input().split()

d_dic = {
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

r, c = int(r)-1, int(c)-1
d_num = d_dic[d]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nr, nc = r + dxs[d_num], c + dys[d_num]
    if in_range(nr, nc):
        r, c = nr, nc
    else:
        d_num = 3 - d_num

print(r+1, c+1)