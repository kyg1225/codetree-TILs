def dfs(idx):
    global node_cnt, visited
    visited[idx] = 1

    for next_node in graph[idx]:
        if not visited[next_node]:
            visited[next_node] = 1
            node_cnt += 1
            dfs(next_node)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
node_cnt = 0

for i in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

dfs(1)

print(node_cnt)