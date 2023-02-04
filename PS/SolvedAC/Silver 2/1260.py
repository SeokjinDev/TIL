# baekjoon 1260
# https://www.acmicpc.net/problem/1260
# Silver 2

from collections import deque

n, m, v = map(int, input().split())
graph = [[]] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    if graph[a]:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if graph[b]:
        graph[b].append(a)
    else:
        graph[b] = [a]

for g in graph:
    g.sort()

# dfs
visited = [0] * (n+1)
stack = [v]
while stack:
    data = stack.pop()
    if not visited[data]:
        print(data, end=' ')
        visited[data] = 1
        stack.extend(sorted(graph[data], reverse=True))
print()
# bfs
visited = [0] * (n+1)
queue = deque([v])
while queue:
    data = queue.popleft()
    if not visited[data]:
        print(data, end=' ')
        visited[data] = 1
        queue.extend(graph[data])