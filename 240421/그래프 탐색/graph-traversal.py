def dfs(node):
    global visited, node_cnt
    visited[node] = 1
    for next_n in graph[node]:
        if not visited[next_n] and graph[next_n]:
            visited[next_n] = 1
            node_cnt += 1
            dfs(next_n)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

node_cnt = 0

for i in range(m):
    start_node, end_node = map(int, input().split())

    graph[start_node].append(end_node)
    graph[end_node].append(start_node)

root_node = 1
dfs(root_node)
print(node_cnt)