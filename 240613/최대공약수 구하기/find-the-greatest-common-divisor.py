def shared(x):
    share = []
    for i in range(1, x+1):
        if x%i == 0:
            share.append(i)
    return share

def maxi(n, m):
    max_item = 0
    for item in n:
        if item in m:
            if item > max_item:
                max_item = item
    return max_item

n, m = map(int, input().split())

n_list = shared(n)
m_list = shared(m)

print(maxi(n_list, m_list))