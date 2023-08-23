from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if graph.get(u): graph[u].append(v)
    else: graph[u] = [v]
    if graph.get(v): graph[v].append(u)
    else: graph[v] = [u]

cnt = 1
visited = [0] * (n+1)
queue = deque(sorted(graph[r]))
visited[r] = cnt
while queue:
    data = queue.popleft()
    if visited[data] == 0:
        visited[data] = (cnt:=cnt+1)
        queue.extend(sorted(graph[data]))
[print(v) for v in visited[1:]]