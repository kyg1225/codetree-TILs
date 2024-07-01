n, m, k = map(int, input().split())
n_arr = [0]*(m+1)

for i in range(m):
    st_num = int(input())
    n_arr[st_num] += 1

    if n_arr[st_num] >= k:
        print(st_num)
        break
    else:
        if i==(m-1):
            print(-1)